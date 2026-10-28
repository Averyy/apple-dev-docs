# mirrored

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Indicates whether the layer display is mirrored.

**Availability**:
- iOS 4.0+ - Deprecated in 6.0
- iPadOS 4.0+ - Deprecated in 6.0
- Mac Catalyst 14.0+ - Deprecated in 13.1

> **Deprecated**: Use [`isVideoMirrored`](../avcaptureconnection/isvideomirrored.md) ([`AVCaptureConnection`](../avcaptureconnection.md)) instead.

## Declaration

```objc
@property (nonatomic, getter=isMirrored) BOOL mirrored;
```

## Discussion

To change the value of this property, the value of [`automaticallyAdjustsMirroring`](./automaticallyadjustsmirroring.md) must be [`false`](../../Swift/false.md).

Mirroring is not supported on all hardware configurations. You should check the value of [`isVideoMirroringSupported`](../avcaptureconnection/isvideomirroringsupported.md) (`AVCaptureConnection`) before attempting to change this value.

## See Also

### Layer configuration
- [orientation](./orientation.md)
  The layer’s orientation.
- [orientationSupported](./orientationsupported.md)
  Indicates whether the layer display supports changing the orientation.
- [mirroringSupported](./mirroringsupported.md)
  Indicates whether the layer display supports mirroring.
- [automaticallyAdjustsMirroring](./automaticallyadjustsmirroring.md)
  Indicates whether the layer display automatically adjusts mirroring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/mirrored)*