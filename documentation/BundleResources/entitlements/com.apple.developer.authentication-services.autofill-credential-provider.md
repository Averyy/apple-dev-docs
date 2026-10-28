# AutoFill Credential Provider Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether the app may, with user permission, provide user names and passwords for AutoFill in Safari and other apps.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- macOS 11.0+
- visionOS 1.0+

## Details

- **Name**: `com.apple.developer.authentication-services.autofill-credential-provider` (AutoFill Credential Provider)
- **Type**: boolean

## Discussion

To add this entitlement to a target, enable the AutoFill Credential Provider capability in Xcode. Do this for both your Password AutoFill extension and its host app.

## See Also

### Authentication
- [Account Creation Requires Phone Number](./com.apple.developer.authentication-services.account-creation-requires-phone-number.md)
  A Boolean value that indicates whether an app requires someone to provide a phone number to create an account.
- [Sign in with Apple Entitlement](./com.apple.developer.applesignin.md)
  An entitlement that lets your app use Sign in with Apple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.authentication-services.autofill-credential-provider)*