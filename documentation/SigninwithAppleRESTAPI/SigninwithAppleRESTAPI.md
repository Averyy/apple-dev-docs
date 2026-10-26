# Sign in with Apple REST API

**Framework**: SigninwithAppleRESTAPI  
**Kind**: module  
**Role**: Framework

Communicate between your app servers and Apple’s authentication servers.

## Mentions

- [Configuring your environment for Sign in with Apple](../SigninwithApple/configuring-your-environment-for-sign-in-with-apple.md)

#### Overview

The [Sign in with Apple](../SigninwithApple/SigninwithApple.md) REST API is a web service that connects you to Apple’s authentication servers. Use this service to generate and validate the identity tokens used to verify a user’s identity.

To sign in from a web app or other platform, like Android, use [Sign in with Apple JS](../SigninwithAppleJS/SigninwithAppleJS.md). Alternatively, to let users set up accounts and sign in to your native iOS, macOS, tvOS, and watchOS apps, use the [Authentication Services](../AuthenticationServices/AuthenticationServices.md) framework.

## Topics

### Authentication and verification of users
- [Authenticating users with Sign in with Apple](../SigninwithApple/authenticating-users-with-sign-in-with-apple.md)
  Securely authenticate users and create accounts for them in your app.
- [Receiving a User’s Identity Token](../SigninwithApple/receiving-a-users-identity-token.md)
  Retrieve the user’s information from Apple Account servers
- [Verifying a user](../SigninwithApple/verifying-a-user.md)
  Check the validity and integrity of a user’s identity token.
- [Processing changes for Sign in with Apple accounts](../SigninwithApple/processing-changes-for-sign-in-with-apple-accounts.md)
  Manage user-initiated modifications to maintain privacy with server-to-server notifications.
- [Request an authorization to the Sign in with Apple server](./request-an-authorization-to-the-sign-in-with-apple-server.md)
  Add a Sign in with Apple authorization flow to apps and web services that can’t directly access Sign in with Apple JS.
### Generating and revoking tokens
- [Creating a client secret](../AccountOrganizationalDataSharing/creating-a-client-secret.md)
  Generate a signed token to identify your client application.
- [Fetch Apple’s public key to verify token signatures](./fetch-apples-public-key-for-verifying-token-signature.md)
  Fetch Apple’s public key to verify ID token and server notification signatures.
- [Token validation](./generate-and-validate-tokens.md)
  Validate an authorization grant code delivered to your app to obtain tokens, or validate an existing refresh token.
- [Token revocation](./revoke-tokens.md)
  Invalidate the tokens and associated user authorizations for a user when they are no longer associated with your app.
### Common objects
- [object JWKSet](./jwkset.md)
  A set of JSON Web Key objects.
- [object TokenResponse](./tokenresponse.md)
  The response token object returned on a successful request.
- [object ErrorResponse](./errorresponse.md)
  The error object returned after an unsuccessful request.
### Sign in with Apple buttons
- [Get a Sign in with Apple button that is center-aligned.](./get-a-sign-in-with-apple-button-that-is-center-aligned.md)
  Generate a Sign in with Apple button with center-aligned text.
- [Get a Sign in with Apple button that is left-aligned.](./get-a-sign-in-with-apple-button-that-is-left-aligned.md)
  Generate a Sign in with Apple button with left-aligned text.
- [Get a Sign in with Apple button that contains just the Apple logo.](./get-a-sign-in-with-apple-button-that-contains-just-the-apple-logo.md)
  Generate a Sign in with Apple button image containing just the Apple logo.

## See Also

### Web support
- [Sign in with Apple JS](../SigninwithAppleJS/SigninwithAppleJS.md)
  Provide users a fast, secure way to sign in to your web service with their Apple Account.
- [Displaying Sign in with Apple buttons on the web](../SigninwithApple/displaying-sign-in-with-apple-buttons-on-the-web.md)
  Configure the appearance of Sign in with Apple buttons with CSS styles.
- [Configuring your environment for Sign in with Apple](../SigninwithApple/configuring-your-environment-for-sign-in-with-apple.md)
  Authenticate users with your web service by associating an existing app with a Services ID and private key.
- [Processing changes for Sign in with Apple accounts](../SigninwithApple/processing-changes-for-sign-in-with-apple-accounts.md)
  Manage user-initiated modifications to maintain privacy with server-to-server notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapplerestapi)*