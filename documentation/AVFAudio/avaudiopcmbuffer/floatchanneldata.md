# floatChannelData

**Framework**: AVFAudio  
**Kind**: property

The buffer’s audio samples as floating point values.

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
var floatChannelData: UnsafePointer<UnsafeMutablePointer<Float>>? { get }
```

#### Discussion

The `floatChannelData` property returns pointers to the buffer’s audio samples if the buffer’s format is 32-bit float. It returns `nil` if it’s another format.

The returned pointer is to `format.channelCount` pointers to float. Each of these pointers is to [`frameLength`](avaudiopcmbuffer/framelength.md) valid samples, which the class spaces by [`stride`](avaudiopcmbuffer/stride.md) samples.

If the format isn’t interleaved, as with the standard deinterleaved float format, the pointers point to separate chunks of memory, and the [`stride`](avaudiopcmbuffer/stride.md) property value is `1`.

When the format is in an interleaved state, the pointers refer to the same buffer of interleaved samples, each offset by `1` frame, and the [`stride`](avaudiopcmbuffer/stride.md) property value is the number of interleaved channels.

## See Also

- [func channelData(Int) -> AVAudioPCMBuffer.ChannelData](avaudiopcmbuffer/channeldata(_:).md)
  Returns read-only access to a specific channel’s data.
- [func mutableChannelData(Int) -> AVAudioPCMBuffer.MutableChannelData](avaudiopcmbuffer/mutablechanneldata(_:).md)
  Returns mutable access to a specific channel’s data.
- [func withUnsafeAudioBufferList<R>((UnsafePointer<AudioBufferList>) throws -> R) rethrows -> R](avaudiopcmbuffer/withunsafeaudiobufferlist(_:).md)
  Provides scoped read-only access to the audio buffer list.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiopcmbuffer/floatchanneldata)*