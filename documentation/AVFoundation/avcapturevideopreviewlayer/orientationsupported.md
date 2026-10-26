# orientationSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Indicates whether the layer display supports changing the orientation.

**Availability**:
- iOS 4.0+ - Deprecated in 6.0
- iPadOS 4.0+ - Deprecated in 6.0
- Mac Catalyst 14.0+ - Deprecated in 13.1

> **Deprecated**: Use [`isVideoOrientationSupported`](../avcaptureconnection/isvideoorientationsupported.md) ([`AVCaptureConnection`](../avcaptureconnection.md)) instead.

## Declaration

```objc
@property (nonatomic, readonly, getter=isOrientationSupported) BOOL orientationSupported;
```

## See Also

### Layer configuration
- [orientation](./orientation.md)
  The layer’s orientation.
- [mirrored](./mirrored.md)
  Indicates whether the layer display is mirrored.
- [mirroringSupported](./mirroringsupported.md)
  Indicates whether the layer display supports mirroring.
- [automaticallyAdjustsMirroring](./automaticallyadjustsmirroring.md)
  Indicates whether the layer display automatically adjusts mirroring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/orientationsupported)*