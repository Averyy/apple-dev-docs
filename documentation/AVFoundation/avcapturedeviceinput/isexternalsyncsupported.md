# isExternalSyncSupported

**Framework**: AVFoundation  
**Kind**: property

Indicates whether the device input supports being configured to follow an external sync device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var isExternalSyncSupported: Bool { get }
```

#### Discussion

See [`follow(_:videoFrameDuration:delegate:)`](avcapturedeviceinput/follow(_:videoframeduration:delegate:).md) for more information on external sync.

## See Also

- [func follow(AVExternalSyncDevice, videoFrameDuration: CMTime, delegate: (any AVExternalSyncDeviceDelegate)?)](avcapturedeviceinput/follow(_:videoframeduration:delegate:).md)
  Configures the the device input to follow an external sync device at the given frame duration.
- [func unfollowExternalSyncDevice()](avcapturedeviceinput/unfollowexternalsyncdevice.md)
  Discontinues external sync.
- [var activeExternalSyncVideoFrameDuration: CMTime](avcapturedeviceinput/activeexternalsyncvideoframeduration.md)
  The receiver’s external sync frame duration (the reciprocal of its frame rate) when being driven by an external sync device.
- [var externalSyncDevice: AVExternalSyncDevice?](avcapturedeviceinput/externalsyncdevice.md)
  The external sync device currently being followed by this input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/isexternalsyncsupported)*