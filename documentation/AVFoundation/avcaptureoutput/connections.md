# connections

**Framework**: AVFoundation  
**Kind**: property

The capture output object’s connections.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var connections: [AVCaptureConnection] { get }
```

#### Discussion

Each connection object in the array describes the mapping between the output and the capture input ports.

## See Also

- [func connection(with: AVMediaType) -> AVCaptureConnection?](avcaptureoutput/connection(with:).md)
  Returns the first connection with an input port of a specified media type.
- [AVCaptureOutput.DataDroppedReason](avcaptureoutput/datadroppedreason.md)
  Constants that define reasons for why the system dropped a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureoutput/connections)*