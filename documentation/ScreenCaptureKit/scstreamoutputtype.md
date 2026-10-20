# SCStreamOutputType

**Framework**: ScreenCaptureKit  
**Kind**: enum  
**Role**: Enumeration

Constants that represent output types for a stream frame.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 12.3+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum SCStreamOutputType
```

```c
enum SCStreamOutputType : NSInteger;
```

## Topics

### Output types
- [SCStreamOutputType.screen](./scstreamoutputtype/screen.md)
  An output type that represents a screen capture sample buffer.
- [SCStreamOutputType.audio](./scstreamoutputtype/audio.md)
  An output type that represents an audio capture sample buffer.
### Enumeration Cases
- [SCStreamOutputType.microphone](./scstreamoutputtype/microphone.md)
### Initializers
- [init?(rawValue: Int)](./scstreamoutputtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Output processing
- [protocol SCStreamOutput](./scstreamoutput.md)
  A delegate protocol your app implements to receive capture stream output events.
- [struct SCStreamFrameInfo](./scstreamframeinfo.md)
  An instance that defines metadata keys for a stream frame.
- [enum SCFrameStatus](./scframestatus.md)
  Status values for a frame from a stream.
- [class SCClipBufferingOutput](./scclipbufferingoutput.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamoutputtype)*