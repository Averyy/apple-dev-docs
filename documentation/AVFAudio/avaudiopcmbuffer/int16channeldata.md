# int16ChannelData

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The buffer’s 16-bit integer audio samples.

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
var int16ChannelData: UnsafePointer<UnsafeMutablePointer<Int16>>? { get }
```

```objc
@property (nonatomic, readonly) int16_t * const* int16ChannelData;
```

#### Discussion

The `int16ChannelData` property returns the buffer’s audio samples if the buffer’s format has 2-byte integer samples, or `nil` if it’s another format. For more information, see [`floatChannelData`](./floatchanneldata.md).

## See Also

### Accessing PCM buffer data
- [func channelData(Int) -> AVAudioPCMBuffer.ChannelData](./channeldata%28_%29.md)
  Returns read-only access to a specific channel’s data.
- [func mutableChannelData(Int) -> AVAudioPCMBuffer.MutableChannelData](./mutablechanneldata%28_%29.md)
  Returns mutable access to a specific channel’s data.
- [func withUnsafeAudioBufferList<R>((UnsafePointer<AudioBufferList>) throws -> R) rethrows -> R](./withunsafeaudiobufferlist%28_%29.md)
  Provides scoped read-only access to the audio buffer list.
- [var floatChannelData: UnsafePointer<UnsafeMutablePointer<Float>>?](./floatchanneldata.md)
  The buffer’s audio samples as floating point values.
- [var frameCapacity: AVAudioFrameCount](./framecapacity.md)
  The buffer’s capacity, in audio sample frames.
- [var int32ChannelData: UnsafePointer<UnsafeMutablePointer<Int32>>?](./int32channeldata.md)
  The buffer’s 32-bit integer audio samples.
- [var stride: Int](./stride.md)
  The buffer’s number of interleaved channels.
- [AVAudioPCMBuffer.ChannelData](./channeldata.md)
  Represents read-only channel data.
- [AVAudioPCMBuffer.MutableChannelData](./mutablechanneldata.md)
  Represents mutable channel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiopcmbuffer/int16channeldata)*