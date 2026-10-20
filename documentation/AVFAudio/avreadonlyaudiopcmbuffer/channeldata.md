# AVReadOnlyAudioPCMBuffer.ChannelData

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Represents read-only channel data.

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
enum ChannelData
```

#### Overview

For **deinterleaved** formats:

- The span contains only the requested channel’s samples in contiguous memory

For **interleaved** formats:

- The span contains the entire interleaved buffer starting at the channel’s first sample

## Topics

### Getting typed channel data
- [AVReadOnlyAudioPCMBuffer.ChannelData.float(_:)](./channeldata/float%28_%29.md)
- [AVReadOnlyAudioPCMBuffer.ChannelData.int16(_:)](./channeldata/int16%28_%29.md)
- [AVReadOnlyAudioPCMBuffer.ChannelData.int32(_:)](./channeldata/int32%28_%29.md)

## See Also

### Accessing channel data
- [func channelData(Int) -> AVReadOnlyAudioPCMBuffer.ChannelData](./channeldata%28_%29.md)
  Returns read-only access to a specific channel’s data.
- [func withUnsafeAudioBufferList<R>((UnsafePointer<AudioBufferList>) throws -> R) rethrows -> R](./withunsafeaudiobufferlist%28_%29.md)
  Provides scoped read-only access to the audio buffer list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avreadonlyaudiopcmbuffer/channeldata)*