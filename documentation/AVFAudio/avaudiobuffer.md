# AVAudioBuffer

**Framework**: AVFAudio  
**Kind**: class

An object that represents a buffer of audio data with a format.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class AVAudioBuffer
```

## Topics

### Getting the Buffer Format
- [var format: AVAudioFormat](avaudiobuffer/format.md)
  The format of the audio in the buffer.
### Getting the Audio Buffers
- [var audioBufferList: UnsafePointer<AudioBufferList>](avaudiobuffer/audiobufferlist.md)
  The buffer’s underlying audio buffer list.
- [var mutableAudioBufferList: UnsafeMutablePointer<AudioBufferList>](avaudiobuffer/mutableaudiobufferlist.md)
  A mutable version of the buffer’s underlying audio buffer list.
### Specialized Audio Buffers
- [class AVAudioCompressedBuffer](avaudiocompressedbuffer.md)
  An object that represents an audio buffer that you use for compressed audio formats.
- [class AVAudioPCMBuffer](avaudiopcmbuffer.md)
  An object that represents an audio buffer you use with PCM audio formats.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVAudioCompressedBuffer](avaudiocompressedbuffer.md)
- [AVAudioPCMBuffer](avaudiopcmbuffer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVAudioFile](avaudiofile.md)
  An object that represents an audio file that the system can open for reading or writing.
- [class AVAudioTime](avaudiotime.md)
  An object you use to represent a moment in time.
- [Audio settings](audio-settings.md)
  Configure audio processing settings using standard key and value constants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiobuffer)*