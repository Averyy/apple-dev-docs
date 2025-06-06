# AudioFeaturePrint.FeatureSequence

**Framework**: Create ML Components  
**Kind**: struct

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
- [var count: Int?](audiofeatureprint/featuresequence/count.md)
  The number of elements in the sequence. For this sequence count is always nil.
### Creating an iterator
- [func makeAsyncIterator() -> AudioFeaturePrint.FeatureSequence.AsyncIterator](audiofeatureprint/featuresequence/makeasynciterator.md)
  Constructs an iterator.
- [AudioFeaturePrint.FeatureSequence.Iterator](audiofeatureprint/featuresequence/iterator.md)
  An async iterator of audio buffers.
- [AudioFeaturePrint.FeatureSequence.AsyncIterator](audiofeatureprint/featuresequence/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [AudioFeaturePrint.FeatureSequence.Feature](audiofeatureprint/featuresequence/feature.md)
  The feature type.
### Type Aliases
- [AudioFeaturePrint.FeatureSequence.Element](audiofeatureprint/featuresequence/element.md)
  The type of element produced by this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](audiofeatureprint/featuresequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [TemporalSequence](temporalsequence.md)

## See Also

- [func applied<S>(to: S, eventHandler: EventHandler?) throws -> AudioFeaturePrint.FeatureSequence](audiofeatureprint/applied(to:eventhandler:).md)
  Extracts audio features from an a sequence of audio buffers
- [func applied<S, TS, Annotation>(to: S, eventHandler: EventHandler?) async throws -> [AnnotatedFeature<Self.OutputSequence, Annotation>]](audiofeatureprint/applied(to:eventhandler:)-74d6e.md)
  Performs the transformation on a sequence of annotated input sequences.
- [AudioFeaturePrint.Input](audiofeatureprint/input.md)
  The input type.
- [AudioFeaturePrint.Output](audiofeatureprint/output.md)
  The output type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audiofeatureprint/featuresequence)*