# unfollowExternalSyncDevice()

**Framework**: AVFoundation  
**Kind**: method

Discontinues external sync.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
func unfollowExternalSyncDevice()
```

#### Discussion

This method stops your input from syncing to the external sync device you specified in [`follow(_:videoFrameDuration:delegate:)`](avcapturedeviceinput/follow(_:videoframeduration:delegate:).md).

## See Also

- [var isExternalSyncSupported: Bool](avcapturedeviceinput/isexternalsyncsupported.md)
  Indicates whether the device input supports being configured to follow an external sync device.
- [func follow(AVExternalSyncDevice, videoFrameDuration: CMTime, delegate: (any AVExternalSyncDeviceDelegate)?)](avcapturedeviceinput/follow(_:videoframeduration:delegate:).md)
  Configures the the device input to follow an external sync device at the given frame duration.
- [var activeExternalSyncVideoFrameDuration: CMTime](avcapturedeviceinput/activeexternalsyncvideoframeduration.md)
  The receiver’s external sync frame duration (the reciprocal of its frame rate) when being driven by an external sync device.
- [var externalSyncDevice: AVExternalSyncDevice?](avcapturedeviceinput/externalsyncdevice.md)
  The external sync device currently being followed by this input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/unfollowexternalsyncdevice())*