# isHighestPhotoQualitySupported

**Framework**: AVFoundation  
**Kind**: property

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

#### Discussion

The simplest way to capture the highest quality photos is to set [`photo`](avcapturesession/preset/photo.md) as your session’s preset. If you’re instead manually setting the capture device’s [`activeFormat`](avcapturedevice/activeformat.md) value, select the format whose [`isHighestPhotoQualitySupported`](avcapturedevice/format/ishighestphotoqualitysupported.md) property is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var supportedMaxPhotoDimensions: [CMVideoDimensions]](avcapturedevice/format/supportedmaxphotodimensions.md)
  The maximum photo dimension this format supports.
- [var isHighPhotoQualitySupported: Bool](avcapturedevice/format/ishighphotoqualitysupported.md)
  A Boolean value that indicates whether this format supports high-quality capture with the current quality prioritization setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/ishighestphotoqualitysupported)*