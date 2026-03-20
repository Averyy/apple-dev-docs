# Family Controls App and Website Usage

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether the app may, with the person’s permission, access app and website usage information from the current device.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+



**Type**: boolean

#### Discussion

You must add this entitlement to your app before you access app and website usage information through the [`Family Controls`](https://developer.apple.com/documentation/FamilyControls) and [`Device Activity`](https://developer.apple.com/documentation/DeviceActivity) frameworks. This includes obtaining the [`AuthorizationStatus.approvedWithDataAccess`](https://developer.apple.com/documentation/FamilyControls/AuthorizationStatus/approvedWithDataAccess) authorization status, which lets your app use [`FamilyActivityData`](https://developer.apple.com/documentation/FamilyControls/FamilyActivityData) to retrieve the actual bundle identifiers of installed applications, domain names of visited websites, and display names of activity categories. Your app requires explicit authorization from the person before it can access any of this data.

Add this entitlement to your app by enabling the Family Controls App And Website Usage on your target in Xcode. For more information, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).

## See Also

- [Family Controls](entitlements/com.apple.developer.family-controls.md)
  A Boolean value that indicates whether the app can request or revoke authorization to provide parental controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.family-controls.app-and-website-usage)*