# OSUpdateStatusResponse.OSUpdateStatusItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes the status of a software update.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11.5+
- tvOS 12.0+

## Declaration

```swift
object OSUpdateStatusResponse.OSUpdateStatusItem
```

## Properties

- `DeferralsRemaining` (integer): Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `DownloadPercentComplete` (number) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `IsDownloaded` (boolean) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `MaxDeferrals` (integer): Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `NextScheduledInstall` (date): Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `PastNotifications` ([date]): Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `ProductKey` (string) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `Status` (string) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+

## See Also

- [object OSUpdateStatusResponse.ErrorChainItem](osupdatestatusresponse/errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/osupdatestatusresponse/osupdatestatusitem)*