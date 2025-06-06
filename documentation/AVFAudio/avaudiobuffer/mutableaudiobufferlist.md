# mutableAudioBufferList

**Framework**: AVFAudio  
**Kind**: property

A mutable version of the buffer’s underlying audio buffer list.

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
var mutableAudioBufferList: UnsafeMutablePointer<AudioBufferList> { get }
```

#### Discussion

You use this with some lower-level Core Audio and Audio Toolbox APIs that require a mutable [`AudioBufferList`](https://developer.apple.com/documentation/CoreAudioTypes/AudioBufferList) (for example, the [`AudioConverterConvertComplexBuffer(_:_:_:_:)`](https://developer.apple.com/documentation/AudioToolbox/AudioConverterConvertComplexBuffer(_:_:_:_:)) function).

The `mDataByteSize` fields of this audio buffer list express the buffer’s current [`frameCapacity`](avaudiopcmbuffer/framecapacity.md). If you alter the capacity, modify the buffer’s `frameLength` to match.

## See Also

- [var audioBufferList: UnsafePointer<AudioBufferList>](avaudiobuffer/audiobufferlist.md)
  The buffer’s underlying audio buffer list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiobuffer/mutableaudiobufferlist)*