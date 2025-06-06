# assetListResponseStatusDidChangeNotification

**Framework**: AVFoundation  
**Kind**: property

A notification the system posts when the status of an interstitial event’s asset list response changes.

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
class let assetListResponseStatusDidChangeNotification: NSNotification.Name
```

#### Discussion

Notifications of this type provide a [`userInfo`](https://developer.apple.com/documentation/foundation/notification/1779652-userinfo) dictionary that can contain values for the keys listed below.

## Topics

### User information keys
- [let AVPlayerInterstitialEventMonitorAssetListResponseStatusDidChangeEventKey: String](avplayerinterstitialeventmonitorassetlistresponsestatusdidchangeeventkey.md)
  A key to retrieve the interstitial event that has an asset list response status change.
- [let AVPlayerInterstitialEventMonitorAssetListResponseStatusDidChangeStatusKey: String](avplayerinterstitialeventmonitorassetlistresponsestatusdidchangestatuskey.md)
  A key to retrieve the asset list response status.
- [let AVPlayerInterstitialEventMonitorAssetListResponseStatusDidChangeErrorKey: String](avplayerinterstitialeventmonitorassetlistresponsestatusdidchangeerrorkey.md)
  A key to retrieve the error related to a change in an interstitial event’s asset list response.

## See Also

- [enum AVPlayerInterstitialEventAssetListResponseStatus](avplayerinterstitialeventassetlistresponsestatus.md)
  Constants that describe the status of the asset list response for an interstitial event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/assetlistresponsestatusdidchangenotification)*