# minSupportedLockedVideoFrameDuration

**Framework**: AVFoundation  
**Kind**: property

The maximum frame rate (expressed as a minimum duration) that can be set on an input associated with this device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var minSupportedLockedVideoFrameDuration: CMTime { get }
```

#### Discussion

`kCMTimeInvalid` is returned when the device or its current configuration does not support locked frame rate. Use [`activeLockedVideoFrameDuration`](avcapturedeviceinput/activelockedvideoframeduration.md) to set the locked frame rate on the input.

## See Also

- [var isFollowingExternalSyncDevice: Bool](avcapturedevice/isfollowingexternalsyncdevice.md)
  Whether the device is following an external sync device.
- [var minSupportedExternalSyncFrameDuration: CMTime](avcapturedevice/minsupportedexternalsyncframeduration.md)
  The minimum frame duration that can be passed as the `videoFrameDuration` when directing your device input to follow an external sync device.
- [var isVideoFrameDurationLocked: Bool](avcapturedevice/isvideoframedurationlocked.md)
  Whether the device’s video frame rate (expressed as a duration) is currently locked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/minsupportedlockedvideoframeduration)*