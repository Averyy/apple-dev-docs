# isFollowingExternalSyncDevice

**Framework**: AVFoundation  
**Kind**: property

Whether the device is following an external sync device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var isFollowingExternalSyncDevice: Bool { get }
```

#### Discussion

See [`follow(_:videoFrameDuration:delegate:)`](avcapturedeviceinput/follow(_:videoframeduration:delegate:).md) for more information on external sync.

## See Also

- [var minSupportedExternalSyncFrameDuration: CMTime](avcapturedevice/minsupportedexternalsyncframeduration.md)
  The minimum frame duration that can be passed as the `videoFrameDuration` when directing your device input to follow an external sync device.
- [var isVideoFrameDurationLocked: Bool](avcapturedevice/isvideoframedurationlocked.md)
  Whether the device’s video frame rate (expressed as a duration) is currently locked.
- [var minSupportedLockedVideoFrameDuration: CMTime](avcapturedevice/minsupportedlockedvideoframeduration.md)
  The maximum frame rate (expressed as a minimum duration) that can be set on an input associated with this device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isfollowingexternalsyncdevice)*