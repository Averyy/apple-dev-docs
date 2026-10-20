# videoFieldMode

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A setting that tells the connection how to interlace video flowing through it.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var videoFieldMode: AVVideoFieldMode { get set }
```

```objc
@property (nonatomic) AVVideoFieldMode videoFieldMode;
```

#### Discussion

The property only applies to a video connection and when [`isVideoFieldModeSupported`](./isvideofieldmodesupported.md) is [`true`](../../Swift/true.md).

## See Also

### Interlacing video
- [var isVideoFieldModeSupported: Bool](./isvideofieldmodesupported.md)
  A Boolean value that indicates whether the connection supports setting a video field mode.
- [enum AVVideoFieldMode](../avvideofieldmode.md)
  Constants that indicate which interlacing modes the connection applies to video flowing through it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/videofieldmode)*