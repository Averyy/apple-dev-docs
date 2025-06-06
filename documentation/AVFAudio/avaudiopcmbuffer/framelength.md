# frameLength

**Framework**: AVFAudio  
**Kind**: property

The current number of valid sample frames in the buffer.

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
var frameLength: AVAudioFrameCount { get set }
```

#### Discussion

By default, the `frameLength` property doesn’t have a useful value upon creation, so you must set this property before using the buffer. The length must be less than or equal to the [`frameCapacity`](avaudiopcmbuffer/framecapacity.md) of the buffer. For deinterleaved formats, [`frameCapacity`](avaudiopcmbuffer/framecapacity.md) refers to the size of one channel’s worth of audio samples.

You may modify the length of the buffer as part of an operation that modifies its contents. Modifying `frameLength` updates the `mDataByteSize` field in each of the underlying [`AudioBufferList`](https://developer.apple.com/documentation/CoreAudioTypes/AudioBufferList) structure’s `AudioBuffer` properties correspondingly, and vice versa.

## See Also

- [var frameCapacity: AVAudioFrameCount](avaudiopcmbuffer/framecapacity.md)
  The buffer’s capacity, in audio sample frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiopcmbuffer/framelength)*