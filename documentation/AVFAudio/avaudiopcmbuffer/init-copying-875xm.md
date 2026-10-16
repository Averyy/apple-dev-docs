# init(copying:)

**Framework**: AVFAudio  
**Kind**: init

Creates a mutable buffer by copying a read-only buffer’s audio data.

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
convenience init(copying readOnlyBuffer: AVReadOnlyAudioPCMBuffer)
```

#### Discussion

This initializer allocates a new mutable buffer and copies all audio data from the read-only buffer.

## Parameters

- `readOnlyBuffer`: The read-only buffer to copy from.

## See Also

- [init?(pcmFormat: AVAudioFormat, frameCapacity: AVAudioFrameCount)](avaudiopcmbuffer/init(pcmformat:framecapacity:)-5jhd5.md)
  Creates a PCM audio buffer instance for PCM audio data.
- [init?(pcmFormat: AVAudioFormat, bufferListNoCopy: UnsafePointer<AudioBufferList>, deallocator: ((UnsafePointer<AudioBufferList>) -> Void)?)](avaudiopcmbuffer/init(pcmformat:bufferlistnocopy:deallocator:)-9iwe7.md)
  Creates a PCM audio buffer instance without copying samples, for PCM audio data, with a specified buffer list and a deallocator closure.
- [convenience init(copying: AVAudioPCMBuffer)](avaudiopcmbuffer/init(copying:)-68es5.md)
  Creates a mutable buffer by copying another PCM buffer’s audio data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiopcmbuffer/init(copying:)-875xm)*