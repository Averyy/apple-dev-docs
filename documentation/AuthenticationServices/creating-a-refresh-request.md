# Creating a refresh request

**Framework**: Authentication Services

Refresh a non-expired token instead of sending a new login request.

#### Overview

The system sends a refresh request instead of a login request when a token hasn’t expired yet and the [`refreshEndpointURL`](asauthorizationproviderextensionloginconfiguration/refreshendpointurl.md) is set. The refresh request also sends a server nonce request before it begins.

A refresh request uses the previous refresh token to request a new token without prompting the user for credentials. The system attempts it when the existing token hasn’t expired and the time since the last full login hasn’t exceeded the `LoginFrequency` in the Device Management profile. It doesn’t apply to User Secure Enclave key authentication, because the user isn’t prompted for credentials.

The refresh request is a JSON Object Signing and Encryption object (JOSE) object that’s formatted per RFC 7519 and signed with the `DeviceSigningKey` and `ES256` per RFC 7515. Processing the refresh network request and response is the same as for a JSON Web Encryption (JWE) login response. For more information, see [`Creating a JSON Web Encryption (JWE) login response`](creating-a-json-web-encryption-jwe-login-response.md).

The following table specifies the header parameters that the system uses to create a refresh request:

| Key | Value | Notes |
| --- | --- | --- |
| `typ` | `platformsso-refresh-request+jwt` | Required. |
| `alg` | `ES256` | Required. The signing algorithm. Only ES256 is supported. |
| `kid` | The base-64 encoded SHA256 hash of the ANSI X9.63 formatted public key for the signing identity | Required. |
| `x5c` | The base-64 encoded device signing certificate from [`saveCertificate(_:keyType:)`](asauthorizationproviderextensionloginmanager/savecertificate(_:keytype:).md). | Optional. If the certificate is set, the system includes it here. The value is base-64 encoded per RFC 7517. |
| `loginConfiguration.customRefreshRequestHeaderClaims` |  | Optional. If present, adds key value pairs to the JWT. |

The following table specifies the body parameters that the system uses to create a refresh request:

| Key | Value | Notes |
| --- | --- | --- |
| `client_id` | [`clientID`](asauthorizationproviderextensionloginconfiguration/clientid.md) | Required. The open id `client_id` for login. |
| `iss` | [`clientID`](asauthorizationproviderextensionloginconfiguration/clientid.md) | Required. Per RFC 7523 Section 3. |
| `exp` | 5 minutes from now | Required. Per RFC 7523 Section 3. |
| `scope` | `openid offline_access` and [`additionalScopes`](asauthorizationproviderextensionloginconfiguration/additionalscopes.md) | Required. The requested scope for the assertion. The default value is `openid offline_access` and the system appends any additional ones to it. The default additional scope is `urn:apple:platformsso` If there’s an embedded assertion, this value must match the scope in the embedded assertion JWT. |
| `nonce` | A nonce value | Required. A unique nonce for this request. |
| `aud` | [`tokenEndpointURL`](asauthorizationproviderextensionloginconfiguration/tokenendpointurl.md) | Required. The refresh endpoint URL host and path. |
| `iat` | The current time | Required. The IdP needs to verify this value. |
| [`serverNonceClaimName`](asauthorizationproviderextensionloginconfiguration/servernonceclaimname.md) or `request_nonce` | The value that the nonce request returns. | Required. The key name is either the [`serverNonceClaimName`](asauthorizationproviderextensionloginconfiguration/servernonceclaimname.md) or the default value `request_nonce`. |
| `grant_type` | `refresh_token` | Required. |
| `refresh_token` | The previous refresh token | Required. |
| `jwe_crypto` | A dictionary with the following three values: | Required. The system uses the values in the dictionary to encrypt the response. |
| `enc` | `A256GCM` | Required. The supported encryption algorithm for the response per RFC 7518 Section 4.6. |
| `alg` | `ECDH-ES` | Required. The supported key agreement algorithm for the response per RFC 7518 Section 5.3. |
| `apv` | The base-64 URL encoded `PartyVInfo` to use for the response | Required. Per RFC 7518 Section 4.6.1.3. The value for `PartyVInfo` to encrypt the response. See Configure Concat KDF in [`Creating an encrypted embedded assertion`](creating-an-encrypted-embedded-assertion.md) for more information. |
| `loginConfiguration.customRefreshRequestBodyClaims` |  | Optional. If present, adds the key value pairs to the JWT. |

The following code provides an example of a refresh request:

```javascript
{
    "kid" : "10gy5SeDGL4KRZb0gKyFmPuV9LBAcm/Istdk4lgn24M=",
    "x5c" : "MIIBg...nFg==",
    "typ" : "platformsso-refresh-request+jwt",
    "alg" : "ES256"
}.{
    "iat" : 1685750697,
    "jwe_crypto" : {
        "alg" : "ECDH-ES",
        "enc" : "A256GCM",
        "apv" : "AAAAB...zZEMA"
    },
    "nonce" : "A978348D-DEDF-4AF2-94D4-FCC60B6736D0",
    "request_nonce" : "AwABA...YQgAA",
    "scope" : "openid offline_access urn:apple:platformsso",
    "refresh_token" : "abcd1234",
    "grant_type" : "refresh_token",
    "exp" : 1685750997,
    "aud" : "https://localhost.apple.com:8888/auth/token",
    "client_id" : "aaff1524-fa35-40c5-94e3-2b233c5f2965",
    "iss" : "aaff1524-fa35-40c5-94e3-2b233c5f2965"
}.[Signature]
```

## See Also

- [Performing a WS-Trust login request](performing-a-ws-trust-login-request.md)
  Create a WS-Trust login request using the metadata exchange data (MEX) response.
- [Creating an embedded assertion](creating-an-embedded-assertion.md)
  Request an embedded assertion for login types that require a digital signature for authentication.
- [Creating an encrypted embedded assertion](creating-an-encrypted-embedded-assertion.md)
  Request an encrypted embedded assertion for login types that require password encryption.
- [Creating and validating a login request](creating-and-validating-a-login-request.md)
  Create a signed JOSE login request.
- [Supporting key requests and key exchange requests](supporting-key-requests-and-key-exchange-requests.md)
  Support the platform SSO 2.0 protocol for encryption and decryption operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/creating-a-refresh-request)*