# isFollowingExternalSyncDevice

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, getter=isFollowingExternalSyncDevice) BOOL followingExternalSyncDevice;
```

## Discussion

See [`follow(_:videoFrameDuration:delegate:)`](../avcapturedeviceinput/follow%28_,videoframeduration,delegate%29.md) for more information on external sync.

## See Also

### Synchronizing with external devices
- [var minSupportedExternalSyncFrameDuration: CMTime](./minsupportedexternalsyncframeduration.md)
  The minimum frame duration that can be passed as the `videoFrameDuration` when directing your device input to follow an external sync device.
- [var isVideoFrameDurationLocked: Bool](./isvideoframedurationlocked.md)
  Whether the device’s video frame rate (expressed as a duration) is currently locked.
- [var minSupportedLockedVideoFrameDuration: CMTime](./minsupportedlockedvideoframeduration.md)
  The maximum frame rate (expressed as a minimum duration) that can be set on an input associated with this device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isfollowingexternalsyncdevice)*