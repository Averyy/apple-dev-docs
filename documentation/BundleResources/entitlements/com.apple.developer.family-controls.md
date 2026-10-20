# Family Controls

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether the app can request or revoke authorization to provide parental controls.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Details

- **Name**: `com.apple.developer.family-controls`
- **Type**: boolean

#### Discussion

You must add the Family Controls entitlement to your app before you call the [`AuthorizationCenter`](../../FamilyControls/authorizationcenter.md) class’s [`requestAuthorization(completionHandler:)`](../../FamilyControls/authorizationcenter/requestauthorization%28completionhandler%29.md) or [`revokeAuthorization(completionHandler:)`](../../FamilyControls/authorizationcenter/revokeauthorization%28completionhandler%29.md) methods.

Adding the Family Controls capability to your app automatically sets this entitlement. Before submitting your app to the App Store, you must [request permission](https://developer.apple.com/contact/request/family-controls-distribution) to use the entitlement. For more information, see [Adding capabilities to your app](../../Xcode/adding-capabilities-to-your-app.md).

## See Also

### Family controls
- [Family Controls App and Website Usage](./com.apple.developer.family-controls.app-and-website-usage.md)
  A Boolean value that indicates whether the app may, with the person’s permission, access app and website usage information from the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.family-controls)*