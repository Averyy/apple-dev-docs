# activeLockedVideoFrameDuration

**Framework**: AVFoundation  
**Kind**: property

The receiver’s locked frame duration (the reciprocal of its frame rate). Setting this property guarantees the intra-frame duration delivered by the device input is precisely the frame duration you request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var activeLockedVideoFrameDuration: CMTime { get set }
```

#### Discussion

Set this property to run the receiver’s associated [`AVCaptureDevice`](avcapturedevice.md) at precisely your provided frame rate (expressed as a duration). Query [`minSupportedLockedVideoFrameDuration`](avcapturedevice/minsupportedlockedvideoframeduration.md) to find the minimum value supported by this [`AVCaptureDeviceInput`](avcapturedeviceinput.md). In order to disable locked video frame duration, set this property to `kCMTimeInvalid`. This property resets itself to `kCMTimeInvalid` when the receiver’s attached [`activeFormat`](avcapturedevice/activeformat.md) changes. When you set this property, its value is also reflected in the receiver’s [`activeVideoMinFrameDuration`](avcapturedevice/activevideominframeduration.md) and [`activeVideoMaxFrameDuration`](avcapturedevice/activevideomaxframeduration.md).

> **Note**: Locked frame duration availability may change depending on the device configuration. For example, locked frame duration is unsupported when [`isAutoVideoFrameRateEnabled`](avcapturedevice/isautovideoframerateenabled.md) or [`isSpatialVideoCaptureEnabled`](avcapturemoviefileoutput/isspatialvideocaptureenabled.md) is set to `true`.

> **Note**: Only one [`AVCaptureDeviceInput`](avcapturedeviceinput.md) added to an [`AVCaptureMultiCamSession`](avcapturemulticamsession.md) can follow an external sync device or run at a locked frame duration.

> **Note**: Setting this property may cause a lengthy reconfiguration of the receiver, similar to setting [`activeFormat`](avcapturedevice/activeformat.md) or [`sessionPreset`](avcapturesession/sessionpreset.md).

> ❗ **Important**: If you set this property to a valid value while the receiver’s [`minSupportedLockedVideoFrameDuration`](avcapturedevice/minsupportedlockedvideoframeduration.md) is `kCMTimeInvalid`, it throws an `NSInvalidArgumentException`.

> ❗ **Important**: If you set this property while the receiver’s  [`isLockedVideoFrameDurationSupported`](avcapturedeviceinput/islockedvideoframedurationsupported.md) property returns `false`, it throws an `NSInvalidArgumentException`.

## See Also

- [var isLockedVideoFrameDurationSupported: Bool](avcapturedeviceinput/islockedvideoframedurationsupported.md)
  Indicates whether the device input supports locked frame durations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/activelockedvideoframeduration)*