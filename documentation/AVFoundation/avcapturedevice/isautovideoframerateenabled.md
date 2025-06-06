# isAutoVideoFrameRateEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the capture device performs automatic video frame rate adjustments.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
var isAutoVideoFrameRateEnabled: Bool { get set }
```

#### Discussion

You can enable this property on a device when its active format’s [`isAutoVideoFrameRateSupported`](avcapturedevice/format/isautovideoframeratesupported.md) property is [`true`](https://developer.apple.com/documentation/swift/true). When enabled, a capture device automatically adjusts the active frame rate based on light level. Under low light conditions, it decreases the frame rate to properly expose the scene. For formats with a maximum frame rate of 30 fps, the frame rate switches between 30-24. For formats with a maximum frame rate of 60 fps, the frame rate switches between 60-30-24.

> ❗ **Important**:  After enabling automatic frame rate adjustments, attempting to set a device’s [`activeVideoMinFrameDuration`](avcapturedevice/activevideominframeduration.md) or [`activeVideoMaxFrameDuration`](avcapturedevice/activevideomaxframeduration.md) throws an exception.

 After enabling automatic frame rate adjustments, attempting to set a device’s [`activeVideoMinFrameDuration`](avcapturedevice/activevideominframeduration.md) or [`activeVideoMaxFrameDuration`](avcapturedevice/activevideomaxframeduration.md) throws an exception.

Changing the device’s active format resets this property to its default value of [`false`](https://developer.apple.com/documentation/swift/false).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isautovideoframerateenabled)*