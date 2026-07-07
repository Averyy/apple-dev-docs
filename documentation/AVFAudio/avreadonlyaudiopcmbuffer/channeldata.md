# AVReadOnlyAudioPCMBuffer.ChannelData

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
- [AVReadOnlyAudioPCMBuffer.ChannelData.float(_:)](avreadonlyaudiopcmbuffer/channeldata/float(_:).md)
- [AVReadOnlyAudioPCMBuffer.ChannelData.int16(_:)](avreadonlyaudiopcmbuffer/channeldata/int16(_:).md)
- [AVReadOnlyAudioPCMBuffer.ChannelData.int32(_:)](avreadonlyaudiopcmbuffer/channeldata/int32(_:).md)

## See Also

- [func channelData(Int) -> AVReadOnlyAudioPCMBuffer.ChannelData](avreadonlyaudiopcmbuffer/channeldata(_:).md)
  Returns read-only access to a specific channel’s data.
- [func withUnsafeAudioBufferList<R>((UnsafePointer<AudioBufferList>) throws -> R) rethrows -> R](avreadonlyaudiopcmbuffer/withunsafeaudiobufferlist(_:).md)
  Provides scoped read-only access to the audio buffer list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avreadonlyaudiopcmbuffer/channeldata)*