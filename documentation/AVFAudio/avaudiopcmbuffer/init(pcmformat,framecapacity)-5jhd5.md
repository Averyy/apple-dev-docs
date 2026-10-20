# init(pcmFormat:frameCapacity:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

Creates a PCM audio buffer instance for PCM audio data.

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
init?(pcmFormat format: AVAudioFormat, frameCapacity: AVAudioFrameCount)
```

```objc
- (instancetype) initWithPCMFormat:(AVAudioFormat *) format frameCapacity:(AVAudioFrameCount) frameCapacity;
```

#### Return Value

A new [`AVAudioPCMBuffer`](../avaudiopcmbuffer.md) instance, or `nil` if it’s not possible.

#### Discussion

The method returns `nil` due to the following reasons:

- The format has zero bytes per frame.
- The system can’t represent the buffer byte capacity as an unsigned 32-bit integer.

## Parameters

- `format`: The format of the PCM audio the buffer contains.
- `frameCapacity`: The capacity of the buffer in PCM sample frames.

## See Also

### Related Documentation
- [var frameLength: AVAudioFrameCount](./framelength.md)
  The current number of valid sample frames in the buffer.
- [var frameCapacity: AVAudioFrameCount](./framecapacity.md)
  The buffer’s capacity, in audio sample frames.
### Creating a PCM audio buffer
- [init?(pcmFormat: AVAudioFormat, bufferListNoCopy: UnsafePointer<AudioBufferList>, deallocator: ((UnsafePointer<AudioBufferList>) -> Void)?)](./init%28pcmformat,bufferlistnocopy,deallocator%29-9iwe7.md)
  Creates a PCM audio buffer instance without copying samples, for PCM audio data, with a specified buffer list and a deallocator closure.
- [convenience init(copying: AVAudioPCMBuffer)](./init%28copying%29-68es5.md)
  Creates a mutable buffer by copying another PCM buffer’s audio data.
- [convenience init(copying: AVReadOnlyAudioPCMBuffer)](./init%28copying%29-875xm.md)
  Creates a mutable buffer by copying a read-only buffer’s audio data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiopcmbuffer/init(pcmformat:framecapacity:)-5jhd5)*