# AVAudioPCMBuffer

**Framework**: AVFAudio  
**Kind**: class

An object that represents an audio buffer you use with PCM audio formats.

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
class AVAudioPCMBuffer
```

#### Overview

The PCM buffer class provides methods that are useful for manipulating buffers of audio in PCM format.

## Topics

### Creating a PCM Audio Buffer
- [init?(pcmFormat: AVAudioFormat, frameCapacity: AVAudioFrameCount)](avaudiopcmbuffer/init(pcmformat:framecapacity:)-5jhd5.md)
  Creates a PCM audio buffer instance for PCM audio data.
- [init?(pcmFormat: AVAudioFormat, bufferListNoCopy: UnsafePointer<AudioBufferList>, deallocator: ((UnsafePointer<AudioBufferList>) -> Void)?)](avaudiopcmbuffer/init(pcmformat:bufferlistnocopy:deallocator:)-9iwe7.md)
  Creates a PCM audio buffer instance without copying samples, for PCM audio data, with a specified buffer list and a deallocator closure.
### Getting and Setting the Frame Length
- [var frameLength: AVAudioFrameCount](avaudiopcmbuffer/framelength.md)
  The current number of valid sample frames in the buffer.
### Accessing PCM Buffer Data
- [func channelData(Int) -> AVAudioPCMBuffer.ChannelData](avaudiopcmbuffer/channeldata(_:).md)
  Returns read-only access to a specific channel’s data.
- [func mutableChannelData(Int) -> AVAudioPCMBuffer.MutableChannelData](avaudiopcmbuffer/mutablechanneldata(_:).md)
  Returns mutable access to a specific channel’s data.
- [func withUnsafeAudioBufferList<R>((UnsafePointer<AudioBufferList>) throws -> R) rethrows -> R](avaudiopcmbuffer/withunsafeaudiobufferlist(_:).md)
  Provides scoped read-only access to the audio buffer list.
- [var floatChannelData: UnsafePointer<UnsafeMutablePointer<Float>>?](avaudiopcmbuffer/floatchanneldata.md)
  The buffer’s audio samples as floating point values.
- [var frameCapacity: AVAudioFrameCount](avaudiopcmbuffer/framecapacity.md)
  The buffer’s capacity, in audio sample frames.
- [var int16ChannelData: UnsafePointer<UnsafeMutablePointer<Int16>>?](avaudiopcmbuffer/int16channeldata.md)
  The buffer’s 16-bit integer audio samples.
- [var int32ChannelData: UnsafePointer<UnsafeMutablePointer<Int32>>?](avaudiopcmbuffer/int32channeldata.md)
  The buffer’s 32-bit integer audio samples.
- [var stride: Int](avaudiopcmbuffer/stride.md)
  The buffer’s number of interleaved channels.
- [AVAudioPCMBuffer.ChannelData](avaudiopcmbuffer/channeldata.md)
  Represents read-only channel data.
- [AVAudioPCMBuffer.MutableChannelData](avaudiopcmbuffer/mutablechanneldata.md)
  Represents mutable channel data.
### Initializers
- [init?(PCMFormat: AVAudioFormat, bufferListNoCopy: UnsafePointer<AudioBufferList>, deallocator: ((UnsafePointer<AudioBufferList>) -> Void)?)](avaudiopcmbuffer/init(pcmformat:bufferlistnocopy:deallocator:)-2ms1j.md)
- [init?(PCMFormat: AVAudioFormat, frameCapacity: AVAudioFrameCount)](avaudiopcmbuffer/init(pcmformat:framecapacity:)-7scyk.md)
- [convenience init(copying: AVAudioPCMBuffer)](avaudiopcmbuffer/init(copying:)-68es5.md)
  Creates a mutable buffer by copying another PCM buffer’s audio data.
- [convenience init(copying: AVReadOnlyAudioPCMBuffer)](avaudiopcmbuffer/init(copying:)-875xm.md)
  Creates a mutable buffer by copying a read-only buffer’s audio data.

## Relationships

### Inherits From
- [AVAudioBuffer](avaudiobuffer.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSMutableCopying](../foundation/nsmutablecopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class AVAudioBuffer](avaudiobuffer.md)
  An object that represents a buffer of audio data with a format.
- [struct AVReadOnlyAudioPCMBuffer](avreadonlyaudiopcmbuffer.md)
  A read-only, Sendable audio buffer for safe concurrent access.
- [class AVAudioFile](avaudiofile.md)
  An object that represents an audio file that the system can open for reading or writing.
- [class AVAudioTime](avaudiotime.md)
  An object you use to represent a moment in time.
- [Audio settings](audio-settings.md)
  Configure audio processing settings using standard key and value constants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiopcmbuffer)*