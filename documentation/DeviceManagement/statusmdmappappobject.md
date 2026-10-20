# StatusMDMAppAppObject

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

A status report that contains details about an MDM-installed app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```
object StatusMDMAppAppObject
```

## Properties

- `_removed` (boolean): If `true`, the system removed the app and only this key and the `identifier` key are present in the status item object. The device reports an MDM-installed app as removed if management of the app has been transferred to Declarative Device Management.

  **Default**: `false`
- `external-version-id` (string): The app’s external version identifier. You can also retrieve this value from the App Store. For more information, see [Apps and books metadata for organizations](./apps-and-books-metadata-for-organizations.md).

  If the current external version identifier of an app on the App Store doesn’t match the external version identifier reported by the device, there may be an app update available for the device.
- `identifier` (string) *(required)*: The app’s bundle id, which is unique.
- `name` (string): The name of the app.
- `short-version` (string): The short version of the app.
- `state` (string): The status of the app that [`ManagedApplicationListCommand`](./managedapplicationlistcommand.md) reports.

  **Allowed Values**: `queued`, `needs-redemption`, `redeeming`, `prompting`, `prompting-for-login`, `validating-purchase`, `prompting-for-update`, `prompting-for-update-login`, `prompting-for-management`, `validating-update`, `updating`, `installing`, `managed`, `managed-but-uninstalled`, `unknown`, `user-installed-app`, `user-rejected`, `update-rejected`, `management-rejected`, `failed`
- `version` (string): The version of the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusmdmappappobject)*