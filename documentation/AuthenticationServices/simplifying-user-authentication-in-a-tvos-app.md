# Simplifying User Authentication in a tvOS App

**Framework**: Authenticationservices

Build a fluid sign-in experience for your tvOS apps using AuthenticationServices.

**Availability**:
- tvOS 15.0+
- Xcode 13.0+

#### Overview

> **Note**: This sample code project is associated with WWDC21 session [`10279: Simplify sign in for your tvOS apps`](https://developer.apple.comhttps://developer.apple.com/wwdc21/10279/).

##### Configure the Sample Code Project

To configure the sample code project, perform the following steps in Xcode:

1. Add your Apple ID account and assign the target to a team so Xcode can enable the `Associated Domains` capability with your provisioning profile.
2. Configure your [`Supporting associated domains`](https://developer.apple.com/documentation/Xcode/supporting-associated-domains) in the `Associated Domains` capability and your website’s associated domains file.
3. Set up an Apple TV running tvOS 15 and an iPhone or iPad running iOS 15 or iPadOS 15.
4. Add the same Apple ID to both devices. Alternatively, you may [`pair`](https://developer.apple.comhttps://support.apple.com/en-us/HT208088) the iPhone or iPad with the Apple TV.
5. Set the Apple TV as the run destination in the scheme pop-up menu.
6. In the toolbar, click Run, or choose Product > Run.

## See Also

- [Implementing User Authentication with Sign in with Apple](implementing-user-authentication-with-sign-in-with-apple.md)
  Provide a way for users of your app to set up an account and start using your services.
- [struct SignInWithAppleButton](signinwithapplebutton.md)
  The view that creates the Sign in with Apple button for display.
- [Sign in with Apple Entitlement](../BundleResources/Entitlements/com.apple.developer.applesignin.md)
  An entitlement that lets your app use Sign in with Apple.
- [class ASAuthorizationAppleIDProvider](asauthorizationappleidprovider.md)
  A mechanism for generating requests to authenticate users based on their Apple ID.
- [class ASAuthorizationAppleIDCredential](asauthorizationappleidcredential.md)
  A credential that results from a successful Apple ID authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AuthenticationServices/simplifying-user-authentication-in-a-tvos-app)*