# Sign in with Apple Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

An entitlement that lets your app use Sign in with Apple.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Details

- **Name**: `com.apple.developer.applesignin` (Sign in with Apple)
- **Type**: array of string 

## Possible Values

- `Default`: The value used for normal operation.

## Discussion

To add this entitlement to your app with the correct associated value, enable the Sign in with Apple capability in Xcode. For information about letting users log into your apps and services with their Apple ID, see [`ASAuthorizationAppleIDProvider`](../../AuthenticationServices/asauthorizationappleidprovider.md).

## See Also

### Authentication
- [Account Creation Requires Phone Number](./com.apple.developer.authentication-services.account-creation-requires-phone-number.md)
  A Boolean value that indicates whether an app requires someone to provide a phone number to create an account.
- [AutoFill Credential Provider Entitlement](./com.apple.developer.authentication-services.autofill-credential-provider.md)
  A Boolean value that indicates whether the app may, with user permission, provide user names and passwords for AutoFill in Safari and other apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.applesignin)*