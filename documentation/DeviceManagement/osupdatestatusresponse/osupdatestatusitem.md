# OSUpdateStatusResponse.OSUpdateStatusItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes the status of a software update.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11.5+
- tvOS 12.0+

## Declaration

```swift
object OSUpdateStatusResponse.OSUpdateStatusItem
```

## Properties

- `DeferralsRemaining` (integer): The number of remaining user deferrals for this OS update. Available in macOS 12.3 and later.
- `DownloadPercentComplete` (number) *(required)*: A floating-point number between `0.0` and `1.0` that indicates the download progress as a percentage.
- `IsDownloaded` (boolean) *(required)*: If `true`, the update has finished downloading.
- `MaxDeferrals` (integer): The number of times a user can defer this OS update. Available in macOS 12.3 and later.
- `NextScheduledInstall` (date): The date of the next attempt at installing this OS update. Available in macOS 12.3 and later.
- `PastNotifications` ([date]): The dates/times when the OS notified the user about installing this OS update. Available in macOS 12.3 and later.
- `ProductKey` (string) *(required)*: The product key that represents the update.
- `Status` (string) *(required)*: The status of the update, which is one of the following values: - `Idle`: The update is idle.
- `Downloading`: The software update is downloading and subsequently preparing.
- `Installing`: The software update is installing.

## See Also

- [object OSUpdateStatusResponse.ErrorChainItem](osupdatestatusresponse/errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/osupdatestatusresponse/osupdatestatusitem)*