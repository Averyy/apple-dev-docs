# Family Controls

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether the app can request or revoke authorization to provide parental controls.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+



**Type**: boolean

#### Discussion

You must add the Family Controls entitlement to your app before you call the [`AuthorizationCenter`](https://developer.apple.com/documentation/familycontrols/authorizationcenter) class’s [`requestAuthorization(completionHandler:)`](https://developer.apple.com/documentation/familycontrols/authorizationcenter/requestauthorization(completionhandler:)) or [`revokeAuthorization(completionHandler:)`](https://developer.apple.com/documentation/familycontrols/authorizationcenter/revokeauthorization(completionhandler:)) methods.

Adding the Family Controls capability to your app automatically sets this entitlement. Before submitting your app to the App Store, you must [`request permission`](https://developer.apple.comhttps://developer.apple.com/contact/request/family-controls-distribution) to use the entitlement. For more information, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/xcode/adding-capabilities-to-your-app).

## See Also

- [Family Controls App and Website Usage](entitlements/com.apple.developer.family-controls.app-and-website-usage.md)
  A Boolean value that indicates whether the app may, with the person’s permission, access app and website usage information from the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.family-controls)*