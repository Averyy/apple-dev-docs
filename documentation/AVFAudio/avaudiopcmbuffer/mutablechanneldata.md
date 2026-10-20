# AVAudioPCMBuffer.MutableChannelData

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Represents mutable channel data.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum MutableChannelData
```

#### Overview

For **deinterleaved** formats:

- The span contains only the requested channel’s samples in contiguous memory

For **interleaved** formats:

- The span contains the entire interleaved buffer starting at the channel’s first sample

## Topics

### Getting typed mutable channel data
- [AVAudioPCMBuffer.MutableChannelData.float(_:)](./mutablechanneldata/float%28_%29.md)
- [AVAudioPCMBuffer.MutableChannelData.int16(_:)](./mutablechanneldata/int16%28_%29.md)
- [AVAudioPCMBuffer.MutableChannelData.int32(_:)](./mutablechanneldata/int32%28_%29.md)

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
- [var int16ChannelData: UnsafePointer<UnsafeMutablePointer<Int16>>?](./int16channeldata.md)
  The buffer’s 16-bit integer audio samples.
- [var int32ChannelData: UnsafePointer<UnsafeMutablePointer<Int32>>?](./int32channeldata.md)
  The buffer’s 32-bit integer audio samples.
- [var stride: Int](./stride.md)
  The buffer’s number of interleaved channels.
- [AVAudioPCMBuffer.ChannelData](./channeldata.md)
  Represents read-only channel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiopcmbuffer/mutablechanneldata)*