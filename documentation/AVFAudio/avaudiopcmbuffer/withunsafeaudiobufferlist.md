# withUnsafeAudioBufferList(_:)

**Framework**: AVFAudio  
**Kind**: method

Provides scoped read-only access to the audio buffer list.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func withUnsafeAudioBufferList<R>(_ body: (UnsafePointer<AudioBufferList>) throws -> R) rethrows -> R
```

#### Return Value

The value returned by the closure.

## Parameters

- `body`: A closure that receives a pointer to the audio buffer list.

## See Also

- [func channelData(Int) -> AVAudioPCMBuffer.ChannelData](avaudiopcmbuffer/channeldata(_:).md)
  Returns read-only access to a specific channel’s data.
- [func mutableChannelData(Int) -> AVAudioPCMBuffer.MutableChannelData](avaudiopcmbuffer/mutablechanneldata(_:).md)
  Returns mutable access to a specific channel’s data.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiopcmbuffer/withunsafeaudiobufferlist(_:))*