# int32ChannelData

**Framework**: AVFAudio  
**Kind**: property

The buffer’s 32-bit integer audio samples.

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
var int32ChannelData: UnsafePointer<UnsafeMutablePointer<Int32>>? { get }
```

#### Discussion

The `int32ChannelData` property returns the buffer’s audio samples if the buffer’s format has 4-byte integer samples, or `nil` if it’s another format. For more information, see [`floatChannelData`](avaudiopcmbuffer/floatchanneldata.md).

## See Also

- [var floatChannelData: UnsafePointer<UnsafeMutablePointer<Float>>?](avaudiopcmbuffer/floatchanneldata.md)
  The buffer’s audio samples as floating point values.
- [var frameCapacity: AVAudioFrameCount](avaudiopcmbuffer/framecapacity.md)
  The buffer’s capacity, in audio sample frames.
- [var int16ChannelData: UnsafePointer<UnsafeMutablePointer<Int16>>?](avaudiopcmbuffer/int16channeldata.md)
  The buffer’s 16-bit integer audio samples.
- [var stride: Int](avaudiopcmbuffer/stride.md)
  The buffer’s number of interleaved channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiopcmbuffer/int32channeldata)*