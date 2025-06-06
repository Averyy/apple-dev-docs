# Performing a WS-Trust login request

**Framework**: Authentication Services

Create a WS-Trust login request using the metadata exchange data (MEX) response.

#### Overview

After receiving a WS-Trust MEX response, the next step that the system performs for federated authentication with WS-Trust, meaning between security domains, is to send a login request to a federated identity provider (IdP).

The system uses the [`federationRequestURN`](asauthorizationproviderextensionloginconfiguration/federationrequesturn.md) and the URLs specified in the MEX response to create the WS-Trust login request, per Web Services Security Username Token Profile Version 1.1.1. The system doesn’t support `PasswordDigest`. The system sends the WS-Trust login using Simple Object Access Protocol (SOAP) to the endpoint in the MEX response.

For more information about federated authentication with WS-Trust, see [`Authentication process`](authentication-process.md).

##### Receive the Ws Trust Login Response

The system loads the SOAP response as XML and validates it, which includes checking that the nonce is correct and the created and expires dates are current. The system then parses the `TokenType` and uses it to set the correct `grant_type` in the platform SSO login request.

## See Also

- [Creating an embedded assertion](creating-an-embedded-assertion.md)
  Request an embedded assertion for login types that require a digital signature for authentication.
- [Creating an encrypted embedded assertion](creating-an-encrypted-embedded-assertion.md)
  Request an encrypted embedded assertion for login types that require password encryption.
- [Creating and validating a login request](creating-and-validating-a-login-request.md)
  Create a signed JOSE login request.
- [Creating a refresh request](creating-a-refresh-request.md)
  Refresh a non-expired token instead of sending a new login request.
- [Supporting key requests and key exchange requests](supporting-key-requests-and-key-exchange-requests.md)
  Support the platform SSO 2.0 protocol for encryption and decryption operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/performing-a-ws-trust-login-request)*