# write(from:)

**Framework**: AVFAudio  
**Kind**: method

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

Write a buffer.

Writes sequentially. The buffer’s frameLength signifies how much of the buffer is to be written.

## Parameters

- `buffer`: The buffer from which to write to the file. Its format must match the file’s processing format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiofile/write(from:)-6qgec)*