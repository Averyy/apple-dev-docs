# PHVideoRequestOptionsDeliveryMode.mediumQualityFormat

**Framework**: Photos  
**Kind**: case  
**Role**: Case

Photos provides a video of moderate quality unless a higher quality version is locally cached.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case mediumQualityFormat
```

```c
PHVideoRequestOptionsDeliveryModeMediumQualityFormat
```

## Discussion

When the [`isNetworkAccessAllowed`](../phvideorequestoptions/isnetworkaccessallowed.md) property is `true`, the medium quality option provides a version of the video asset that is suitable for streaming from iCloud and displaying on a device—for example, an MP4 video with 720p resolution. If a higher-quality version is already cached on the device, Photos provides that video instead.

## See Also

### Constants
- [PHVideoRequestOptionsDeliveryMode.automatic](./automatic.md)
  Photos automatically determines which quality of video data to provide based on the request and current conditions.
- [PHVideoRequestOptionsDeliveryMode.highQualityFormat](./highqualityformat.md)
  Photos provides only the highest quality video available.
- [PHVideoRequestOptionsDeliveryMode.fastFormat](./fastformat.md)
  Photos provides whatever quality of video can be most quickly loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phvideorequestoptionsdeliverymode/mediumqualityformat)*