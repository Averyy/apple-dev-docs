# mirroringSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Indicates whether the layer display supports mirroring.

**Availability**:
- iOS 4.0+ - Deprecated in 6.0
- iPadOS 4.0+ - Deprecated in 6.0
- Mac Catalyst 14.0+ - Deprecated in 13.1

> **Deprecated**: Use [`isVideoMirroringSupported`](../avcaptureconnection/isvideomirroringsupported.md) ([`AVCaptureConnection`](../avcaptureconnection.md)) instead.

## Declaration

```objc
@property (nonatomic, readonly, getter=isMirroringSupported) BOOL mirroringSupported;
```

## See Also

### Layer configuration
- [orientation](./orientation.md)
  The layer’s orientation.
- [orientationSupported](./orientationsupported.md)
  Indicates whether the layer display supports changing the orientation.
- [mirrored](./mirrored.md)
  Indicates whether the layer display is mirrored.
- [automaticallyAdjustsMirroring](./automaticallyadjustsmirroring.md)
  Indicates whether the layer display automatically adjusts mirroring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/mirroringsupported)*