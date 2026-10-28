# isExternalSyncSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, getter=isExternalSyncSupported) BOOL externalSyncSupported;
```

## Discussion

See [`follow(_:videoFrameDuration:delegate:)`](./follow%28_,videoframeduration,delegate%29.md) for more information on external sync.

## See Also

### Synchronizing with external devices
- [func follow(AVExternalSyncDevice, videoFrameDuration: CMTime, delegate: (any AVExternalSyncDeviceDelegate)?)](./follow%28_,videoframeduration,delegate%29.md)
  Configures the the device input to follow an external sync device at the given frame duration.
- [func unfollowExternalSyncDevice()](./unfollowexternalsyncdevice%28%29.md)
  Discontinues external sync.
- [var activeExternalSyncVideoFrameDuration: CMTime](./activeexternalsyncvideoframeduration.md)
  The receiver’s external sync frame duration (the reciprocal of its frame rate) when being driven by an external sync device.
- [var externalSyncDevice: AVExternalSyncDevice?](./externalsyncdevice.md)
  The external sync device currently being followed by this input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/isexternalsyncsupported)*