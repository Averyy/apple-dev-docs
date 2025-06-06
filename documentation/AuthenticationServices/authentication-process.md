# Authentication process

**Framework**: Authentication Services

Use a system-supported method to authenticate with an identity provider.

#### Overview

Platform SSO supports several methods to authenticate with an identity provider (IdP) that stores and verfies user identities. Each method includes specific steps to complete the authentication process. At a high level, authentication begins with the system requesting a server nonce, which includes an anti-replay value. Next, the system creates a login request per requirements of the authentication method, sends the request, receives a response, and processes it.

This flowchart provides a high-level overview of authentication using password, secure enclave key, SmartCard, and encrypted password:

![A flowchart that shows a Device icon and Identity provider icon at the top of a looping process that starts with requesting and receiving a server nonce value, followed by sending a JSON Object Signing and Encryption (JOSE) login request and receiving the JSON Web Encryption (JWE) response. For secure enclave key, SmartCard, and encrypted password authentication, the next step involves sending an embedded assertion login JOSE and receiving the JWE response. The last step involves decrypting and validating the login response and saving the tokens.” ](https://docs-assets.developer.apple.com/published/7c4881540f1ee32aca3a8fee366e6c75/media-4302344%402x.png)

For password and encrypted password authentication, the IdP uses the local account password and keeps it in sync, including password updates from the login window and screensaver unlock. The secure enclave key authenticates with the IdP without a password and without changing the local password, and high-security customers can use a SmartCard to authenticate with the IdP.

Platform SSO also facilitates federated authentication with WS-Trust. Federation enables authentication between security domains, such as from a local IdP to a cloud IdP. In WS-Trust authentication, a federated IdP uses the local account password for authentication.

This flowchart provides a high-level overview of WS-Trust authentication, which includes preauthentication (for dynamic WS-Trust), obtaining federation metadata, authenticating with a federated IdP, and logging in with the IdP:

![A flowchart that shows a Device icon, Identity provider icon, and Federated identity provider (IdP) icon at the top of a looping process that starts with requesting and receiving a server nonce value, followed by optionally requesting and receiving a preauthentication from the IdP. The next steps include requesting and receiving federation metadata from a federated IdP, performing WS-Trust authentication, receiving and validating the Security Assertion Markup Language (SAML) response, sending the SAML bearer login JOSE to the IdP, receiving the login response JWE, and decrypting and validating the login response and saving the tokens.](https://docs-assets.developer.apple.com/published/5c832d71d633649c7c7bcfbf874c63f9/media-4302341%402x.png)

##### Support Tls and System Ca Requirements

Because the login process can happen on any network, the system sends all HTTP requests using Transport Layer Security (TLS) and uses the current App Transport Security settings. The requests explicitly require that the system-provided root certificate authorities (CAs) include the issuer of the TLS certificate. The system doesn’t trust user-trusted or MDM-provided CAs for these requests. It limits these CAs to ensure the TLS tunnel to the identity provider doesn’t include any third-party products with security vulnerabilities or intentionally malicious code.

## Topics

### Pre-login
- [Obtaining a server nonce](obtaining-a-server-nonce.md)
  Request and process a server nonce to verify communication and detect replays.
- [Performing a preauthentication request](performing-a-preauthentication-request.md)
  Request and process a preauthentication for dynamic WS-Trust authentication.
- [Performing a WS-Trust metadata exchange data (MEX) request](performing-a-ws-trust-metadata-exchange-data-mex-request.md)
  Send and process a WS-Trust MEX request to determine the version and URLs for authentication.
### Login request
- [Performing a WS-Trust login request](performing-a-ws-trust-login-request.md)
  Create a WS-Trust login request using the metadata exchange data (MEX) response.
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
### Login response
- [Creating a JSON Web Encryption (JWE) login response](creating-a-json-web-encryption-jwe-login-response.md)
  Create an encrypted login response and configure the concatenation key derivation function (Concat KDF).
- [Processing the JSON Web Encryption (JWE) login response](processing-the-json-web-encryption-jwe-login-response.md)
  Validate the encrypted response.
- [Performing encryption verification](performing-encryption-verification.md)
  Verify the login request and create a JSON Web Encryption (JWE) response.

## See Also

- [class ASAuthorizationProviderExtensionKerberosMapping](asauthorizationproviderextensionkerberosmapping.md)
  A set of Kerberos mappings that the system login process uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/authentication-process)*