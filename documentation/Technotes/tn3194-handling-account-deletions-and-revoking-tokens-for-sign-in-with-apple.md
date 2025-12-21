# TN3194: Handling account deletions and revoking tokens for Sign in with Apple

**Framework**: Technotes

Learn the best techniques for managing Sign in with Apple user sessions and responding to account deletion requests.

#### Overview

Apps submitted to the App Store that support account creation must also let users initiate deletion of their account within the app, as of June 30, 2022. To learn more, see [`Offering account deletion in your app`](https://developer.apple.comhttps://developer.apple.com/support/offering-account-deletion-in-your-app/).

To properly support both account creation, verification, and deletion in your app, securely store user credentials—for example, identity tokens and refresh tokens— and consider using a server infrastructure to handle token generation, validation, and revocation.

#### Invalidate a User Session

The [`Token revocation`](https://developer.apple.com/documentation/SigninwithAppleRESTAPI/Revoke-tokens) endpoint (`/auth/revoke`) is the only way to programmatically invalidate user tokens associated to your developer account without user interaction. Apps using Sign in with Apple are expected to securely transmit and store tokens when integrated with a server infrastructure. This allows you to validate all user tokens received from Apple, as well as verify the user’s identity and Apple’s public key before granting access to your app or its data. Because this endpoint manages your user sessions, either a valid refresh token or access token for invalidation is required.

If you don’t have the user’s refresh token, access token, or authorization code, you must still fulfill the user’s account deletion request and meet the account deletion requirement. To manually revoke the user credentials, follow the steps below:

1. Delete the user’s account data from your systems.
2. Direct the user to [`manually revoke access`](https://developer.apple.comhttps://support.apple.com/en-us/102571) for your client.
3. Respond to the credential revoked notification to revert the client to an unauthenticated state

> ❗ **Important**: If the manual token revocation isn’t completed, the next time the user authenticates with your client using Sign in with Apple, they won’t be presented with the initial authorization flow to enter their full name, email address, or both. This is because the user credential state managed by Sign in with Apple remains unchanged and returns [`ASAuthorizationAppleIDProvider.CredentialState.authorized`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationAppleIDProvider/CredentialState/authorized), which may also result in the system auth UI displaying the “Continue with Apple” button type. For more information, about displaying the button, see [`Sign in with Apple Button`](https://developer.apple.comhttps://account.apple.com/signinwithapple/button).

#### Respond to Credential Revoked Notifications

Once the user’s credentials are revoked by Apple, your client will receive a notification signaling the revocation event:

- For apps using the [`Authentication Services`](https://developer.apple.com/documentation/AuthenticationServices) framework to implement Sign in with Apple, observe the [`credentialRevokedNotification`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationAppleIDProvider/credentialRevokedNotification) and use [`getCredentialState(forUserID:completion:)`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationAppleIDProvider/getCredentialState(forUserID:completion:)) on the [`ASAuthorizationAppleIDProvider`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationAppleIDProvider) object to respond to credential revocation and account deletion events.
- For web services, if an endpoint is registered for [`Processing changes for Sign in with Apple accounts`](https://developer.apple.com/documentation/signinwithapple/processing-changes-for-sign-in-with-apple-accounts), Apple broadcasts a notification to the specified endpoint with the `consent-revoked` event type.

When receiving either notification, ensure you’ve completed the following operations to meet the requirements of account deletion:

1. Delete all user-related account data, including: - The token used for token revocation;
- Any user-related data stored in your app servers; and
- Any user-related data store in the Keychain or securely on disk in the native app or locally on a web client.
2. Revert the client to an unauthenticated state.

#### Securely Store User Tokens for Account Creations

For all new user account creations, properly store and handle the user credentials by following the authorization flow below:

1. Securely transmit the identity token and authorization code to your app server.
2. Verify the identity token and validate the authorization code using the `/auth/token` endpoint.
3. Once the authorization code is validated, securely store the token response — including the identity token, refresh token, and access token.
4. Validate the refresh token up to once per day with Apple servers (to manage the lifetime of your user session and for future token revocation requests), and obtain access tokens (for future token revocation, app transfer, or user migration requests).

If you have questions about implementing these flows, including client authorization, token validation, or token revocation, please see the following resources:

- [`Verifying a user`](https://developer.apple.com/documentation/signinwithapple/verifying-a-user)
- [`Creating a client secret`](https://developer.apple.com/documentation/AccountOrganizationalDataSharing/creating-a-client-secret)
- [`Token validation`](https://developer.apple.com/documentation/SigninwithAppleRESTAPI/Generate-and-validate-tokens)
- [`TN3107: Resolving Sign in with Apple response errors`](tn3107-resolving-sign-in-with-apple-response-errors.md)
- [`TN3159: Migrating Sign in with Apple users for an app transfer`](tn3159-migrating-sign-in-with-apple-users-for-an-app-transfer.md)

#### Revision History

-  First published.

## See Also

- [TN3190: USB audio device design considerations](tn3190-usb-audio-device-design-considerations.md)
  Learn the best techniques for designing devices that conform to the USB Audio Device Class specifications.
- [TN3193: Managing the on-device foundation model’s context window](tn3193-managing-the-on-device-foundation-model-s-context-window.md)
  Learn how to budget for the context window limit of Apple’s on-device foundation model and handle the error when reaching the limit.
- [TN3115: Bluetooth State Restoration app relaunch rules](tn3115-bluetooth-state-restoration-app-relaunch-rules.md)
  Learn about the conditions under which an iOS app will be relaunched by Bluetooth State Restoration.
- [TN3192: Migrating your iPad app from the deprecated UIRequiresFullScreen key](tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md)
  Support iPad multitasking and dynamic resizing while updating your app to remove the deprecated full-screen compatibility mode.
- [TN3151: Choosing the right networking API](tn3151-choosing-the-right-networking-api.md)
  Learn which networking API is best for you.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3191: IMAP extensions supported by Mail for iOS, iPadOS, and visionOS](tn3191-imap-extensions-supported-by-mail.md)
  Learn which extensions to the RFC 3501 IMAP protocol are supported by Mail for iOS, iPadOS, and visionOS.
- [TN3134: Network Extension provider deployment](tn3134-network-extension-provider-deployment.md)
  Explore the platforms, packaging, OS versions, and device configurations for Network Extension provider deployment.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple)*