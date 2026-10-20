# activeExternalSyncVideoFrameDuration

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The receiver’s external sync frame duration (the reciprocal of its frame rate) when being driven by an external sync device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var activeExternalSyncVideoFrameDuration: CMTime { get }
```

```objc
@property (nonatomic, readonly) CMTime activeExternalSyncVideoFrameDuration;
```

#### Discussion

Set up your input to follow an external sync device by calling [`follow(_:videoFrameDuration:delegate:)`](./follow%28_,videoframeduration,delegate%29.md).

> **Note**: The value of this readonly property is `kCMTimeInvalid` unless the [`AVExternalSyncDevice`](../avexternalsyncdevice.md) is actively driving the [`AVCaptureDeviceInput`](../avcapturedeviceinput.md). This is reflected by the [`status`](../avexternalsyncdevice/status.md) being either `AVExternalSyncDeviceStatusActiveSync` or `AVExternalSyncDeviceStatusFreeRunSync`.

## See Also

### Synchronizing with external devices
- [var isExternalSyncSupported: Bool](./isexternalsyncsupported.md)
  Indicates whether the device input supports being configured to follow an external sync device.
- [func follow(AVExternalSyncDevice, videoFrameDuration: CMTime, delegate: (any AVExternalSyncDeviceDelegate)?)](./follow%28_,videoframeduration,delegate%29.md)
  Configures the the device input to follow an external sync device at the given frame duration.
- [func unfollowExternalSyncDevice()](./unfollowexternalsyncdevice%28%29.md)
  Discontinues external sync.
- [var externalSyncDevice: AVExternalSyncDevice?](./externalsyncdevice.md)
  The external sync device currently being followed by this input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/activeexternalsyncvideoframeduration)*