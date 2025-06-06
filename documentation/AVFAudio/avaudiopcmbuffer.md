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
- [init?(pcmFormat: AVAudioFormat, frameCapacity: AVAudioFrameCount)](avaudiopcmbuffer/init(pcmformat:framecapacity:).md)
  Creates a PCM audio buffer instance for PCM audio data.
- [init?(pcmFormat: AVAudioFormat, bufferListNoCopy: UnsafePointer<AudioBufferList>, deallocator: ((UnsafePointer<AudioBufferList>) -> Void)?)](avaudiopcmbuffer/init(pcmformat:bufferlistnocopy:deallocator:).md)
  Creates a PCM audio buffer instance without copying samples, for PCM audio data, with a specified buffer list and a deallocator closure.
### Getting and Setting the Frame Length
- [var frameLength: AVAudioFrameCount](avaudiopcmbuffer/framelength.md)
  The current number of valid sample frames in the buffer.
### Accessing PCM Buffer Data
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

## Relationships

### Inherits From
- [AVAudioBuffer](avaudiobuffer.md)
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

- [class AVAudioCompressedBuffer](avaudiocompressedbuffer.md)
  An object that represents an audio buffer that you use for compressed audio formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiopcmbuffer)*