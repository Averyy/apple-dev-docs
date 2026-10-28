# unfollowExternalSyncDevice()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) unfollowExternalSyncDevice;
```

## Discussion

This method stops your input from syncing to the external sync device you specified in [`follow(_:videoFrameDuration:delegate:)`](./follow%28_,videoframeduration,delegate%29.md).

## See Also

### Synchronizing with external devices
- [var isExternalSyncSupported: Bool](./isexternalsyncsupported.md)
  Indicates whether the device input supports being configured to follow an external sync device.
- [func follow(AVExternalSyncDevice, videoFrameDuration: CMTime, delegate: (any AVExternalSyncDeviceDelegate)?)](./follow%28_,videoframeduration,delegate%29.md)
  Configures the the device input to follow an external sync device at the given frame duration.
- [var activeExternalSyncVideoFrameDuration: CMTime](./activeexternalsyncvideoframeduration.md)
  The receiver’s external sync frame duration (the reciprocal of its frame rate) when being driven by an external sync device.
- [var externalSyncDevice: AVExternalSyncDevice?](./externalsyncdevice.md)
  The external sync device currently being followed by this input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/unfollowexternalsyncdevice())*