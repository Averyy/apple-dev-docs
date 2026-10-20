# AVPlayerInterstitialEventAssetListResponseStatus

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the status of the asset list response for an interstitial event.

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
enum AVPlayerInterstitialEventAssetListResponseStatus
```

```c
enum AVPlayerInterstitialEventAssetListResponseStatus : NSInteger;
```

## Topics

### Status values
- [AVPlayerInterstitialEventAssetListResponseStatus.available](./avplayerinterstitialeventassetlistresponsestatus/available.md)
  Indicates that a valid asset list response is available.
- [AVPlayerInterstitialEventAssetListResponseStatus.cleared](./avplayerinterstitialeventassetlistresponsestatus/cleared.md)
  Indicates that the system cleared the asset list response.
- [AVPlayerInterstitialEventAssetListResponseStatus.unavailable](./avplayerinterstitialeventassetlistresponsestatus/unavailable.md)
  Indicates that the asset list response is unavailable.
### Initializers
- [init?(rawValue: Int)](./avplayerinterstitialeventassetlistresponsestatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Monitoring the asset list response
- [class let assetListResponseStatusDidChangeNotification: NSNotification.Name](./avplayerinterstitialeventmonitor/assetlistresponsestatusdidchangenotification.md)
  A notification the system posts when the status of an interstitial event’s asset list response changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventassetlistresponsestatus)*