# isHighestPhotoQualitySupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether this format supports the highest photo quality that the platform delivers.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isHighestPhotoQualitySupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isHighestPhotoQualitySupported) BOOL highestPhotoQualitySupported;
```

## Discussion

The simplest way to capture the highest quality photos is to set [`photo`](../../avcapturesession/preset/photo.md) as your session’s preset. If you’re instead manually setting the capture device’s [`activeFormat`](../activeformat.md) value, select the format whose [`isHighestPhotoQualitySupported`](./ishighestphotoqualitysupported.md) property is [`true`](../../../Swift/true.md).

## See Also

### Determining photo quality
- [var supportedMaxPhotoDimensions: [CMVideoDimensions]](./supportedmaxphotodimensions.md)
  The maximum photo dimension this format supports.
- [var isHighPhotoQualitySupported: Bool](./ishighphotoqualitysupported.md)
  A Boolean value that indicates whether this format supports high-quality capture with the current quality prioritization setting.
- [supportedMaxPhotoDimensions](../../avcapturedeviceformat/supportedmaxphotodimensions.md)
  The maximum photo dimension this format supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/ishighestphotoqualitysupported)*