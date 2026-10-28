# externalSyncDevice

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) AVExternalSyncDevice * externalSyncDevice;
```

## Discussion

This readonly property returns the [`AVExternalSyncDevice`](../avexternalsyncdevice.md) instance you provided in [`follow(_:videoFrameDuration:delegate:)`](./follow%28_,videoframeduration,delegate%29.md). This property returns `nil` when an external sync device is disconnected or fails to calibrate.

## See Also

### Synchronizing with external devices
- [var isExternalSyncSupported: Bool](./isexternalsyncsupported.md)
  Indicates whether the device input supports being configured to follow an external sync device.
- [func follow(AVExternalSyncDevice, videoFrameDuration: CMTime, delegate: (any AVExternalSyncDeviceDelegate)?)](./follow%28_,videoframeduration,delegate%29.md)
  Configures the the device input to follow an external sync device at the given frame duration.
- [func unfollowExternalSyncDevice()](./unfollowexternalsyncdevice%28%29.md)
  Discontinues external sync.
- [var activeExternalSyncVideoFrameDuration: CMTime](./activeexternalsyncvideoframeduration.md)
  The receiver’s external sync frame duration (the reciprocal of its frame rate) when being driven by an external sync device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/externalsyncdevice)*