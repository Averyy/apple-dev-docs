# Authenticating users with Sign in with Apple

**Framework**: Sign in with Apple  
**Role**: Article

Securely authenticate users and create accounts for them in your app.

#### Overview

Sign in with Apple lets users log in to your app across all of your platforms using their two-factor authentication Apple Account. After the user chooses to use Sign in with Apple to log in, your app receives tokens and user information that you can verify from a server.

When the user attempts to sign in using Sign in with Apple, the sequence in the following diagram begins:

![A sequence diagram that describes the steps for authenticating a user. The app creates a scoped sign-in request to the API. The API requests user information, then verifies the user and obtains the token from an Apple Account server. The server provides the user’s name and, if requested, the email address to the app.](https://developer.apple.com/tutorials/images/com.apple.signinwithapple/media-3635395@2x.png)

You may group apps in your developer account for Sign in with Apple so an app only requests information the first time the user logs in. A simple confirmation to continue appears even if the app bundle IDs are different across systems, such as iOS, macOS, and the web.

##### Authenticate the user and request information

Initialize an authentication session with your app server and associate a client session with an ID token using the `nonce` value. You can request to receive the user’s information, such as name and email address. If the user approves accessing this information, your authorization request includes the requested information.

Sign in with Apple protects user accounts by using two-factor authentication. Users that log in to an Apple device can quickly sign in to your app in the following ways:

- With Face ID or Touch ID on passcode-protected devices
- With a passcode, if Touch ID or Face ID isn’t available
- With an Apple Account password, if the passcode isn’t set

Native apps only allow the signed-in iCloud user to use Sign in with Apple. Web-based interactions allow logins using any Apple Account.

> **Note**:  On non-Apple devices, users must log in with their Apple Account, password, and two-factor authentication code.

Apple determines whether a user is a real person by combining on-device machine learning, account history, and hardware attestation using privacy-preserving mechanisms. There are three possible values when determining whether a user is a real person:

- **`2` (or `LikelyReal`)**: The user appears to be a real person, and you can treat this account as a valid user. You can skip any additional fraud verification checks or CAPTCHAs that your app normally uses. For more information, see [`ASUserDetectionStatus.likelyReal`](../AuthenticationServices/asuserdetectionstatus/likelyreal.md).
- **`1` (or `Unknown`)**: The system can’t determine whether the user is a real person. The server may return this value if status determination takes too long. Treat this user as any other account with limited information that requires additional verification steps. Don’t block service, because the user may be a real person. For more information, see [`ASUserDetectionStatus.unknown`](../AuthenticationServices/asuserdetectionstatus/unknown.md).
- **`0` (or `Unsupported`)**: Real user status is only available in iOS 14 and later, macOS 11 and later, watchOS 7 and later, and tvOS 14 and later. Previous versions of iOS, macOS, watchOS, tvOS return `Unsupported`. For more information, see [`ASUserDetectionStatus.unsupported`](../AuthenticationServices/asuserdetectionstatus/unsupported.md).

This system for detecting whether the user is real is tuned for high-precision and moderate recall time. You may also use it as a feature in your own machine-learning models for detecting account fraud.

When someone uses your app and Sign in with Apple for the first time, the identification servers return the user status. Subsequent attempts don’t return the user status.

After the user logs in to your app using Sign in with Apple on one of their devices, they can sign in on all of their devices. Deleting your app from a device doesn’t affect this capability. If the user reinstalls your app, they can continue to use Sign in with Apple on any of their devices to sign in with their existing account.

##### Send information to app servers and verify tokens

After successfully authenticating the user, the server returns an identity JSON Web Token (JWT), single-use authorization grant code, the state contained in the authorization request, and user identifier to your app. Use the authorization grant code to verify the token claims with Apple servers, and exchange them for refresh tokens. For more information, see [Receiving a User’s Identity Token](./receiving-a-users-identity-token.md).

Ensure that your app relays the credentials and user information to your app servers. The API collects this information and shares it with your app the first time the user logs in using Sign in with Apple. If the user then uses Sign in with Apple on another device, the API doesn’t ask for the user’s name or email again. It collects the information again only if the user stops using Sign in with Apple and later reconnects to your app.

Although Apple provides the user’s email address in the identity token on all subsequent API responses, it doesn’t include other information about the user, such as their name. When you receive user information from the API response, immediately store it locally so your app can access it again in the event of a process or network failure.

Your app servers verify the validity of the token credentials with Apple Account servers. For more information, see [Verifying a user](./verifying-a-user.md).

##### Prevent duplicate accounts

A user may already have an account in your system, but may attempt to use Sign in with Apple to log in to that account. Sharing the real email address that’s associated with the user’s Apple Account may not help because it may not be the same email the user uses to create the account with your system. There are a couple of ways you can mitigate this issue:

- Implement the [`ASAuthorizationPasswordProvider`](../AuthenticationServices/asauthorizationpasswordprovider.md) class to detect and offer keychain credentials that the system already knows about. This works seamlessly to detect and use existing accounts, and prevents creating new accounts using Sign in with Apple.
- For new accounts that use Sign in with Apple, let the user know that they’re creating a new account, and ask if they have any existing accounts to link to.

## See Also

### Authentication and verification of users
- [Receiving a User’s Identity Token](./receiving-a-users-identity-token.md)
  Retrieve the user’s information from Apple Account servers
- [Verifying a user](./verifying-a-user.md)
  Check the validity and integrity of a user’s identity token.
- [Processing changes for Sign in with Apple accounts](./processing-changes-for-sign-in-with-apple-accounts.md)
  Manage user-initiated modifications to maintain privacy with server-to-server notifications.
- [Request an authorization to the Sign in with Apple server](https://developer.apple.com/documentation/signinwithapplerestapi/request-an-authorization-to-the-sign-in-with-apple-server.)
  Add a Sign in with Apple authorization flow to apps and web services that can’t directly access Sign in with Apple JS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapple/authenticating-users-with-sign-in-with-apple)*