# write(from:)

**Framework**: AVFAudio  
**Kind**: method

Writes an audio buffer sequentially.

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
func write(from buffer: AVAudioPCMBuffer) throws
```

#### Discussion

The buffer’s [`frameLength`](avaudiopcmbuffer/framelength.md) signifies how much of the buffer the method writes.

## Parameters

- `buffer`: The buffer from which to write to the file. Its format must match the file’s processing format.

## See Also

- [func read(into: AVAudioPCMBuffer) throws](avaudiofile/read(into:).md)
  Reads an entire audio buffer.
- [func read(into: AVAudioPCMBuffer, frameCount: AVAudioFrameCount) throws](avaudiofile/read(into:framecount:).md)
  Reads a portion of an audio buffer using the number of frames you specify.
- [func close()](avaudiofile/close.md)
  Closes the audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiofile/write(from:))*