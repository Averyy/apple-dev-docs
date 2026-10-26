# PHVideoRequestOptionsDeliveryMode.fastFormat

**Framework**: Photos  
**Kind**: case  
**Role**: Case

Photos provides whatever quality of video can be most quickly loaded.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case fastFormat
```

```c
PHVideoRequestOptionsDeliveryModeFastFormat
```

#### Discussion

When the [`isNetworkAccessAllowed`](../phvideorequestoptions/isnetworkaccessallowed.md) property is `true`, the fast option provides a version of the video asset suitable for streaming from iCloud over a low-quality connection—for example, an MP4 video with 360p resolution. If a higher-quality version is already cached on the device, Photos provides that video instead.

## See Also

### Constants
- [PHVideoRequestOptionsDeliveryMode.automatic](./automatic.md)
  Photos automatically determines which quality of video data to provide based on the request and current conditions.
- [PHVideoRequestOptionsDeliveryMode.highQualityFormat](./highqualityformat.md)
  Photos provides only the highest quality video available.
- [PHVideoRequestOptionsDeliveryMode.mediumQualityFormat](./mediumqualityformat.md)
  Photos provides a video of moderate quality unless a higher quality version is locally cached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phvideorequestoptionsdeliverymode/fastformat)*