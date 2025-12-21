# isVideoFrameDurationLocked

**Framework**: AVFoundation  
**Kind**: property

Whether the device’s video frame rate (expressed as a duration) is currently locked.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var isVideoFrameDurationLocked: Bool { get }
```

#### Discussion

Returns `true` when an [`AVCaptureDeviceInput`](avcapturedeviceinput.md) associated with the device has its [`activeLockedVideoFrameDuration`](avcapturedeviceinput/activelockedvideoframeduration.md) property set to something other than `kCMTimeInvalid`. See [`activeLockedVideoFrameDuration`](avcapturedeviceinput/activelockedvideoframeduration.md) for more information on video frame duration locking.

## See Also

- [var isFollowingExternalSyncDevice: Bool](avcapturedevice/isfollowingexternalsyncdevice.md)
  Whether the device is following an external sync device.
- [var minSupportedExternalSyncFrameDuration: CMTime](avcapturedevice/minsupportedexternalsyncframeduration.md)
  The minimum frame duration that can be passed as the `videoFrameDuration` when directing your device input to follow an external sync device.
- [var minSupportedLockedVideoFrameDuration: CMTime](avcapturedevice/minsupportedlockedvideoframeduration.md)
  The maximum frame rate (expressed as a minimum duration) that can be set on an input associated with this device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isvideoframedurationlocked)*