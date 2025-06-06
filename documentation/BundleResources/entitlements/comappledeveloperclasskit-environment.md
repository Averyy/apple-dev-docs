# ClassKit Environment Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

The ClassKit development or production environment for an education app that works with the Schoolwork app.

**Availability**:
- iOS 11.4+
- iPadOS 11.4+
- macOS 11.0+
- visionOS 1.0+

#### Discussion

This key specifies the ClassKit environment your app uses to share data with Apple’s Schoolwork app.

To support testing locally, Xcode sets the value to `development` by default. When you upload your app to the App Store, Xcode changes the value to `production`.

To add this entitlement to your app, enable the ClassKit capability in Xcode.

## See Also

- [Enabling ClassKit in your app](../ClassKit/enabling-classkit-in-your-app.md)
  Prepare your app and your development environment to adopt ClassKit.
- [Testing your ClassKit app during development](../ClassKit/testing-your-classkit-app-during-development.md)
  Use development mode to test your app without a Managed Apple ID.
- [com.apple.developer.automatic-assessment-configuration](entitlements/com.apple.developer.automatic-assessment-configuration.md)
  A Boolean value that indicates whether an app may create an assessment session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.classkit-environment)*