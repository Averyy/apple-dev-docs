# frameCapacity

**Framework**: AVFAudio  
**Kind**: property

The buffer’s capacity, in audio sample frames.

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
var frameCapacity: AVAudioFrameCount { get }
```

## See Also

- [var floatChannelData: UnsafePointer<UnsafeMutablePointer<Float>>?](avaudiopcmbuffer/floatchanneldata.md)
  The buffer’s audio samples as floating point values.
- [var int16ChannelData: UnsafePointer<UnsafeMutablePointer<Int16>>?](avaudiopcmbuffer/int16channeldata.md)
  The buffer’s 16-bit integer audio samples.
- [var int32ChannelData: UnsafePointer<UnsafeMutablePointer<Int32>>?](avaudiopcmbuffer/int32channeldata.md)
  The buffer’s 32-bit integer audio samples.
- [var stride: Int](avaudiopcmbuffer/stride.md)
  The buffer’s number of interleaved channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiopcmbuffer/framecapacity)*