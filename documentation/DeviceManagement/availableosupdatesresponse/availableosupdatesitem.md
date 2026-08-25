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

## Declaration

```swift
object AvailableOSUpdatesResponse.AvailableOSUpdatesItem
```

## Properties

- `AllowsInstallLater` (boolean): Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `AppIdentifiersToClose` ([string]) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `Build` (string) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `DeferredUntil` (date): Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `DownloadSize` (integer) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `HumanReadableName` (string) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `HumanReadableNameLocale` (string) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `InstallSize` (integer) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `IsConfigDataUpdate` (boolean): Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `IsCritical` (boolean): Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `IsFirmwareUpdate` (boolean): Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `IsMajorOSUpdate` (boolean): Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `IsSecurityResponse` (boolean) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `MetadataURL` (string) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `ProductKey` (string) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `ProductName` (string) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `RequiresBootstrapToken` (boolean): Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `RestartRequired` (boolean): Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `SupplementalBuildVersion` (string): Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `SupplementalOSVersionExtra` (string): Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `Version` (string) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+

## See Also

- [object AvailableOSUpdatesResponse.ErrorChainItem](availableosupdatesresponse/errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/availableosupdatesresponse/availableosupdatesitem)*