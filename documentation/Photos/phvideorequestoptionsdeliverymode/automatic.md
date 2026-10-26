# PHVideoRequestOptionsDeliveryMode.automatic

**Framework**: Photos  
**Kind**: case  
**Role**: Case

Photos automatically determines which quality of video data to provide based on the request and current conditions.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case automatic
```

```c
PHVideoRequestOptionsDeliveryModeAutomatic
```

#### Discussion

When you request an [`AVAsset`](../../AVFoundation/avasset.md) or [`AVPlayerItem`](../../AVFoundation/avplayeritem.md) object, Photos typically uses the medium-quality format. When you request an [`AVAssetExportSession`](../../AVFoundation/avassetexportsession.md) object for writing out the asset’s contents, Photos always uses the high-quality format.

## See Also

### Constants
- [PHVideoRequestOptionsDeliveryMode.highQualityFormat](./highqualityformat.md)
  Photos provides only the highest quality video available.
- [PHVideoRequestOptionsDeliveryMode.mediumQualityFormat](./mediumqualityformat.md)
  Photos provides a video of moderate quality unless a higher quality version is locally cached.
- [PHVideoRequestOptionsDeliveryMode.fastFormat](./fastformat.md)
  Photos provides whatever quality of video can be most quickly loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phvideorequestoptionsdeliverymode/automatic)*