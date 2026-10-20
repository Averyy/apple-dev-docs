# floatChannelData

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) float * const* floatChannelData;
```

#### Discussion

The `floatChannelData` property returns pointers to the buffer’s audio samples if the buffer’s format is 32-bit float. It returns `nil` if it’s another format.

The returned pointer is to `format.channelCount` pointers to float. Each of these pointers is to [`frameLength`](./framelength.md) valid samples, which the class spaces by [`stride`](./stride.md) samples.

If the format isn’t interleaved, as with the standard deinterleaved float format, the pointers point to separate chunks of memory, and the [`stride`](./stride.md) property value is `1`.

When the format is in an interleaved state, the pointers refer to the same buffer of interleaved samples, each offset by `1` frame, and the [`stride`](./stride.md) property value is the number of interleaved channels.

## See Also

### Accessing PCM buffer data
- [func channelData(Int) -> AVAudioPCMBuffer.ChannelData](./channeldata%28_%29.md)
  Returns read-only access to a specific channel’s data.
- [func mutableChannelData(Int) -> AVAudioPCMBuffer.MutableChannelData](./mutablechanneldata%28_%29.md)
  Returns mutable access to a specific channel’s data.
- [func withUnsafeAudioBufferList<R>((UnsafePointer<AudioBufferList>) throws -> R) rethrows -> R](./withunsafeaudiobufferlist%28_%29.md)
  Provides scoped read-only access to the audio buffer list.
- [var frameCapacity: AVAudioFrameCount](./framecapacity.md)
  The buffer’s capacity, in audio sample frames.
- [var int16ChannelData: UnsafePointer<UnsafeMutablePointer<Int16>>?](./int16channeldata.md)
  The buffer’s 16-bit integer audio samples.
- [var int32ChannelData: UnsafePointer<UnsafeMutablePointer<Int32>>?](./int32channeldata.md)
  The buffer’s 32-bit integer audio samples.
- [var stride: Int](./stride.md)
  The buffer’s number of interleaved channels.
- [AVAudioPCMBuffer.ChannelData](./channeldata.md)
  Represents read-only channel data.
- [AVAudioPCMBuffer.MutableChannelData](./mutablechanneldata.md)
  Represents mutable channel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiopcmbuffer/floatchanneldata)*