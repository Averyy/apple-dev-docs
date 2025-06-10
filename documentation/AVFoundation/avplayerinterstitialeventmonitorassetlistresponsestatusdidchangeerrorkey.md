# AVPlayerInterstitialEventMonitorAssetListResponseStatusDidChangeErrorKey

**Framework**: AVFoundation  
**Kind**: var

A key to retrieve the error related to a change in an interstitial event’s asset list response.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
let AVPlayerInterstitialEventMonitorAssetListResponseStatusDidChangeErrorKey: String
```

#### Discussion

This key only exists in the notification’s [`userInfo`](https://developer.apple.com/documentation/Foundation/Notification/userInfo) dictionary when the status is [`AVPlayerInterstitialEventAssetListResponseStatus.unavailable`](avplayerinterstitialeventassetlistresponsestatus/unavailable.md). Use it to retrieve an error object that provides information about the failure to read the asset list.

## See Also

- [let AVPlayerInterstitialEventMonitorAssetListResponseStatusDidChangeEventKey: String](avplayerinterstitialeventmonitorassetlistresponsestatusdidchangeeventkey.md)
  A key to retrieve the interstitial event that has an asset list response status change.
- [let AVPlayerInterstitialEventMonitorAssetListResponseStatusDidChangeStatusKey: String](avplayerinterstitialeventmonitorassetlistresponsestatusdidchangestatuskey.md)
  A key to retrieve the asset list response status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitorassetlistresponsestatusdidchangeerrorkey)*