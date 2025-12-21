# externalSyncDevice

**Framework**: AVFoundation  
**Kind**: property

The external sync device currently being followed by this input.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var externalSyncDevice: AVExternalSyncDevice? { get }
```

#### Discussion

This readonly property returns the [`AVExternalSyncDevice`](avexternalsyncdevice.md) instance you provided in [`follow(_:videoFrameDuration:delegate:)`](avcapturedeviceinput/follow(_:videoframeduration:delegate:).md). This property returns `nil` when an external sync device is disconnected or fails to calibrate.

## See Also

- [var isExternalSyncSupported: Bool](avcapturedeviceinput/isexternalsyncsupported.md)
  Indicates whether the device input supports being configured to follow an external sync device.
- [func follow(AVExternalSyncDevice, videoFrameDuration: CMTime, delegate: (any AVExternalSyncDeviceDelegate)?)](avcapturedeviceinput/follow(_:videoframeduration:delegate:).md)
  Configures the the device input to follow an external sync device at the given frame duration.
- [func unfollowExternalSyncDevice()](avcapturedeviceinput/unfollowexternalsyncdevice.md)
  Discontinues external sync.
- [var activeExternalSyncVideoFrameDuration: CMTime](avcapturedeviceinput/activeexternalsyncvideoframeduration.md)
  The receiver’s external sync frame duration (the reciprocal of its frame rate) when being driven by an external sync device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/externalsyncdevice)*