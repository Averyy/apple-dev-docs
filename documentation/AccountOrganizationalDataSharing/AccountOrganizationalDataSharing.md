# Account & Organizational Data Sharing

**Framework**: Account & Organizational Data Sharing  
**Kind**: module

Provide people with the ability to authorize your apps and websites that access information about them on Apple REST services, like Roster API.

**Availability**:
- AccountOrganizationalDataSharing 1.0+

#### Overview

With [`OAuth 2.0`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc6749), Account & Organizational Data Sharing gives your users a safe way to authorize your apps and websites to access information about them on Apple services, for example [`Roster API`](https://developer.apple.com/documentation/RosterAPI).

## Topics

### Generating tokens
- [Creating a client secret](creating-a-client-secret.md)
  Generate a signed token to identify your client application.
- [Fetch Apple's public key for verifying token signature](fetch-apple's-public-key-for-verifying-token-signature.md)
  Retrieve the public key associated with the cryptographic identity Apple uses to sign the token.
- [Generate and validate tokens](generate-and-validate-tokens.md)
  Validate an authorization grant code delivered to your app to obtain tokens, or validate an existing refresh token.
### Using and revoking tokens
- [Request an authorization](request-an-authorization.md)
  Request a user authorization to Account & Organizational Data Sharing apps and web services.
- [Revoke tokens](revoke-tokens.md)
  Invalidate the tokens and associated user authorizations for someone when they are no longer associated with your app.
### Common objects
- [object JWKSet](jwkset.md)
  A set of JSON web keys.
- [object TokenResponse](tokenresponse.md)
  The response token object returned on a successful request.
- [object ErrorResponse](errorresponse.md)
  The error object returned after an unsuccessful request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AccountOrganizationalDataSharing)*