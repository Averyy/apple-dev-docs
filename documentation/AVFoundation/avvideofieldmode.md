# AVVideoFieldMode

**Framework**: AVFoundation  
**Kind**: enum

Constants that indicate which interlacing modes the connection applies to video flowing through it.

**Availability**:
- macOS 10.7+

## Declaration

```swift
enum AVVideoFieldMode
```

#### Overview

The values apply to the [`videoFieldMode`](avcaptureconnection/videofieldmode.md) property.

## Topics

### Constants
- [AVVideoFieldMode.both](avvideofieldmode/both.md)
  A value that indicates that a video connection passes both the top and bottom video fields.
- [AVVideoFieldMode.topOnly](avvideofieldmode/toponly.md)
  A value that indicates that a video connection only passes the top video field.
- [AVVideoFieldMode.bottomOnly](avvideofieldmode/bottomonly.md)
  A value that indicates that a video connection only passes the bottom video field.
- [AVVideoFieldMode.deinterlace](avvideofieldmode/deinterlace.md)
  A value that indicates that a video connection deinterlaces the top and bottom video fields.
### Initializers
- [init?(rawValue: Int)](avvideofieldmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var isVideoFieldModeSupported: Bool](avcaptureconnection/isvideofieldmodesupported.md)
  A Boolean value that indicates whether the connection supports setting a video field mode.
- [var videoFieldMode: AVVideoFieldMode](avcaptureconnection/videofieldmode.md)
  A setting that tells the connection how to interlace video flowing through it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideofieldmode)*