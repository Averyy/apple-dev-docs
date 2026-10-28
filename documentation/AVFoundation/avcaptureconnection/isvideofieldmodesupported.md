# isVideoFieldModeSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the connection supports setting a video field mode.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var isVideoFieldModeSupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isVideoFieldModeSupported) BOOL supportsVideoFieldMode;
```

## Discussion

The property only applies to a video connection’s [`videoFieldMode`](./videofieldmode.md) property.

## See Also

### Interlacing video
- [var videoFieldMode: AVVideoFieldMode](./videofieldmode.md)
  A setting that tells the connection how to interlace video flowing through it.
- [enum AVVideoFieldMode](../avvideofieldmode.md)
  Constants that indicate which interlacing modes the connection applies to video flowing through it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/isvideofieldmodesupported)*