# AudioFeaturePrint.FeatureSequence

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

An async sequence of audio buffers.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct FeatureSequence
```

## Topics

### Getting the count
- [var count: Int?](./featuresequence/count.md)
  The number of elements in the sequence. For this sequence count is always nil.
### Creating an iterator
- [func makeAsyncIterator() -> AudioFeaturePrint.FeatureSequence.AsyncIterator](./featuresequence/makeasynciterator%28%29.md)
  Constructs an iterator.
- [AudioFeaturePrint.FeatureSequence.Iterator](./featuresequence/iterator.md)
  An async iterator of audio buffers.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)
- [TemporalSequence](../temporalsequence.md)

## See Also

### Performing the transformation
- [func applied<S>(to: S, eventHandler: EventHandler?) throws -> AudioFeaturePrint.FeatureSequence](./applied%28to,eventhandler%29.md)
  Extracts audio features from an a sequence of audio buffers


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audiofeatureprint/featuresequence)*