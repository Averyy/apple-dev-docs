# AudioReader.MicrophoneAsyncBuffers

**Framework**: Create ML Components  
**Kind**: struct

An async sequence of audio frames.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct MicrophoneAsyncBuffers
```

#### Overview

This sequence allows iterating through the microphone audio frames.

## Topics

### Getting the count
- [var count: Int?](audioreader/microphoneasyncbuffers/count.md)
  The number of audio buffers. For this sequence count is always nil.
### Creating an iterator
- [func makeAsyncIterator() -> AudioReader.MicrophoneAsyncBuffers.Iterator](audioreader/microphoneasyncbuffers/makeasynciterator.md)
  Constructs an iterator.
- [AudioReader.MicrophoneAsyncBuffers.Iterator](audioreader/microphoneasyncbuffers/iterator.md)
  An async iterator of audio frames.
- [AudioReader.MicrophoneAsyncBuffers.AsyncIterator](audioreader/microphoneasyncbuffers/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [AudioReader.MicrophoneAsyncBuffers.Feature](audioreader/microphoneasyncbuffers/feature.md)
  The feature type.
### Type Aliases
- [AudioReader.MicrophoneAsyncBuffers.Element](audioreader/microphoneasyncbuffers/element.md)
  The type of element produced by this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](audioreader/microphoneasyncbuffers/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TemporalSequence](temporalsequence.md)

## See Also

- [AudioReader.AsyncBuffers](audioreader/asyncbuffers.md)
  An async sequence of audio buffers read from an audio file.
- [AudioReader.Configuration](audioreader/configuration-swift.struct.md)
  The configuration of the audio reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audioreader/microphoneasyncbuffers)*