# highResolutionStillImageDimensions

**Framework**: AVFoundation  
**Kind**: property

The highest resolution still image the system can produce for this format.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var highResolutionStillImageDimensions: CMVideoDimensions { get }
```

#### Discussion

Normally, the [`AVCaptureStillImageOutput`](avcapturestillimageoutput.md) class emits images with the same dimensions as the source [`AVCaptureDevice`](avcapturedevice.md) instance’s [`activeFormat`](avcapturedevice/activeformat.md). However, if you set `highResolutionStillImageOutputEnabled` to [`true`](https://developer.apple.com/documentation/swift/true), [`AVCaptureStillImageOutput`](avcapturestillimageoutput.md) emits still images with its source [`AVCaptureDevice`](avcapturedevice.md) instance’s `activeFormat.highResolutionStillImageDimensions` dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/highresolutionstillimagedimensions)*