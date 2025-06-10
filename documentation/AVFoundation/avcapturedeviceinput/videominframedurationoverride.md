# videoMinFrameDurationOverride

**Framework**: AVFoundation  
**Kind**: property

A time value that acts as a modifier to a capture device’s active video minimum frame duration.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var videoMinFrameDurationOverride: CMTime { get set }
```

#### Discussion

A capture device’s [`activeVideoMinFrameDuration`](avcapturedevice/activevideominframeduration.md) property is the reciprocal of its active maximum frame rate. To limit the maximum frame rate of the capture device, you may set [`activeVideoMinFrameDuration`](avcapturedevice/activevideominframeduration.md) to a value supported by the device’s [`activeFormat`](avcapturedevice/activeformat.md). Changes you make to the device’s [`activeVideoMinFrameDuration`](avcapturedevice/activevideominframeduration.md) value take effect immediately without disrupting preview. Therefore, [`AVCaptureSession`](avcapturesession.md) must always allocate sufficient resources to allow the device to run at its active format’s maximum frame rate.

If you wish to use a particular device format but run it only at lower frame rates (for instance, only run a 1080p240 fps format at a maximum frame rate of 60), set the input’s [`videoMinFrameDurationOverride`](avcapturedeviceinput/videominframedurationoverride.md) property to the reciprocal of the maximum frame rate you intend to use before starting the session (or within a [`beginConfiguration()`](avcapturesession/beginconfiguration().md) / [`commitConfiguration()`](avcapturesession/commitconfiguration().md) block while running the session).

This property’s default value is [`invalid`](https://developer.apple.com/documentation/CoreMedia/CMTime/invalid). When you remove a device input from a session and then add it back, this property reverts to its default value.

## See Also

- [var unifiedAutoExposureDefaultsEnabled: Bool](avcapturedeviceinput/unifiedautoexposuredefaultsenabled.md)
  A Boolean value that indicates whether the input enables unified auto-exposure defaults.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/videominframedurationoverride)*