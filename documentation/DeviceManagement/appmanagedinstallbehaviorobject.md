# AppManagedInstallBehaviorObject

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes how and when to install the app.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 26.0+
- visionOS 2.4+

## Declaration

```swift
object AppManagedInstallBehaviorObject
```

## Mentions

- [Installing, managing, updating, and removing apps](installing-managing-updating-and-removing-apps.md)

## Topics

### Objects
- [object AppManagedInstallBehavior_LicenseObject](appmanagedinstallbehavior_licenseobject.md)
  A dictionary that describes the app’s license.

## Properties

- `AllowDownloadsOverCellular` (string): Indicates how the device uses a cellular network when it downloads the app for automatic install or update operations: - `AlwaysOn`: The device downloads apps of any size using a cellular network.
- `AlwaysOff`: The device doesn’t download apps using a cellular network. The device pauses the automatic install or update operation until a different network is active.
- `StoreSettings`: The device uses the settings for the corresponding store when downloading apps. The device always uses the store settings to download apps when the install or update operation is user initiated. Available: iOS 26+ | iPadOS 26+
Allowed enrollments: supervised
- `Install` (string): A string that specifies if the app needs to remain on the device at all times or if the user can freely install and remove it, which is one of the following values: - `Optional`: The user can install and remove the app after the system activates the configuration.
- `Required`: The system installs the app after it activates the configuration. The user can’t remove the app. The system automatically installs apps on supervised devices. Otherwise, the device prompts the user to approve installation of the app.
- `License` (AppManagedInstallBehavior_LicenseObject): A dictionary that describes the app’s license.
- `Version` (integer): The App Store external version identifier (EVID) of the version of the app the device installs. You can retrieve this value from the App Store. For more information, see [`Apps and books metadata for organizations`](apps-and-books-metadata-for-organizations.md). This key is ignored if the app isn’t an App Store app. The following rules apply when the device applies or updates the configuration: - If this key isn’t present: - If the app isn’t present, the device installs the latest version.
- If the app is present, if allowed the device takes over management of the current version of the app.
- If this key is present: - If the app isn’t present, the device installs the app with the specified version.
- If an app with the same version is present, if allowed the device takes over management of that app.
- If an app with an older version is present, if allowed the device updates the app to the specified version and takes over management of it.
- If an app with a newer version is present, the device doesn’t take over management of the app. The device reports an app status failure. > **Note**:  The device never installs an older version of the app over a newer version. Available: iOS 26+ | iPadOS 26+ | macOS 26+ | visionOS 26+

## See Also

- [object AppManagedAppConfigDictionaryObject](appmanagedappconfigdictionaryobject.md)
  A dictionary of app config data and credentials.
- [object AppManagedAttributesObject](appmanagedattributesobject.md)
  A dictionary of values to associate with the app.
- [object AppManagedExtensionConfigsObject](appmanagedextensionconfigsobject.md)
  A dictionary of extension config data and credentials.
- [object AppManagedUpdateBehaviorObject](appmanagedupdatebehaviorobject.md)
  A dictionary that specifies how the device updates apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/appmanagedinstallbehaviorobject)*