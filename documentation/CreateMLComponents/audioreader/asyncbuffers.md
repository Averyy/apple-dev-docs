# AudioReader.AsyncBuffers

**Framework**: Create ML Components  
**Kind**: struct

An async sequence of audio buffers read from an audio file.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct AsyncBuffers
```

#### Overview

This sequence allows iterating through the file only once.

## Topics

### Getting the count
- [let count: Int?](audioreader/asyncbuffers/count.md)
  The number of audio buffers in the file.
### Getting the url
- [let url: URL](audioreader/asyncbuffers/url.md)
  The audio file URL, used when throwing an error.
### Creating an iterator
- [func makeAsyncIterator() -> AudioReader.AsyncBuffers.Iterator](audioreader/asyncbuffers/makeasynciterator.md)
  Constructs an iterator.
- [AudioReader.AsyncBuffers.Iterator](audioreader/asyncbuffers/iterator.md)
  An async iterator of audio buffers.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [TemporalSequence](temporalsequence.md)

## See Also

- [AudioReader.Configuration](audioreader/configuration-swift.struct.md)
  The configuration of the audio reader.
- [AudioReader.MicrophoneAsyncBuffers](audioreader/microphoneasyncbuffers.md)
  An async sequence of audio frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audioreader/asyncbuffers)*