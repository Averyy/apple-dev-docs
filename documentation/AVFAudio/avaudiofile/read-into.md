# read(into:)

**Framework**: AVFAudio  
**Kind**: method

Reads an entire audio buffer.

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
func read(into buffer: AVAudioPCMBuffer) throws
```

#### Discussion

When reading sequentially from the [`framePosition`](avaudiofile/frameposition.md) property, the method attempts to fill the buffer to its capacity. On return, the buffer’s [`length`](avaudiofile/length.md) property indicates the number of sample frames it successfully reads.

## Parameters

- `buffer`: The buffer from which to read the file. Its format must match the file’s processing format.

## See Also

- [var framePosition: AVAudioFramePosition](avaudiofile/frameposition.md)
  The position in the file where the next read or write operation occurs.
- [var length: AVAudioFramePosition](avaudiofile/length.md)
  The number of sample frames in the file.
- [func read(into: AVAudioPCMBuffer, frameCount: AVAudioFrameCount) throws](avaudiofile/read(into:framecount:).md)
  Reads a portion of an audio buffer using the number of frames you specify.
- [func write(from: AVAudioPCMBuffer) throws](avaudiofile/write(from:).md)
  Writes an audio buffer sequentially.
- [func close()](avaudiofile/close.md)
  Closes the audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiofile/read(into:))*