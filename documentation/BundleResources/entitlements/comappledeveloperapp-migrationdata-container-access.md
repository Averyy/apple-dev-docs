# com.apple.developer.app-migration.data-container-access

**Framework**: Bundle Resources  
**Kind**: typealias

An entitlement required for app extensions to perform a one-time transfer of on-device data to or from another platform.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+

#### Discussion

Use this entitlement with the app extension that implements the [`AppMigrationExtension`](https://developer.apple.com/documentation/AppMigrationKit/AppMigrationExtension) protocol from the [`AppMigrationKit`](https://developer.apple.com/documentation/AppMigrationKit) framework.

The value of this entitlement is an array of strings. Populate this value with a one-item array containing the bundle identifier of the extension’s containing app. No other values are valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.app-migration.data-container-access)*