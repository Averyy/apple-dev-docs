# Receiving a User’s Identity Token

**Framework**: Sign in with Apple  
**Role**: Article

Retrieve the user’s information from Apple Account servers

#### Overview

After successfully authenticating the user, the server returns an identity JSON Web Token (JWT), single-use authorization grant code, the state contained in the authorization request, and user identifier to your app. For more information, see [`Request an authorization to the Sign in with Apple server`](../SigninwithAppleRESTAPI/request-an-authorization-to-the-sign-in-with-apple-server.md) and [`id_token`](../SigninwithAppleJS/authorizationi/id_token.md).

The information you retrieve must include the credentials required to verify the user’s identity. The server returns the credentials and user information based on the initial request. The information that returns can include user identity, full name, verified email address, and real user status.

> **Note**:  If the user signs in with a managed Apple Account, the value of the `email` claim is a real email address, not a proxy address. Alternatively, if the managed Apple Account is in Apple School Manager, the `email` claim may be empty. Students, for example, often don’t have an email that the school issues.

Use the authorization grant code to verify the token claims with Apple servers, and exchange them for refresh tokens. For more information, see [`Token validation`](../SigninwithAppleRESTAPI/generate-and-validate-tokens.md).

Use the user identifier instead of an email address to identify the user. The user identifier remains unique and static for your developer team.

If you request the user’s verified email address, Sign in with Apple prompts the user to share it with your app. The user may choose to share their real email address or an anonymous one that uses the private email relay service. In both cases, Apple verifies that the email address works and is ready for use.

If you request the user’s full name, Sign in with Apple collects the information to pass along to your app. The name defaults to the user’s name from their Apple Account, but the user can change their name when creating an account.

> ❗ **Important**:  Apple doesn’t receive the user’s full name shared with the system UI. The raw data is passed directly to your app from the browser and is not included in the user’s identity token. To help prevent cross-site scripting attacks, validate and sanitize the user-submitted first and last name values before storing on your app servers.

For more information, see [Communicating using the private email relay service](./communicating-using-the-private-email-relay-service.md).

## See Also

### Authentication and verification of users
- [Authenticating users with Sign in with Apple](./authenticating-users-with-sign-in-with-apple.md)
  Securely authenticate users and create accounts for them in your app.
- [Verifying a user](./verifying-a-user.md)
  Check the validity and integrity of a user’s identity token.
- [Processing changes for Sign in with Apple accounts](./processing-changes-for-sign-in-with-apple-accounts.md)
  Manage user-initiated modifications to maintain privacy with server-to-server notifications.
- [Request an authorization to the Sign in with Apple server](../SigninwithAppleRESTAPI/request-an-authorization-to-the-sign-in-with-apple-server.md)
  Add a Sign in with Apple authorization flow to apps and web services that can’t directly access Sign in with Apple JS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapple/receiving-a-users-identity-token)*