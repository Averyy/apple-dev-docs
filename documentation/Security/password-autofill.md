# Password AutoFill

**Framework**: Security

Streamline your app’s login and onboarding procedures.

#### Overview

Password AutoFill simplifies login and account creation tasks for iOS apps and webpages. With just a few taps, your users can create and save new passwords or log in to an existing account. Users don’t even need to know their password; the system handles everything. This convenience increases the likelihood that users will complete your app’s onboarding process and start using your app more quickly. Additionally, by encouraging users to select unique, strong passwords, you increase the security of your app.

By default, Password AutoFill saves the user’s login credentials on their current iOS device. iOS can sync these credentials securely across the user’s devices using iCloud Keychain. Password AutoFill recommends credentials only for your app’s associated domain, and the user must authenticate using Face ID or Touch ID before accessing these credentials. For more information on privacy and security, see [`Approach to Privacy`](https://developer.apple.comhttps://www.apple.com/privacy/approach-to-privacy/) and [`iOS Security Guide`](https://developer.apple.comhttps://images.apple.com/business/docs/iOS_Security_Guide.pdf).

Password AutoFill also provides credentials from third-party password managers that implement a credential provider extension. For more information on the credential provider extension, see the [`Authentication Services`](https://developer.apple.com/documentation/AuthenticationServices) framework.

##### Enable Password Autofill

Password AutoFill uses heuristics to determine when the user logs in or creates new passwords, and automatically provides the password QuickType bar. These heuristics give users some Password AutoFill support in most apps, even if those apps haven’t been updated to support AutoFill. However, to provide the best user experience and ensure your app fully supports Password AutoFill, perform the following steps:

1. Set up your app’s associated domains. To learn how to set up your app’s associated domains, see [`Supporting associated domains`](https://developer.apple.com/documentation/Xcode/supporting-associated-domains).
2. Set the correct AutoFill type on relevant text fields. For an iOS app, see [`Enabling Password AutoFill on a text input view`](enabling-password-autofill-on-a-text-input-view.md). For a web app, see [`Enabling Password AutoFill on an HTML input element`](enabling-password-autofill-on-an-html-input-element.md).

##### Support Third Party Web Services

Password AutoFill streamlines logging into web services at your domain; however, if you need to log into a third-party service, use [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession) instead, which supports Password AutoFill when your user hasn’t already logged in.

##### Integrate a Password Management App with Password Autofill

If you’re developing a password management app, create AutoFill Credential Provider Extensions to surface credentials from your app in Password AutoFill and pull your app’s password data into the Password AutoFill workflow. When your app integrates with Password AutoFill, users don’t have to copy and paste credentials. Instead, they can use password data stored in your app easily because the data will be offered to the user to fill in compatible user name and password fields. To integrate a password app with Password AutoFill, use in the [`Authentication Services`](https://developer.apple.com/documentation/AuthenticationServices) framework.

## Topics

### Essentials
- [About the Password AutoFill workflow](about-the-password-autofill-workflow.md)
  Learn how Password AutoFill interacts with both iOS and web apps.
- [Supporting associated domains](../Xcode/supporting-associated-domains.md)
  Connect your app and a website to provide both a native app and a browser experience.
- [object applinks](../BundleResources/applinks.md)
  The root object for a universal links service definition.
### Text input views
- [Enabling Password AutoFill on a text input view](enabling-password-autofill-on-a-text-input-view.md)
  Make sure a text input view displays the correct AutoFill suggestions.
- [var textContentType: UITextContentType!](../UIKit/UITextInputTraits/textContentType.md)
  The semantic meaning for a text input area.
- [static let username: UITextContentType](../UIKit/UITextContentType/username.md)
  A property that defines the content in a text input area as an account or login name.
- [static let password: UITextContentType](../UIKit/UITextContentType/password.md)
  A property that defines the content in a text input area as a password.
- [static let newPassword: UITextContentType](../UIKit/UITextContentType/newPassword.md)
  A property that defines the content in a text input area as a new password.
- [static let oneTimeCode: UITextContentType](../UIKit/UITextContentType/oneTimeCode.md)
  A property that defines the content in a text input area as a one-time code.
### Text input elements
- [Enabling Password AutoFill on an HTML input element](enabling-password-autofill-on-an-html-input-element.md)
  Make sure a web view or webpage provides the correct AutoFill suggestions.
### Password rules
- [Customizing Password AutoFill rules](customizing-password-autofill-rules.md)
  Modify the strong password rules for your app by adding your own restrictions.
- [var passwordRules: UITextInputPasswordRules?](../UIKit/UITextInputTraits/passwordRules.md)
- [class UITextInputPasswordRules](../UIKit/UITextInputPasswordRules.md)
  A class that represents password rules for a text input field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/password-autofill)*