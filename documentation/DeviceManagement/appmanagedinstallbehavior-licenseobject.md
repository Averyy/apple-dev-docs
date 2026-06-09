# AppManagedInstallBehavior_LicenseObject

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes the app’s license.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 26.0+
- visionOS 2.4+

## Declaration

```swift
object AppManagedInstallBehavior_LicenseObject
```

## Mentions

- [Installing, managing, updating, and removing apps](installing-managing-updating-and-removing-apps.md)

## Properties

- `Assignment` (string): The type of license that the app uses for installation through the App Store, which is one of the following values: - `Device`: The app has a device license.
- `User`: The app has a user license. This key needs to be present for App Store apps, when either `AppStoreID` or `BundleID` are present in the configuration.
- `VPPType` (string)


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/appmanagedinstallbehavior_licenseobject)*