# com.apple.developer.app-migration.data-container-access

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

An entitlement required for app extensions to perform a one-time transfer of on-device data to or from another platform.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+

## Details

- **Name**: `com.apple.developer.app-migration.data-container-access` (App Identifier for OS Data Transfer)
- **Type**: array of string 

#### Discussion

Use this entitlement with the app extension that implements the [`AppMigrationExtension`](../../AppMigrationKit/appmigrationextension.md) protocol from the [AppMigrationKit](../../AppMigrationKit/AppMigrationKit.md) framework.

The value of this entitlement is an array of strings. Populate this value with a one-item array containing the bundle identifier of the extension’s containing app. No other values are valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.app-migration.data-container-access)*