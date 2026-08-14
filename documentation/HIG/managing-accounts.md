---
url: https://developer.apple.com/design/human-interface-guidelines/managing-accounts
framework: HIG
---

# Managing accounts

**Type:** article

**Platforms:** ios, ipados, macos, tvos, visionos, watchos

When it doesn’t create an unnecessary barrier to your experience, an account can be a convenient way for people to access their content and track personal details.

![A sketch of a person, suggesting personal information. The image is overlaid with rectangular and circular grid lines and is tinted orange to subtly reflect the orange in the original six-color Apple logo.](/images/com.apple.HIG/patterns-managing-accounts-intro~dark@2x.png)
Ask people to create an account only if your core functionality requires it; otherwise, let people enjoy your app or game without one. If you require an account, consider using [Sign in with Apple](sign-in-with-apple.md) to give people a consistent sign-in experience they can trust and the convenience of not having to remember multiple accounts and authentication methods.

## Best practices
**Explain the benefits of creating an account and how to sign up.** If your app or game requires an account, write a brief, friendly description of the reasons for the requirement and its benefits. Display this message in your sign-in view.
**Delay sign-in for as long as possible.** People often abandon apps when they’re forced to sign in before they can do anything useful. To help avoid this situation, give people a chance to get a sense of what your app or game does before asking them to make a commitment to it. For example, a shopping app might let people browse as much as they want, requiring sign-in only when they’re ready to make a purchase.
**If you don’t use Sign in with Apple in your iOS, iPadOS, macOS, or visionOS app, prefer using a passkey.** Passkeys simplify account creation and authentication, eliminating the need for people to create or enter passwords. When an app supports passkeys, people simply provide their user name when creating a new account or signing in to an existing one. For developer guidance, see [Supporting passkeys](../authenticationservices/supporting-passkeys.md). If you need to continue using passwords for authentication, augment security by requiring two-factor authentication (for developer guidance, see [Securing Logins with iCloud Keychain Verification Codes](../authenticationservices/securing-logins-with-icloud-keychain-verification-codes.md)).
**Always identify the authentication method you offer.** For example, if you display a button for signing in to your app with Face ID, title it using a phrase like “Sign In with Face ID” instead of a generic phrase like “Sign In.”
**Refer only to authentication methods that are available in the current context.** For example, don’t reference Face ID on a device that doesn’t offer it. Check the device’s capabilities and use the appropriate terminology. For developer guidance, see [LABiometryType](../localauthentication/labiometrytype.md).
**In general, avoid offering an app-specific setting for opting in to biometric authentication.** People turn on biometric authentication at the system level, so presenting an in-app setting is redundant and could be confusing.
**Avoid using the term *passcode* to refer to account authentication.** People create a passcode to unlock their device or authenticate for Apple services. If you use the term in your interface, people might think you’re asking them to reuse their passcode in your app or game.

## Deleting accounts
If you help people create an account within your app or game, you must also help them delete it, not just deactivate it. In addition to following the guidelines below, be sure to understand and comply with your region’s legal requirements related to account deletion and the right to be forgotten.

> **Important:** If legal requirements compel your app to maintain accounts or information — such as digital health records — or to follow a specific account-deletion process, clearly describe the situation so people can understand the information or accounts you must maintain and the process you must follow.
**Provide a clear way to initiate account deletion within your app or game.** If people can’t perform account deletion within your app, you must provide a direct link to the webpage on which people can do so. Make the link easy to discover — for example, don’t bury it in your Privacy Policy or Terms of Service pages.

> **Note:** If people used [Sign in with Apple](sign-in-with-apple.md) to create an account within your app, you revoke the associated tokens when they delete their account. See [Token revocation](../signinwithapplerestapi/revoke-tokens.md).
**Provide a consistent account-deletion experience whether people perform it within your app or game or on the website.** For example, avoid making one version of the deletion flow longer or more complicated than the other.
**Consider letting people schedule account deletion to occur in the future.** People can appreciate the opportunity to use their remaining services or wait until their subscription auto-renews before deleting their account. If you offer a way to schedule account deletion, offer an option for immediate deletion as well.
**Tell people when account deletion will complete, and notify them when it’s finished.** Because it can sometimes take a while to fully delete an account, it’s essential to keep people informed about the status of the deletion process so they know what to expect.
**If you support in-app purchases, help people understand how billing and cancellation work when they delete their account.** For example, you might need to help people understand the following scenarios:
- Billing for an auto-renewable subscription continues through Apple until people cancel the subscription, regardless of whether they delete their account.
- After they delete their account, people need to cancel their subscription or request a refund.
In addition to helping people understand these scenarios, provide information that describes how to cancel subscriptions and manage purchases. For guidance, see [Helping people manage their subscriptions](in-app-purchase.md#Helping-people-manage-their-subscriptions) and [Providing help with in-app purchases](in-app-purchase.md#Providing-help-with-in-app-purchases).

> **Note:** Even if people didn’t use your app to purchase the subscription, you still need to support account deletion.

## TV provider accounts
Many popular TV providers let people sign in to their accounts at the system level, eliminating the need to authenticate on an app-by-app basis. If your TV provider app requires people to sign in, use TV Provider Authentication to provide the most efficient onboarding experience.
**Avoid displaying a sign-out option when people are signed in at the system level.** If your app must include a sign-out option, invoking it needs to prompt people to navigate to Settings > TV Provider to sign out of their account.
**Never instruct people to sign out by adjusting privacy controls.** The TV provider controls in Settings > Privacy aren’t a sign-out mechanism. These settings help people manage the apps that can access their TV provider account.

## Platform considerations
*No additional considerations for iOS, iPadOS, macOS, or visionOS.*

### tvOS
Most people interact with Apple TV using a remote, not a keyboard, so ask for the minimum amount of information necessary.
**Prefer letting people use another device to sign up or authenticate.** When you configure your app’s associated domains, Apple TV can work with other devices to safely suggest sign-in credentials, including [Sign in with Apple](sign-in-with-apple.md). For developer guidance, see [Configuring an associated domain](../xcode/configuring-an-associated-domain.md).
**When people are signed in to a shared account, avoid asking them to choose their profile every time they become the current user.** In tvOS 16 and later, your app can share its credentials with all users while storing each individual’s profile and user data separately. When you support this type of sharing, your app can automatically use the current user’s profile without asking each person to sign in separately to a shared account. For developer guidance, see [kSecUseUserIndependentKeychain](../security/ksecuseuserindependentkeychain.md) and [User Management Entitlement](../bundleresources/entitlements/com.apple.developer.user-management.md).
**Minimize data entry.** If you need to gather more than a small amount of information, ask people to visit a website from another device. If you need an email address, show the email keyboard screen, which includes a list of recently entered addresses.

### watchOS
Use iCloud synchronization to provide access to the Keychain, letting people autofill user names and passwords and preserve app settings.

## Resources

#### Related
[Onboarding](onboarding.md)
[Sign in with Apple](sign-in-with-apple.md)

#### Developer documentation
[Supporting passkeys](../authenticationservices/supporting-passkeys.md) — Authentication Services

#### Videos
- [What’s new in passkeys](https://developer.apple.com/videos/play/wwdc2025/279) - Discover how iOS, iPadOS, macOS, and visionOS 26 enhance passkeys. We’ll explore key updates including: the new account creation API for streamlined sign-up, keeping passkeys up-to-date, new ways to drive passkey upgrades through automatic passkey upgrades and passkey management endpoints, and the secure import/export of passkeys. Learn how these improvements enhance user experience and security, and how to implement these updates in your apps to provide a smoother, more secure authentication experience. To get the most out of this video, first watch “Meet passkeys” from WWDC22.
- [What’s new in device management](https://developer.apple.com/videos/play/wwdc2024/10143) - Learn about the latest management capabilities for iOS, iPadOS, macOS, and visionOS, then discover the latest changes to Apple Business Manager and Apple School Manager. We’ll also share updates to Activation Lock, SoftwareUpdate, and Safari management.



---
*Source: [https://developer.apple.com/design/human-interface-guidelines/managing-accounts](https://developer.apple.com/design/human-interface-guidelines/managing-accounts)*
