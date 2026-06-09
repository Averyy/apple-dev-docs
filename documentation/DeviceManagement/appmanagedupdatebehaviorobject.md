# AppManagedUpdateBehaviorObject

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that specifies how the device updates apps.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
object AppManagedUpdateBehaviorObject
```

## Mentions

- [Installing, managing, updating, and removing apps](installing-managing-updating-and-removing-apps.md)

## Properties

- `AutomaticAppUpdates` (string) *(required)*: Specifies whether the device automatically updates the app: - `AlwaysOn`: The device automatically updates the app to the latest version. For App Store apps, the device periodically checks the store for updates. For Enterprise apps, the device periodically downloads the manifest file and compares it to the previous manifest file. If the device detects a change to the bundle version in the manifest, it downloads and updates the app.
- `AlwaysOff`: The device never automatically updates the app.
- `StoreSettings`: The device uses the settings for the corresponding store to determine when to automatically update the app. For Enterprise apps, this setting behaves the same as `AlwaysOff`. When you specify the `InstallBehavior.Version` key, the device ignores this key and Automatic App Updates are disabled. In macOS, the device ignores this setting if the `AppComposedIdentifier` key is set in the configuration.

## See Also

- [object AppManagedAppConfigDictionaryObject](appmanagedappconfigdictionaryobject.md)
  A dictionary of app config data and credentials.
- [object AppManagedAttributesObject](appmanagedattributesobject.md)
  A dictionary of values to associate with the app.
- [object AppManagedExtensionConfigsObject](appmanagedextensionconfigsobject.md)
  A dictionary of extension config data and credentials.
- [object AppManagedInstallBehaviorObject](appmanagedinstallbehaviorobject.md)
  A dictionary that describes how and when to install the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/appmanagedupdatebehaviorobject)*