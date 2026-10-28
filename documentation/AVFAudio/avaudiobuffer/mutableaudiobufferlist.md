# mutableAudioBufferList

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) AudioBufferList * mutableAudioBufferList;
```

## Discussion

You use this with some lower-level Core Audio and Audio Toolbox APIs that require a mutable [`AudioBufferList`](../../CoreAudioTypes/audiobufferlist.md) (for example, the [`AudioConverterConvertComplexBuffer(_:_:_:_:)`](../../AudioToolbox/audioconverterconvertcomplexbuffer%28_,_,_,_%29.md) function).

The `mDataByteSize` fields of this audio buffer list express the buffer’s current [`frameCapacity`](../avaudiopcmbuffer/framecapacity.md). If you alter the capacity, modify the buffer’s `frameLength` to match.

## See Also

### Getting the audio buffers
- [var audioBufferList: UnsafePointer<AudioBufferList>](./audiobufferlist.md)
  The buffer’s underlying audio buffer list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiobuffer/mutableaudiobufferlist)*