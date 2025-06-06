# init(pcmFormat:frameCapacity:)

**Framework**: AVFAudio  
**Kind**: init

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

#### Return Value

A new [`AVAudioPCMBuffer`](avaudiopcmbuffer.md) instance, or `nil` if it’s not possible.

#### Discussion

The method returns `nil` due to the following reasons:

- The format has zero bytes per frame.
- The system can’t represent the buffer byte capacity as an unsigned bit-32 integer.

## Parameters

- `format`: The format of the PCM audio the buffer contains.
- `frameCapacity`: The capacity of the buffer in PCM sample frames.

## See Also

- [var frameLength: AVAudioFrameCount](avaudiopcmbuffer/framelength.md)
  The current number of valid sample frames in the buffer.
- [var frameCapacity: AVAudioFrameCount](avaudiopcmbuffer/framecapacity.md)
  The buffer’s capacity, in audio sample frames.
- [init?(pcmFormat: AVAudioFormat, bufferListNoCopy: UnsafePointer<AudioBufferList>, deallocator: ((UnsafePointer<AudioBufferList>) -> Void)?)](avaudiopcmbuffer/init(pcmformat:bufferlistnocopy:deallocator:).md)
  Creates a PCM audio buffer instance without copying samples, for PCM audio data, with a specified buffer list and a deallocator closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiopcmbuffer/init(pcmformat:framecapacity:))*