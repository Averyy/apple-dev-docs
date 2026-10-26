# orientation

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The layer’s orientation.

**Availability**:
- iOS 4.0+ - Deprecated in 6.0
- iPadOS 4.0+ - Deprecated in 6.0
- Mac Catalyst 14.0+ - Deprecated in 13.1

> **Deprecated**: Use [`videoOrientation`](../avcaptureconnection/videoorientation.md) ([`AVCaptureConnection`](../avcaptureconnection.md)) instead.

## Declaration

```objc
@property (nonatomic) AVCaptureVideoOrientation orientation;
```

#### Discussion

Changes in orientation are not supported on all hardware configurations. You should check the value of [`isVideoOrientationSupported`](../avcaptureconnection/isvideoorientationsupported.md) (`AVCaptureConnection`) before attempting to change the orientation of the receiver. An exception is raised if this requirement is ignored.

## See Also

### Layer configuration
- [orientationSupported](./orientationsupported.md)
  Indicates whether the layer display supports changing the orientation.
- [mirrored](./mirrored.md)
  Indicates whether the layer display is mirrored.
- [mirroringSupported](./mirroringsupported.md)
  Indicates whether the layer display supports mirroring.
- [automaticallyAdjustsMirroring](./automaticallyadjustsmirroring.md)
  Indicates whether the layer display automatically adjusts mirroring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/orientation)*