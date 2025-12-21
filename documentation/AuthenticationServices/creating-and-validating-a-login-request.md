# Creating and validating a login request

**Framework**: Authentication Services

Create a signed JOSE login request.

#### Overview

Your login configuration instructs Platform SSO how to create and validate a login request based on the authentication method. This article provides a description of the parameters that the system uses to create and send a login request, followed by code snippet examples of login requests for each authentication method.

The login request is a JSON Object Signing and Encryption object (JOSE) that’s formatted per RFC 7519 and signed with the `DeviceSigningKey` and `ES256` per RFC 7515.

For more information, see [`Configuring authentication with the identity provider (IdP)`](configuring-authentication-with-the-identity-provider-idp.md).

##### Create the Login Request

The following table specifies the header parameters that the system uses to create a login request:

| Key | Value | Notes |
| --- | --- | --- |
| `typ` | `JWT` | Required if the extension SDK is macOS 13.x. |
|  | `platformsso-login-request+jwt` | Required if the extension SDK is macOS 14.x or later. |
| `alg` | `ES256` | Required: The signing algorithm. The system only supports `ES256`. |
| `kid` | The base-64 encoded SHA256 hash of the ANSI X9.63 formatted public key for the signing identity | Required. |
| `x5c` | The base-64 encoded device signing certificate from [`saveCertificate(_:keyType:)`](asauthorizationproviderextensionloginmanager/savecertificate(_:keytype:).md) | Optional. If the certificate is set, the system includes it here. The value is base-64 encoded per RFC 7517. |
| `loginConfiguration.customLoginRequestHeaderClaims` |  | Optional. If present, adds key value pairs to the JSON Web Token (JWT). |

The following table specifies the body parameters that the system uses to create a login request:

| Key | Value | Notes |
| --- | --- | --- |
| `client_id` | [`clientID`](asauthorizationproviderextensionloginconfiguration/clientid.md) | Required. The open id `client_id` for login. |
| `iss` | [`clientID`](asauthorizationproviderextensionloginconfiguration/clientid.md) | Required. Per RFC 7523 Section 3. |
| `exp` | 5 minutes from now | Required. Per RFC 7523 Section 3. |
| `scope` | `openid offline_access` and [`additionalScopes`](asauthorizationproviderextensionloginconfiguration/additionalscopes.md) | Required. The requested scope for the assertion. The default value is `openid offline_access` and any additional ones are appended to it. The default additional scope is `urn:apple:platformsso`. If there’s an embedded assertion, this value needs to match the scope in the embedded assertion JWT. |
| `nonce` | An nonce value | Required. A unique nonce for this request. If there’s an embedded assertion and it includes the nonce, the IdP needs to verify that this value matches the `nonce` in the embedded assertion JWT. |
| `aud` | [`keyEndpointURL`](asauthorizationproviderextensionloginconfiguration/keyendpointurl.md) | The token endpoint URL host and path. |
| `iat` | The current time | Required. The IdP needs to verify this value. |
| `request_nonce` or [`serverNonceClaimName`](asauthorizationproviderextensionloginconfiguration/servernonceclaimname.md) | The value that the nonce request returns | Required. The key name is either the [`serverNonceClaimName`](asauthorizationproviderextensionloginconfiguration/servernonceclaimname.md) or the default value `request_nonce`. |
| `username` | [`loginUserName`](asauthorizationproviderextensionuserloginconfiguration/loginusername.md) | Required. If not set, the system uses the local account name. If there’s an embedded assertion, this value needs to match the scope in the embedded assertion JWT. |
| `sub` | [`loginUserName`](asauthorizationproviderextensionuserloginconfiguration/loginusername.md) | Required. Per RFC 7523 Section 3. |
| `grant_type` | `password` | Required. The `grant_type` contains the requested authentication type. |
|  | `urn:ietf:params:oauth:grant-type:jwt-bearer` | Use this value when requesting User Secure Enclave Key, SmartCard, or Encrypted Password authentication. |
|  | `urn:ietf:params:oauth:grant-type:saml1_1-bearer` | When using federation and the WS-Trust response token is a Security Assertion Markup Language (SAML) 1.1 token. |
|  | `urn:ietf:params:oauth:grant-type:saml2-bearer` | When using federation and the WS-Trust response token is a SAML 2.0 token. |
| `password` | The password for authentication | Required when `grant_type` is `password` and the [`loginRequestEncryptionPublicKey`](asauthorizationproviderextensionloginconfiguration/loginrequestencryptionpublickey.md) isn’t set. |
| `assertion` | The signed or encrypted embedded assertion | Required when `grant_type` isn’t `password`. For WS-Trust federation, the value is the base-64 encoded SAML token from the WS-Trust response. |
| `jwe_crypto` | A dictionary with the following three values: | Required. The system uses the values in the dictionary to encrypt the response. |
| `enc` | `A256GCM` | Required. The supported encryption algorithm for the response per RFC 7518 Section 4.6. |
| `alg` | `ECDH-ES` | Required. The supported key agreement algorithm for the response per RFC 7518 Section 5.3. |
| `apv` | The base-64 URL encoded `PartyVInfo` to use for the response | Required. Per RFC 7518 Section 4.6.1.3. The value for `PartyVInfo` to encrypt the response. See Configure Concat KDF in [`Creating an encrypted embedded assertion`](creating-an-encrypted-embedded-assertion.md) for more information. |
| [`previousRefreshTokenClaimName`](asauthorizationproviderextensionloginconfiguration/previousrefreshtokenclaimname.md) if [`includePreviousRefreshTokenInLoginRequest`](asauthorizationproviderextensionloginconfiguration/includepreviousrefreshtokeninloginrequest.md) is [`true`](https://developer.apple.com/documentation/Swift/true) | If there’s a previous `refresh_token` in the SSO tokens, the system includes the value here. | Optional. This allows the IdP to carry over any MFA or step-up authentication results per their policy. |
| `loginConfiguration.customLoginRequestBodyClaims` |  | Optional. If present, adds the key value pairs to the JWT. |
| `claims : {` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)     `“id_token” : {` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)         `“groups” : {` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)             `“values” : groupsToRequest` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `} } }` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) or [`groupRequestClaimName`](asauthorizationproviderextensionloginconfiguration/grouprequestclaimname.md) | If new user, user authorization mode is groups, or authorization is enabled, the system includes the set of groups here. | Optional. If the user is a member of any of the groups, then the `id_token` the login response returns needs to include the groups. |

The login network request is an HTTP POST to the [`keyEndpointURL`](asauthorizationproviderextensionloginconfiguration/keyendpointurl.md) that’s formatted per RFC 7523 and includes the following parameters:

| Key | Value | Notes |
| --- | --- | --- |
| `platform_sso_version` | `1` | Required. The version of the login protocol. |
| `grant_type` | `urn:ietf:params:oauth:grant-type:jwt-bearer` | Required. The login assertion type. |
| `request` | The base-64 URL encoded signed login request | Required if the extension SDK is macOS 13.x. |
| [`customRequestJWTParameterName`](asauthorizationproviderextensionloginconfiguration/customrequestjwtparametername.md) or `assertion` | The base 64 URL Encoded signed login request | Required if the extension SDK is macOS 14.x or newer. |
| [`customLoginRequestValues`](asauthorizationproviderextensionloginconfiguration/customloginrequestvalues.md) |  | Optional. If present, adds the key value pairs to the login request. |

The following code provides an example of a login network request:

```javascript
POST /oauth2/token HTTP/1.1
Host: auth.example.com
Accept: application/platformsso-login-response+jwt
Content-Type: application/x-www-form-urlencoded
client-request-id: DCAB01D3-B1FE-4E1C-802F-B3EBDCDF9E67
platform_sso_version=1.0&grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer&assertion=ewogI...A063Eg
```

##### Validate the Login Request

The identity provider (IdP) needs to validate the login request by performing several checks to verify that the:

- JWT signature is valid.
- Signing identity is a known device.
- `client_id` is correct.
- `server_nonce` is valid and not replayed.
- `aud` is the IdP.

If the `grant_type` is password, the IdP needs to verify that the `password` is correct for the supplied [`loginUserName`](asauthorizationproviderextensionuserloginconfiguration/loginusername.md).

If the `grant_type` is `urn:ietf:params:oauth:grant-type:jwt-bearer,` the IdP needs to perform several checks on the embedded assertion to verify that the:

- JWT signature or decrypts is valid.
- Signing identity is known for the user.
- Embedded assertion is for the same user as the login request.
- `iat` claim isn’t in the future.
- `exp` claim isn’t in the past.
- `scope` matches the login request.
- `audience` is the IdP.
- `nonce` matches the login request, if included.

##### Create a Login Request with a Password

The following code provides an example of a login request with a password:

```javascript
{
    "kid" : "WMPGy7o9k+Wh7DB3V7oXBPh3QCP4xuTXtMANwfzn6+k=",
    "x5c" : "MIIBh...8r1E=",
    "typ" : "platformsso-login-request+jwt",
    "alg" : "ES256"
}.{
    "jwe_crypto" : {
        "alg" : "ECDH-ES",
        "enc" : "A256GCM",
        "apv" : "AAAAB...zVGRQ"
    },
    "exp" : 1685737193,
    "nonce" : "A79070DA-4058-4060-B09D-91CECFA635FE",
    "request_nonce" : "AwABA...YQgAA",
    "scope" : "openid offline_access urn:apple:platformsso",
    "grant_type" : "password",
    "iss" : "aaff1524-fa35-40c5-94e3-2b233c5f2965",
    "password" : "password redacted",
    "sub" : "foo",
    "claims" : {
        "id_token" : {
            "groups" : {
                "values" : [
                    "com.example.foogroup",
                    "com.example.bargroup"
                ]
            }
        }
    },
    "aud" : "https://localhost.apple.com:8888/auth/token",
    "iat" : 1685736893,
    "username" : "foo",
    "client_id" : "aaff1524-fa35-40c5-94e3-2b233c5f2965"
}.[Signature]
```

##### Create a Login Request with an Encrypted Password

The following code provides an example of a login request with an encrypted password:

```javascript
{
    "kid" : "o0sPO3BU5DwCIibsHvfVN4D9tOwVcy1Yv0kKKmRG8qk=",
    "x5c" : "MIIBg...xhg==",
  "typ" : "platformsso-login-request+jwt",
  "alg" : "ES256"
}.{
    "jwe_crypto" : {
        "alg" : "ECDH-ES",
        "enc" : "A256GCM",
        "apv" : "AAAAB...zBCRA"
    },
    "exp" : 1685737279,
    "nonce" : "0D7578A1-DE84-4237-A77D-62DDEB2670BD",
    "request_nonce" : "AwABA...YQgAA",
    "scope" : "openid offline_access urn:apple:platformsso",
    "grant_type" : "urn:ietf:params:oauth:grant-type:jwt-bearer",
    "iss" : "aaff1524-fa35-40c5-94e3-2b233c5f2965",
    "sub" : "foo",
    "claims" : {
        "id_token" : {
            "groups" : {
                "values" : [
                    "com.example.foogroup",
                    "com.example.bargroup"
                ]
            }
        }
    }, 
    "aud" : "https://localhost.apple.com:8888/auth/token",
    "username" : "foo",
    "assertion" : "ewogICJlbmMiIDogIkEyNTZHQ00iLAogICJhcHYiIDogIkFBQUFEVUZRVUV4RlJVMUNSVVJFUlVRQUFBQkJCQ1g4N2Vxb25XeU5VTnoySmVIMndHNjhfV2lQZlFsSnc2QWlEdkhTRDA4bjVIZG4xb0RVQnhoTF9UUmFydmhVVUdEWXNuQlJrMkhSSF9ab1hHdHBVbmNBQUFCdVFYZEJRa0ZCUVVGQlFVRkVRVTk2WDBKQlJIWmZlSFJuZFY5VFRURk5kbTl4TURKUVdYcGZXV1pZZUhnMVJrRm5ZMHhJVEU1cGEwZzJaMnB5UWxkM1kzRnVVbGRmYUdGNGNVODVTa05wVUdGME5VdG1hMVJwYkhrd05GTTRSVWd6UVZGM1ZuTlhRM2hJV1ZGblFVRSIsCiAgImFsZyIgOiAiRUNESC1FUyIsCiAgImVwayIgOiB7CiAgICAieSIgOiAiOUVfN0ZyeTlUbDhZdlBncHgzdGc0QTlaQ1FOZkZlZ1BuUWQ0MzNLN0xOTSIsCiAgICAieCIgOiAiU2owYlpzZkhmM3kyMUJRajZ0ejBkUkFwUnhmRGdxdTFwbi1nUGpBcmFCTSIsCiAgICAia3R5IiA6ICJFQyIsCiAgICAiY3J2IiA6ICJQLTI1NiIKICB9LAogICJraWQiIDogIjd5MXhYYzRJNmlBeWxkbVZrSWVHdFF4bzhOUnEyRmdLRmIrK09yMTNqeFU9IiwKICAiYXB1IiA6ICJBQUFBQlVGUVVFeEZBQUFBUVFSS1BSdG14OGRfZkxiVUZDUHEzUFIxRUNsSEY4T0NxN1dtZjZBLU1DdG9FX1JQLXhhOHZVNWZHTHo0S2NkN1lPQVBXUWtEWHhYb0Q1MEhlTjl5dXl6VCIsCiAgInR5cCIgOiAicGxhdGZvcm1zc28tZW5jcnlwdGVkLWxvZ2luLWFzc2VydGlvbitqd3QiCn0..PCPBwllPzLJzaTiw.4InQHbgPs51ExvjLCutmLHzSVLJkxfD5B9lNC1w6H9-7D_FzuinchO6O5Qf0if6IWG0G_bnROLgOvdBEle9Q_0LtF8odeXThBkDszEMqTNpkYhCHmtU6cZgT-lUeHwrA-9mONF5WO4KMIavZOJ_n-6DZWvdMOCgzokx4-OiiPqh5fo0B6MAEQu4AITtXZe7oD6HZAI33zdUD-dQxKNAO2I0aP9RIUP8eLyXkrPY8nIWBRx88aPEtGMs_3uT29BBqGMcMV83zuYFA6TNXTVJy8bCAbeCNZceQbT7lyaFPxZ0s6hg7TSpvIRz7fJX3EXo6a2u4CkkUVgcQrHnfF1aX7v3WOLnYnV1nSO8YPDQYi_m2-bkFSbScmC-ERgmod3m0eV10jA4ag6-TSyB_zlhsVclJQ4suOVyw2YO2Z7AgjRK-BO6GiEMBgbR-P5ad3Zk7v1DVl2MWFMalLfbdcHQNP5drpi4BiY1j0SkFxmdcjTWHea6YAYhmQVjyj29Rd2SOYjRXSXelMftxXO5cZQ.bp-jwZlbdDoL7qjeBbGClw",
    "client_id" : "aaff1524-fa35-40c5-94e3-2b233c5f2965",
    "iat" : 1685736979
}.[Signature]
```

##### Create a Login Request with a Secure Enclave Key

The following code provides an example of a login request with a secure enclave key:

```javascript
{
    "kid" : "R7hXA3CADcaDzreUMbIJWkTw5IjreuwANl9Rj2tAHbk=",
    "x5c" : "MIIBg...XuQ==",
    "typ" : "platformsso-login-assertion+jwt",
    "alg" : "ES256"
}.{
    "jwe_crypto" : {
        "alg" : "ECDH-ES",
        "enc" : "A256GCM",
        "apv" : "AAAAB...jM5RQ"
    },
    "exp" : 1685737367,
    "nonce" : "E0DA0950-3EC4-486E-9C70-A9B4D28CB39E",
    "request_nonce" : "AwABAAAAAAADAOz_BADv_xtgu_SM1Mvoq02PYz_YfXxx5FAgcLHLNikH6gjrBWwcqnRW_haxqO9JCiPat5KfkTily04S8EH3AQwVsWCxHYQgAA",
    "scope" : "openid offline_access urn:apple:platformsso",
    "grant_type" : "urn:ietf:params:oauth:grant-type:jwt-bearer",
    "iss" : "aaff1524-fa35-40c5-94e3-2b233c5f2965",
    "sub" : "foo",
    "claims" : {
        "id_token" : {
            "groups" : {
                "values" : [
                    "com.example.foogroup",
                    "com.example.bargroup"
                ]
            } 
        }
    }, 
    "aud" : "https://localhost.apple.com:8888/auth/token",
    "username" : "foo",
    "assertion" : "ewogICJ0eXAiIDogInBsYXRmb3Jtc3NvLWxvZ2luLWFzc2VydGlvbitqd3QiLAogICJhbGciIDogIkVTMjU2IiwKICAia2lkIiA6ICJ3dzJyVFhrSWNOeG5ma3BBZi8zRFN3ZldBL2pKOUpuNVh0dlhKMVh5NzhNPSIKfQ.ewogICJub25jZSIgOiAiRTBEQTA5NTAtM0VDNC00ODZFLTlDNzAtQTlCNEQyOENCMzlFIiwKICAiaWF0IiA6IDE2ODU3MzcwNjcsCiAgInJlcXVlc3Rfbm9uY2UiIDogIkF3QUJBQUFBQUFBREFPel9CQUR2X3h0Z3VfU00xTXZvcTAyUFl6X1lmWHh4NUZBZ2NMSExOaWtINmdqckJXd2NxblJXX2hheHFPOUpDaVBhdDVLZmtUaWx5MDRTOEVIM0FRd1ZzV0N4SFlRZ0FBIiwKICAic3ViIiA6ICJmb28iLAogICJzY29wZSIgOiAib3BlbmlkIG9mZmxpbmVfYWNjZXNzIHVybjphcHBsZTpwbGF0Zm9ybXNzbyIsCiAgImV4cCIgOiAxNjg1NzM3MzY3LAogICJhdWQiIDogIjA2MDc5OEZGLTgxNEUtNEMzOC05N0Y4LTI4Qzk1NEI3RTA1OCIsCiAgImlzcyIgOiAiZm9vIgp9.jmAh1SQJVaqhQhYc5QFGq7R_CsSeMxGF9KFn7PERV9TP37qe5q1MIhdspbFLShK-_7YcjqpX-thzBVINaXNbnQ",
    "client_id" : "aaff1524-fa35-40c5-94e3-2b233c5f2965",
    "iat" : 1685737067
}.[Signature]
```

##### Create a Login Request with a Smartcard

The following code provides an example of a login request with a SmartCard:

```javascript
{
    "kid" : "MvmFTLE0N7t+SPx8QRYjPB2JzeCYPyL7rZTjsFAlOzs=",
    "x5c" : "MIIBg...RtQ==",
    "typ" : "platformsso-login-request+jwt",
    "alg" : "ES256"
}.{
    "jwe_crypto" : {
        "alg" : "ECDH-ES",
        "enc" : "A256GCM",
        "apv" : "AAAAB...Tg1MQ"
    },
    "exp" : 1685737424,
    "nonce" : "CBA6437A-ED3F-438C-B859-078E058F1851",
    "request_nonce" :"AwABA...YQgAA",
    "scope" : "openid offline_access urn:apple:platformsso",
    "grant_type" : "urn:ietf:params:oauth:grant-type:jwt-bearer",
    "iss" : "aaff1524-fa35-40c5-94e3-2b233c5f2965",
    "sub" : "foo",
    "claims" : {
        "id_token" : {
            "groups" : {
                "values" : [
                    "com.example.foogroup",
                    "com.example.bargroup"
                ]
            }
        }
    }, 
    "aud" : "https://localhost.apple.com:8888/auth/token",
    "username" : "foo",
    "assertion" : "ewogICJraWQiIDogIlV3M3ZzRGI4dW1IVVgwNWE2TUNibEVieXBiSE5HVU0xTUNFK1gxaE5hOFk9IiwKICAieDVjIiA6ICJNSUlCakRDQ0FUR2dBd0lCQWdJQkFUQUtCZ2dxaGtqT1BRUURBakE3TVJnd0ZnWURWUVFEREE5bWIyOUFaWGhoYlhCc1pTNWpiMjB4Q3pBSkJnTlZCQVlUQWxWVE1SSXdFQVlEVlFRS0V3bEJjSEJzWlNCSmJtTXdIaGNOTWpNd05qQXlNakF4T0RRMFdoY05NalF3TmpBeE1qQXhPRFEwV2pBN01SZ3dGZ1lEVlFRRERBOW1iMjlBWlhoaGJYQnNaUzVqYjIweEN6QUpCZ05WQkFZVEFsVlRNUkl3RUFZRFZRUUtFd2xCY0hCc1pTQkpibU13V1RBVEJnY3Foa2pPUFFJQkJnZ3Foa2pPUFFNQkJ3TkNBQVFqWWovNzFPMmhrYWJwOTA5RTlmcmxmc2hSTysxNExzd0NZanlaY3dRSC9aeEpnM1BidjZkL3NIelNTd0ZXS2kydFJaS1VTS3BxQXhrdXpZaXZiRnVCb3lZd0pEQVNCZ05WSFJNQkFmOEVDREFHQVFIL0FnRUFNQTRHQTFVZER3RUIvd1FFQXdJQUFEQUtCZ2dxaGtqT1BRUURBZ05KQURCR0FpRUF3SWU4L2FXOXd1MjFUMWh1cEFNZkt4OUhvQkxsRkpvaE5QQlRrcFh4NGNJQ0lRQ0hVRGdySGZ1RTNRZjRmZi8wV1BueU9mc1g4aCsvVXZvUDgxUU1XcGtPanc9PSIsCiAgInR5cCIgOiAicGxhdGZvcm1zc28tbG9naW4tYXNzZXJ0aW9uK2p3dCIsCiAgImFsZyIgOiAiRVMyNTYiCn0.ewogICJub25jZSIgOiAiQ0JBNjQzN0EtRUQzRi00MzhDLUI4NTktMDc4RTA1OEYxODUxIiwKICAiaWF0IiA6IDE2ODU3MzcxMjQsCiAgInJlcXVlc3Rfbm9uY2UiIDogIkF3QUJBQUFBQUFBREFPel9CQUR2X3h0Z3VfU00xTXZvcTAyUFl6X1lmWHh4NUZBZ2NMSExOaWtINmdqckJXd2NxblJXX2hheHFPOUpDaVBhdDVLZmtUaWx5MDRTOEVIM0FRd1ZzV0N4SFlRZ0FBIiwKICAic3ViIiA6ICJmb28iLAogICJzY29wZSIgOiAib3BlbmlkIG9mZmxpbmVfYWNjZXNzIHVybjphcHBsZTpwbGF0Zm9ybXNzbyIsCiAgImV4cCIgOiAxNjg1NzM3NDI0LAogICJhdWQiIDogIjA2MDc5OEZGLTgxNEUtNEMzOC05N0Y4LTI4Qzk1NEI3RTA1OCIsCiAgImlzcyIgOiAiZm9vIgp9.Ybc1XQeKUO5y5eMvKMVnHj5j-bqh8UnhUfDc76RJFG1viuc3M9OI0D7lKylLcw0V9Y5H-ZAmbxLKg47yh8qxaw",
    "client_id" : "aaff1524-fa35-40c5-94e3-2b233c5f2965",
    "iat" : 1685737124
}.[Signature]
```

## See Also

- [Performing a WS-Trust login request](performing-a-ws-trust-login-request.md)
  Create a WS-Trust login request using the metadata exchange data (MEX) response.
- [Creating an embedded assertion](creating-an-embedded-assertion.md)
  Request an embedded assertion for login types that require a digital signature for authentication.
- [Creating an encrypted embedded assertion](creating-an-encrypted-embedded-assertion.md)
  Request an encrypted embedded assertion for login types that require password encryption.
- [Creating a refresh request](creating-a-refresh-request.md)
  Refresh a non-expired token instead of sending a new login request.
- [Supporting key requests and key exchange requests](supporting-key-requests-and-key-exchange-requests.md)
  Support the Platform SSO 2.0 protocol for encryption and decryption operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/creating-and-validating-a-login-request)*