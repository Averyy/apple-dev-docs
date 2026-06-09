# StatusAppManagedListAppObject

**Framework**: Device Management  
**Kind**: dictionary

A managed app.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 26.0+
- visionOS 2.4+

## Declaration

```swift
object StatusAppManagedListAppObject
```

## Topics

### Objects
- [object StatusAppManagedListManagedConfigurationObject](statusappmanagedlistmanagedconfigurationobject.md)
  The status of app or extension managed configurations. This key is only present when managed configurations are available for the managed app or any of its extensions.
- [object StatusAppManagedListStatusReasonObject](statusappmanagedliststatusreasonobject.md)
  Information about a status error.

## Properties

- `_removed` (boolean): If `true`, the system removed the app and only this key and the `identifier` key are present in the status item object.
- `config-state` (StatusAppManagedListManagedConfigurationObject): The status of app or extension managed configurations. This key is only present when managed configurations are available for the managed app or any of its extensions. Available: iOS 18.4+ | iPadOS 18.4+ | macOS 27+ | visionOS 2.4+
- `declaration-identifier` (string): The identifier of the declaration that controls the app.
- `external-version-id` (integer): The app’s external version identifier. You can also retrieve this value from the App Store. For more information, see [`Apps and books metadata for organizations`](apps-and-books-metadata-for-organizations.md). If the current external version identifier of an app on the App Store doesn’t match the external version identifier reported by the device, there may be an app update available for the device.
- `identifier` (string) *(required)*: The app’s bundle id, which is unique.
- `name` (string): The name of the app.
- `reasons` ([StatusAppManagedListStatusReasonObject]): An array that contains additional details about the app state, including errors.
- `short-version` (string): The short version of the app.
- `state` (string): The status of the app, which has the following possible values: - `optional`: The app is optional and the user has to trigger its installation.
- `queued`: The system has started installation of the app.
- `not-present`: Management of the app occurs after it is installed.
- `prompting-for-consent`: The system is displaying a prompt to the user to proceed with app installation.
- `prompting-for-login`: The system is displaying an App Store sign-in prompt to the user to allow app installation.
- `prompting-for-management`: The system is displaying a prompt to the user to allow changing the installed app to a managed app.
- `downloading`: The system is downloading the app.
- `installing`: The system is installing the app.
- `managed`: The app is installed and managed.
- `managed-but-uninstalled`: The app is required, but the system hasn’t installed it. The app becomes managed if the system installs it again. If the user removes an optional app, its state is `optional`, not `managed-but-uninstalled`.
- `failed`: The app install failed.
- `update-state` (string): The update status of the app, which has the following possible values: - `available`: An update is available for the app.
- `prompting-for-update`: The system is displaying a prompt to the user to proceed with app installation.
- `prompting-for-update-login`: The system is displaying an App Store sign-in prompt to the user to allow app installation.
- `updating`: The app is updating.
- `failed`: The app update failed. > **Note**:  This key is only present if `state` is `managed` and an update is available.
- `version` (string): The version of the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusappmanagedlistappobject)*