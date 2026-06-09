# AppSettingsAllowedObject

**Framework**: Device Management  
**Kind**: dictionary

The dictionary of allowed app settings.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object AppSettingsAllowedObject
```

## Topics

### Objects
- [object AppSettingsAllowed_BinaryIdentifierObject](appsettingsallowed_binaryidentifierobject.md)
  Dictionary containing one or more identifier fields to match a binary.

## Properties

- `AllowedApps` ([string]): If present, the device only shows or launches apps with bundle IDs in the array. Include the value `com.apple.webapp` to allow all webclips. This applies to App Store apps, marketplace apps, and locally installed apps (using Configurator, Xcode, and so forth). Available: iOS 27+ | iPadOS 27+ | tvOS 27+ | visionOS 27+
- `AllowedBinaries` ([AppSettingsAllowed_BinaryIdentifierObject]): If present, the device only allows binaries that match the binary identifier properties to run. A binary is matched only when all the binary identifiers match. The device always runs system critical processes. Use “codesign -dvvv <path_to_binary>” to show the information you need to generate these values. Available: macOS 27+
Allowed scopes: system
- `AlwaysAllowManagedApps` (boolean): If `true`, the device implicitly includes managed apps in the effective allow list when `AllowedApps` or `AllowedBinaries` is present. Available: macOS 27+
Allowed scopes: system
- `DeniedApps` ([string]): If present, the device prevents showing or launching apps with bundle IDs in the array. Include the value `com.apple.webapp` to restrict all webclips. This applies to App Store apps, marketplace apps, and locally installed apps (using Configurator, Xcode, and so forth). > **Note**:  Denying system apps may disable other functionality. For example, denying the App Store app may prevent users from accepting the terms and conditions for the user-based Volume Purchase Program (VPP). Available: iOS 27+ | iPadOS 27+ | tvOS 27+ | visionOS 27+
- `DeniedBinaries` ([AppSettingsAllowed_BinaryIdentifierObject]): If present, the device doesn’t allow binaries that match the binary identifier properties to run. A binary is matched only when all the binary identifiers match. Available: macOS 27+
Allowed scopes: system

## See Also

- [object AppSettingsPrivacyObject](appsettingsprivacyobject.md)
  The dictionary of app settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/appsettingsallowedobject)*