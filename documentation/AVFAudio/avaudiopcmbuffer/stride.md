# stride

**Framework**: AVFAudio  
**Kind**: property

The buffer’s number of interleaved channels.

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
var stride: Int { get }
```

## See Also

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
- [AVAudioPCMBuffer.ChannelData](avaudiopcmbuffer/channeldata.md)
  Represents read-only channel data.
- [AVAudioPCMBuffer.MutableChannelData](avaudiopcmbuffer/mutablechanneldata.md)
  Represents mutable channel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiopcmbuffer/stride)*