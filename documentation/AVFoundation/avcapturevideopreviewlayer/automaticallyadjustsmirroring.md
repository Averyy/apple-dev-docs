# automaticallyAdjustsMirroring

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Indicates whether the layer display automatically adjusts mirroring.

**Availability**:
- iOS 4.0+ - Deprecated in 6.0
- iPadOS 4.0+ - Deprecated in 6.0
- Mac Catalyst 14.0+ - Deprecated in 13.1

> **Deprecated**: Use [`automaticallyAdjustsVideoMirroring`](../avcaptureconnection/automaticallyadjustsvideomirroring.md) ([`AVCaptureConnection`](../avcaptureconnection.md)) instead.

## Declaration

```objc
@property (nonatomic) BOOL automaticallyAdjustsMirroring;
```

#### Discussion

For some session configurations, preview will be mirrored by default.

When the value of this property is [`true`](../../Swift/true.md), the value of [`mirrored`](./mirrored.md) may change depending on the configuration of the session, for example after switching to a different capture device input.

## See Also

### Layer configuration
- [orientation](./orientation.md)
  The layer’s orientation.
- [orientationSupported](./orientationsupported.md)
  Indicates whether the layer display supports changing the orientation.
- [mirrored](./mirrored.md)
  Indicates whether the layer display is mirrored.
- [mirroringSupported](./mirroringsupported.md)
  Indicates whether the layer display supports mirroring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/automaticallyadjustsmirroring)*