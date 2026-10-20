# OSUpdateStatusResponse.OSUpdateStatusItem

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

A dictionary that describes the status of a software update.

**Availability**:
- iOS 9.0+ - Deprecated in 26.0
- iPadOS 9.0+ - Deprecated in 26.0
- Mac Catalyst 9.0+ - Deprecated in 26.0
- macOS 10.11.5+ - Deprecated in 26.0
- tvOS 12.0+ - Deprecated in 26.0

> **Deprecated**: **Removed** Use the declarative management software update features instead.

## Declaration

```
object OSUpdateStatusResponse.OSUpdateStatusItem
```

## Properties

- `DeferralsRemaining` (integer) *(deprecated)*: ~~The number of remaining user deferrals for this OS update.~~

  ~~Available: macOS 12.3+~~
  ~~Deprecated: iOS 26+ | iPadOS 26+ | macOS 26+ | tvOS 26+~~
  Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `DownloadPercentComplete` (number) *(required)* *(deprecated)*: ~~A floating-point number between `0.0` and `1.0` that indicates the download progress as a percentage.~~

  ~~Deprecated: iOS 26+ | iPadOS 26+ | macOS 26+ | tvOS 26+~~
  Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `IsDownloaded` (boolean) *(required)* *(deprecated)*: ~~If `true`, the update has finished downloading.~~

  ~~Deprecated: iOS 26+ | iPadOS 26+ | macOS 26+ | tvOS 26+~~
  Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `MaxDeferrals` (integer) *(deprecated)*: ~~The number of times a user can defer this OS update.~~

  ~~Available: macOS 12.3+~~
  ~~Deprecated: iOS 26+ | iPadOS 26+ | macOS 26+ | tvOS 26+~~
  Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `NextScheduledInstall` (date) *(deprecated)*: ~~The date of the next attempt at installing this OS update.~~

  ~~Available: macOS 12.3+~~
  ~~Deprecated: iOS 26+ | iPadOS 26+ | macOS 26+ | tvOS 26+~~
  Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `PastNotifications` ([date]) *(deprecated)*: ~~The dates/times when the OS notified the user about installing this OS update.~~

  ~~Available: macOS 12.3+~~
  ~~Deprecated: iOS 26+ | iPadOS 26+ | macOS 26+ | tvOS 26+~~
  Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `ProductKey` (string) *(required)* *(deprecated)*: ~~The product key that represents the update.~~

  ~~Deprecated: iOS 26+ | iPadOS 26+ | macOS 26+ | tvOS 26+~~
  Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `Status` (string) *(required)* *(deprecated)*: ~~The status of the update, which is one of the following values:~~

  ~~- `Idle`: The update is idle.~~ ~~- `Downloading`: The software update is downloading and subsequently preparing.~~ ~~- `Installing`: The software update is installing.~~

  ~~Deprecated: iOS 26+ | iPadOS 26+ | macOS 26+ | tvOS 26+~~
  Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+

## See Also

### Objects
- [object OSUpdateStatusResponse.ErrorChainItem](./errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/osupdatestatusresponse/osupdatestatusitem)*