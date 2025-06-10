# AudioReader.Configuration

**Framework**: Create ML Components  
**Kind**: struct

The configuration of the audio reader.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct Configuration
```

## Topics

### Creating a configuration
- [init()](audioreader/configuration-swift.struct/init.md)
  Creates an AudioReader Configuration
- [init(frameCount: Int)](audioreader/configuration-swift.struct/init(framecount:).md)
  Creates an AudioReader Configuration
### Getting the frame count
- [var frameCount: Int](audioreader/configuration-swift.struct/framecount.md)
  The maximum size of each buffer in frames. The default value is `4096`.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [AudioReader.AsyncBuffers](audioreader/asyncbuffers.md)
  An async sequence of audio buffers read from an audio file.
- [AudioReader.MicrophoneAsyncBuffers](audioreader/microphoneasyncbuffers.md)
  An async sequence of audio frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audioreader/configuration-swift.struct)*