# Verifying a user

**Framework**: Sign in with Apple  
**Role**: Article

Check the validity and integrity of a user’s identity token.

#### Overview

After your app receives a user’s information, you can verify their associated identity token with the server to confirm that the token isn’t expired and ensure it hasn’t been tampered with or replayed to your app. For information about retrieving the identity token, see [Authenticating users with Sign in with Apple](./authenticating-users-with-sign-in-with-apple.md).

![A sequence diagram that describes the flow for verifying a user’s identity.](https://developer.apple.com/tutorials/images/com.apple.signinwithapple/media-3384756@2x.png)

##### Verify the identity token

Start by securely transmitting the identity token and authorization code to your app server. For more about the information required to verify a user’s identity, see [Authenticating users with Sign in with Apple](./authenticating-users-with-sign-in-with-apple.md).

> **Note**:  To obtain the identity token from their server, web apps must validate the authorization code using the [`Token validation`](../SigninwithAppleRESTAPI/generate-and-validate-tokens.md) endpoint.

To verify the identity token, your app server must:

- Verify the JWS E256 signature using the server’s public key
- Verify the `nonce` for the authentication
- Verify that the `iss` field contains `https://appleid.apple.com`
- Verify that the `aud` field is the developer’s `client_id`
- Verify that the time is earlier than the `exp` value of the token

For more information, see [`id_token`](../SigninwithAppleJS/authorizationi/id_token.md).

##### Obtain a refresh token

After verifying the identity token on your server, call the [`Token validation`](../SigninwithAppleRESTAPI/generate-and-validate-tokens.md) endpoint with the `client_id`, `client_secret`, and `nonce` information.

On success, the server issues a refresh token, which you use to obtain access tokens with future calls. You may verify the refresh token up to once a day to confirm that the user’s Apple Account on that device is still in good standing with Apple’s servers. Apple’s servers may throttle your call if you attempt to verify a user’s Apple Account more than once a day.

You may continue to use the same refresh token until it’s invalidated — for example, by an Apple Account account password change, or when a user revokes access to your app — or the token verification fails. If any step of the token verification fails, direct your app to fetch a new identity token for the user. Obtaining a new identity token on the device requires user interaction.

##### Manage the user session

After verifying the identity token, your app is responsible for managing the user session. You may tie the session’s lifetime to successful [`getCredentialState(forUserID:completion:)`](../AuthenticationServices/asauthorizationappleidprovider/getcredentialstate%28foruserid,completion%29.md) calls on Apple devices. This is a local, inexpensive, nonnetwork call enabled by the Apple Account system that keeps the Apple Account state on a device in sync with Apple servers.

User interaction is required any time a new identity token is requested. User sessions are long-lived on device, so calling for a new identity token on every launch, or more frequently than once a day, can result in your request failing due to throttling.

If the user’s Apple Account changes in the system, calls to `getCredentialState(forUserID:completion:)` indicate that the user changed. Assume that a different user has signed in and log out the app’s currently known user.

For apps running on other systems, use the periodic successful verification of the refresh token to determine the lifetime of the user session.

## See Also

### Authentication and verification of users
- [Authenticating users with Sign in with Apple](./authenticating-users-with-sign-in-with-apple.md)
  Securely authenticate users and create accounts for them in your app.
- [Receiving a User’s Identity Token](./receiving-a-users-identity-token.md)
  Retrieve the user’s information from Apple Account servers
- [Processing changes for Sign in with Apple accounts](./processing-changes-for-sign-in-with-apple-accounts.md)
  Manage user-initiated modifications to maintain privacy with server-to-server notifications.
- [Request an authorization to the Sign in with Apple server](../SigninwithAppleRESTAPI/request-an-authorization-to-the-sign-in-with-apple-server.md)
  Add a Sign in with Apple authorization flow to apps and web services that can’t directly access Sign in with Apple JS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapple/verifying-a-user)*