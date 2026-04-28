# AvailableOSUpdatesResponse.AvailableOSUpdatesItem

**Framework**: Device Management  
**Kind**: dictionary

The response dictionary that describes the available operating-system updates item.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- tvOS 12.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object AvailableOSUpdatesResponse.AvailableOSUpdatesItem
```

## Properties

- `AllowsInstallLater` (boolean): If `true`, download the software update and install it later.
- `AppIdentifiersToClose` ([string]) *(required)*: An array that contains app identifiers of apps to close so you can install the update. This value is available in macOS 10.11 and later.
- `Build` (string) *(required)*: The build number of the update.
- `DeferredUntil` (date): If present, the date when you want the update to install. This value is available in macOS 10.12.4 and later.
- `DownloadSize` (integer) *(required)*: The storage size necessary to download the software update. Prior to macOS 10.14, this only includes major operating-system updates. In macOS 10.14 and later, this also includes minor updates.
- `HumanReadableName` (string) *(required)*: The human-readable name of the update in the current user’s current locale.
- `HumanReadableNameLocale` (string) *(required)*: The locale, in IOS639-1 Alpha-2 code format, of the `HumanReadableName` value. This value is available in macOS 10.11 and later.
- `InstallSize` (integer) *(required)*: The storage size necessary to install the update. This value is available in iOS 9.0 and later, and tvOS 12.0 and later.
- `IsConfigDataUpdate` (boolean): If `true`, this is an update to a configuration file. This value is available in macOS 10.11 and later.
- `IsCritical` (boolean): If `true`, this is a critical update.
- `IsFirmwareUpdate` (boolean): If `true`, this is an update to firmware. This value is available in macOS 10.11 and later.
- `IsMajorOSUpdate` (boolean): If `true`, this is a major update; for example, 10.15.x to 11. This value is available in macOS 10.11 and later.
- `IsSecurityResponse` (boolean) *(required)*: If `true`, this update is a Background Security Improvement.
- `MetadataURL` (string) *(required)*: A URL where the MDM server can request additional localized names for this update. This key isn’t present for certain updates, such as mobile software updates (MSUs) or major OS updates. This value is available in macOS 10.11 and later.
- `ProductKey` (string) *(required)*: The product key that represents the update.
- `ProductName` (string) *(required)*: The product name; for example, *iOS*. This value is available in iOS 9.0 and later, and tvOS 12.0 and later.
- `RequiresBootstrapToken` (boolean): If `true`, the device can accept a Bootstrap Token from the MDM server instead of prompting for user authentication prior to installation. This only applies when `BootstrapTokenAllowedForAuthentication` is `true` in the [`SecurityInfoResponse.SecurityInfo`](securityinforesponse/securityinfo-data.dictionary.md) response. This value is available for a Mac with Apple silicon in macOS 11 and later.
- `RestartRequired` (boolean): If `true`, the device restarts after installing the update.
- `SupplementalBuildVersion` (string): The build version for the Background Security Improvement update, for example, `13A999`, which is the same as `Build`.
- `SupplementalOSVersionExtra` (string): The Background Security Improvement OS version suffix, for example, `(a)`. Only present if this is a Background Security Improvement update.
- `Version` (string) *(required)*: The version of the update.

## See Also

- [object AvailableOSUpdatesResponse.ErrorChainItem](availableosupdatesresponse/errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/availableosupdatesresponse/availableosupdatesitem)*