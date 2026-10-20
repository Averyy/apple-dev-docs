# assetListResponseStatusDidChangeStatusKey

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A key to retrieve the asset list response status.

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
class let assetListResponseStatusDidChangeStatusKey: String
```

```c
extern NSString * const AVPlayerInterstitialEventMonitorAssetListResponseStatusDidChangeStatusKey;
```

#### Discussion

Use this key to retrieve the  [`AVPlayerInterstitialEventAssetListResponseStatus`](../avplayerinterstitialeventassetlistresponsestatus.md) value that indicates the changed asset response status.

## See Also

### User information keys
- [class let assetListResponseStatusDidChangeEventKey: String](./assetlistresponsestatusdidchangeeventkey.md)
  A key to retrieve the interstitial event that has an asset list response status change.
- [class let assetListResponseStatusDidChangeErrorKey: String](./assetlistresponsestatusdidchangeerrorkey.md)
  A key to retrieve the error related to a change in an interstitial event’s asset list response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/assetlistresponsestatusdidchangestatuskey)*