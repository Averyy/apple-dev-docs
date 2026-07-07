# AVAudioPCMBuffer.ChannelData

**Framework**: AVFAudio  
**Kind**: enum

Represents read-only channel data.

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
enum ChannelData
```

#### Overview

For **deinterleaved** formats:

- The span contains only the requested channel’s samples in contiguous memory

For **interleaved** formats:

- The span contains the entire interleaved buffer starting at the channel’s first sample

## Topics

### Getting typed channel data
- [AVAudioPCMBuffer.ChannelData.float(_:)](avaudiopcmbuffer/channeldata/float(_:).md)
- [AVAudioPCMBuffer.ChannelData.int16(_:)](avaudiopcmbuffer/channeldata/int16(_:).md)
- [AVAudioPCMBuffer.ChannelData.int32(_:)](avaudiopcmbuffer/channeldata/int32(_:).md)

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
- [var stride: Int](avaudiopcmbuffer/stride.md)
  The buffer’s number of interleaved channels.
- [AVAudioPCMBuffer.MutableChannelData](avaudiopcmbuffer/mutablechanneldata.md)
  Represents mutable channel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiopcmbuffer/channeldata)*