# AVPlayerInterstitialEventAssetListResponseStatus.available

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

Indicates that a valid asset list response is available.

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
case available
```

```c
AVPlayerInterstitialEventAssetListResponseStatusAvailable
```

#### Discussion

You can retrieve the value by querying the [`assetListResponse`](../avplayerinterstitialevent/assetlistresponse.md) property of the interstitial event.

## See Also

### Status values
- [AVPlayerInterstitialEventAssetListResponseStatus.cleared](./cleared.md)
  Indicates that the system cleared the asset list response.
- [AVPlayerInterstitialEventAssetListResponseStatus.unavailable](./unavailable.md)
  Indicates that the asset list response is unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventassetlistresponsestatus/available)*