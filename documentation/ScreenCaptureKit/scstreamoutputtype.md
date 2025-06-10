# SCStreamOutputType

**Framework**: ScreenCaptureKit  
**Kind**: enum

Constants that represent output types for a stream frame.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
enum SCStreamOutputType
```

## Topics

### Output types
- [SCStreamOutputType.screen](scstreamoutputtype/screen.md)
  An output type that represents a screen capture sample buffer.
- [SCStreamOutputType.audio](scstreamoutputtype/audio.md)
  An output type that represents an audio capture sample buffer.
### Enumeration Cases
- [SCStreamOutputType.microphone](scstreamoutputtype/microphone.md)
### Initializers
- [init?(rawValue: Int)](scstreamoutputtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol SCStreamOutput](scstreamoutput.md)
  A delegate protocol your app implements to receive capture stream output events.
- [struct SCStreamFrameInfo](scstreamframeinfo.md)
  An instance that defines metadata keys for a stream frame.
- [enum SCFrameStatus](scframestatus.md)
  Status values for a frame from a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamoutputtype)*