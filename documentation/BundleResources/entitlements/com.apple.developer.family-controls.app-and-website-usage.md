# Family Controls App and Website Usage

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether the app may, with the person’s permission, access app and website usage information from the current device.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Details

- **Name**: `com.apple.developer.family-controls.app-and-website-usage` (Family Controls App & Website Usage)
- **Type**: boolean

## Discussion

You must add this entitlement to your app before you access app and website usage information through the [Family Controls](../../FamilyControls/FamilyControls.md) and [Device Activity](../../DeviceActivity/DeviceActivity.md) frameworks. This includes obtaining the [`AuthorizationStatus.approvedWithDataAccess`](../../FamilyControls/authorizationstatus/approvedwithdataaccess.md) authorization status, which lets your app use [`FamilyActivityData`](../../FamilyControls/familyactivitydata.md) to retrieve the actual bundle identifiers of installed applications, domain names of visited websites, and display names of activity categories. Your app requires explicit authorization from the person before it can access any of this data.

Add this entitlement to your app by enabling the Family Controls App And Website Usage on your target in Xcode. For more information, see [Adding capabilities to your app](../../Xcode/adding-capabilities-to-your-app.md).

## See Also

### Family controls
- [Family Controls](./com.apple.developer.family-controls.md)
  A Boolean value that indicates whether the app can request or revoke authorization to provide parental controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.family-controls.app-and-website-usage)*