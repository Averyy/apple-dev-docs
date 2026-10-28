# isAutoVideoFrameRateEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, getter=isAutoVideoFrameRateEnabled) BOOL autoVideoFrameRateEnabled;
```

## Discussion

You can enable this property on a device when its active format’s [`isAutoVideoFrameRateSupported`](./format/isautovideoframeratesupported.md) property is [`true`](../../Swift/true.md). When enabled, a capture device automatically adjusts the active frame rate based on light level. Under low light conditions, it decreases the frame rate to properly expose the scene. For formats with a maximum frame rate of 30 fps, the frame rate switches between 30-24. For formats with a maximum frame rate of 60 fps, the frame rate switches between 60-30-24.

> ❗ **Important**:  After enabling automatic frame rate adjustments, attempting to set a device’s [`activeVideoMinFrameDuration`](./activevideominframeduration.md) or [`activeVideoMaxFrameDuration`](./activevideomaxframeduration.md) throws an exception.

Changing the device’s active format resets this property to its default value of [`false`](../../Swift/false.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isautovideoframerateenabled)*