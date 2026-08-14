# AVReadOnlyAudioPCMBuffer

**Framework**: AVFAudio  
**Kind**: struct

A read-only, Sendable audio buffer for safe concurrent access.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct AVReadOnlyAudioPCMBuffer
```

## Topics

### Creating a read-only buffer
- [init(copying: AVAudioPCMBuffer)](avreadonlyaudiopcmbuffer/init(copying:).md)
  Creates a read-only buffer by copying audio data from an existing PCM buffer.
- [init(format: AVAudioFormat, frameCapacity: Int, initializingWith: (UnsafeMutablePointer<AudioBufferList>) throws -> Void) throws](avreadonlyaudiopcmbuffer/init(format:framecapacity:initializingwith:).md)
  Creates a read-only buffer by allocating and initializing audio data via closure.
- [init(unsafeRetaining: sending AVAudioPCMBuffer)](avreadonlyaudiopcmbuffer/init(unsaferetaining:).md)
  Creates a read-only buffer by retaining the existing PCM buffer without copying.
### Getting buffer properties
- [var format: AVAudioFormat](avreadonlyaudiopcmbuffer/format.md)
- [var frameCapacity: Int](avreadonlyaudiopcmbuffer/framecapacity.md)
- [var frameLength: Int](avreadonlyaudiopcmbuffer/framelength.md)
- [var stride: Int](avreadonlyaudiopcmbuffer/stride.md)
### Accessing channel data
- [func channelData(Int) -> AVReadOnlyAudioPCMBuffer.ChannelData](avreadonlyaudiopcmbuffer/channeldata(_:).md)
  Returns read-only access to a specific channel’s data.
- [func withUnsafeAudioBufferList<R>((UnsafePointer<AudioBufferList>) throws -> R) rethrows -> R](avreadonlyaudiopcmbuffer/withunsafeaudiobufferlist(_:).md)
  Provides scoped read-only access to the audio buffer list.
- [AVReadOnlyAudioPCMBuffer.ChannelData](avreadonlyaudiopcmbuffer/channeldata.md)
  Represents read-only channel data.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class AVAudioBuffer](avaudiobuffer.md)
  An object that represents a buffer of audio data with a format.
- [class AVAudioPCMBuffer](avaudiopcmbuffer.md)
  An object that represents an audio buffer you use with PCM audio formats.
- [class AVAudioFile](avaudiofile.md)
  An object that represents an audio file that the system can open for reading or writing.
- [class AVAudioTime](avaudiotime.md)
  An object you use to represent a moment in time.
- [Audio settings](audio-settings.md)
  Configure audio processing settings using standard key and value constants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avreadonlyaudiopcmbuffer)*