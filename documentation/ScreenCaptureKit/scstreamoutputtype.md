# SCStreamOutputType

**Framework**: ScreenCaptureKit  
**Kind**: enum

Constants that represent output types for a stream frame.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 18.2+
- macOS 12.3+
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol SCStreamOutput](scstreamoutput.md)
  A delegate protocol your app implements to receive capture stream output events.
- [struct SCStreamFrameInfo](scstreamframeinfo.md)
  An instance that defines metadata keys for a stream frame.
- [enum SCFrameStatus](scframestatus.md)
  Status values for a frame from a stream.
- [class SCClipBufferingOutput](scclipbufferingoutput.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamoutputtype)*