# Claim USB Accessory

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

An entitlement that enables an app to use the Accessory Access framework to manage access to USB devices in macOS.

**Availability**:
- macOS 27.0+

## Details

- **Name**: `com.apple.developer.accessory-access.usb`
- **Type**: boolean

#### Discussion

This entitlement enables your app to gain exclusive access to USB devices using the Accessory Access framework.

> **Note**: Without this entitlement, your code receives an AccessoryAccess error [`internalError`](../../AccessoryAccess/aaerror/internalerror.md) and a failure reason string of “Unable to communicate with service” when it attempts to call API in the Accessory Access framework.

Add the entitlement to your app by following these steps:

1. Open your app’s Xcode project and select your app from the target list.
2. Select the Signing & Capabilities panel.
3. Click “+ Capabilities” and enter “accessory” in the search field; then double-click the “Claim USB Accessory” entry to add the entitlement to your app’s entitlements file.

For more information about using the Accessory Access framework, see [Accessory Access](../../AccessoryAccess/AccessoryAccess.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.accessory-access.usb)*