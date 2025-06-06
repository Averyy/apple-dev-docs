# Creating an embedded assertion

**Framework**: Authentication Services

Request an embedded assertion for login types that require a digital signature for authentication.

#### Overview

During authentication, the system uses the embedded assertion when the login type requires a digital signature for authentication. The system uses this assertion for authentication with a secure enclave key, SmartCard, and encrypted password. The embedded assertion is a Javascript Object Signing and Encryption (JOSE) object that’s formatted per RFC 7523 and signed with the authenticator per RFC 7515. However, the assertion differs from RFC 7523 when using secure enclave key authentication, which is signed using the `ES256` algorithm instead of the `RS256` algorithm in the RFC. This algorithm difference is because secure enclave key supports ellyptic curve keys, not RSA keys.

The following table specifies the header parameters that the system uses to create an embedded assertion:

| Key | Value | Notes |
| --- | --- | --- |
| `typ` | `JWT` | Required if the extension SDK is macOS 13.x. |
|  | `platformsso-login-assertion+jwt` | Required if the extension SDK is macOS 14.x or later. |
| `alg` | `ES256` | Required. The signing algorithm. If secure enclave key, the system only supports `ES256`. |
|  | `ES256`, `RS256`, `RS384`, or `RS512` | Required. If SmartCard, it depends on the key type and key length on the SmartCard. |
| `kid` | The base-64 encoded SHA256 hash of the ANSI X9.63-formatted public key for the signing key | Required. |
| `x5c` | The base-64 encoded signing certificate from the SmartCard | Optional. The value is base-64 encoded per RFC 7517. |
| `loginConfiguration.customAssertionRequestHeaderClaims` merged with `userLoginConfiguration.customAssertionRequestHeaderClaims` |  | Optional. If present, adds key value pairs to the assertion. |

The following table specifies the body parameters that the system uses to create an embedded assertion:

| Key | Value | Notes |
| --- | --- | --- |
| `aud` | [`audience`](asauthorizationproviderextensionloginconfiguration/audience.md) | Required. The identity provider (IdP) needs to verify this value to ensure that the assertion was created for them. |
| `iat` | The current time | Required. The IdP needs to verify this value. |
| `exp` | 5 minutes from now | Required. The IdP needs to verify this value. |
| `iss` | [`loginUserName`](asauthorizationproviderextensionuserloginconfiguration/loginusername.md) | Required. If not set, the system uses the local account name. |
| `sub` | [`loginUserName`](asauthorizationproviderextensionuserloginconfiguration/loginusername.md) | Required. If not set, the system uses the local account name. |
| `nonce` | A nonce value | Required. The IdP needs to verify that this value matches the nonce in the login request. |
| [`serverNonceClaimName`](asauthorizationproviderextensionloginconfiguration/servernonceclaimname.md) or `request_nonce` | The value returned from the nonce request | Required. The key name is either the [`serverNonceClaimName`](asauthorizationproviderextensionloginconfiguration/servernonceclaimname.md) or the default value `request_nonce`. |
| `scope` | `openid offline_access` and [`additionalScopes`](asauthorizationproviderextensionloginconfiguration/additionalscopes.md) | Required. The requested scope for the assertion. The default value is `openid offline_access` and any additional ones are appended to it. The default additional scope is `urn:apple:platformsso`. This value needs to match the scope in the login request. |
| `loginConfiguration.customAssertionRequestBodyClaims` merged with `userLoginConfiguration.customAssertionRequestBodyClaims` |  | Optional. If present, adds key value pairs to the assertion. |
| [`serverNonceClaimName`](asauthorizationproviderextensionloginconfiguration/servernonceclaimname.md) or `request_nonce` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) | The value returned from the nonce request | Required. The key name is either the [`serverNonceClaimName`](asauthorizationproviderextensionloginconfiguration/servernonceclaimname.md) or the default value `request_nonce`. |

The following code provides an example of an embedded assertion request:

```javascript
{
    "typ" : "JWT",
    "alg" : "ES256",
    "kid" : "pmQkkBPmTgijIX00/SpKUjzvm3k2MZAZRiVR3iEv8l0="
}.{
    "nonce" : "7DE40CF9-C885-4397-B48E-E95EDD22038A",
    "request_nonce" : "AwABAAAAAAADAOz_BADv_xtgu_SM1Mvoq02PYz_YfXxx5FAgcLHLNikH6gjrBWwcqnRW_haxqO9JCiPat5KfkTily04S8EH3AQwVsWCxHYQgAA",
    "iat" : "1655416300",
    "sub" : "foo",
    "scope" : "openid offline_access urn:apple:platformsso",
    "exp" : "1655416600",
    "aud" : "060798FF-814E-4C38-97F8-28C954B7E058",
    "iss" : "foo"
}.[Signature]

```

For more information, see [`Authentication process`](authentication-process.md).

## See Also

- [Performing a WS-Trust login request](performing-a-ws-trust-login-request.md)
  Create a WS-Trust login request using the metadata exchange data (MEX) response.
- [Creating an encrypted embedded assertion](creating-an-encrypted-embedded-assertion.md)
  Request an encrypted embedded assertion for login types that require password encryption.
- [Creating and validating a login request](creating-and-validating-a-login-request.md)
  Create a signed JOSE login request.
- [Creating a refresh request](creating-a-refresh-request.md)
  Refresh a non-expired token instead of sending a new login request.
- [Supporting key requests and key exchange requests](supporting-key-requests-and-key-exchange-requests.md)
  Support the platform SSO 2.0 protocol for encryption and decryption operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/creating-an-embedded-assertion)*