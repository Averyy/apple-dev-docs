# AudioReader.Configuration

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

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
- [init()](./configuration-swift.struct/init%28%29.md)
  Creates an AudioReader Configuration
- [init(frameCount: Int)](./configuration-swift.struct/init%28framecount%29.md)
  Creates an AudioReader Configuration
### Getting the frame count
- [var frameCount: Int](./configuration-swift.struct/framecount.md)
  The maximum size of each buffer in frames. The default value is `4096`.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing buffers
- [AudioReader.AsyncBuffers](./asyncbuffers.md)
  An async sequence of audio buffers read from an audio file.
- [AudioReader.MicrophoneAsyncBuffers](./microphoneasyncbuffers.md)
  An async sequence of audio frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audioreader/configuration-swift.struct)*