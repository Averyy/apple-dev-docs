# AudioFeaturePrint.FeatureSequence.Iterator

**Framework**: Create ML Components  
**Kind**: struct

An async iterator of audio buffers.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct Iterator
```

## Topics

### Getting the next element
- [func next() async throws -> TemporalFeature<MLShapedArray<Float>>?](audiofeatureprint/featuresequence/iterator/next.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.
### Type Aliases
- [AudioFeaturePrint.FeatureSequence.Iterator.Element](audiofeatureprint/featuresequence/iterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](audiofeatureprint/featuresequence/iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)

## See Also

- [func makeAsyncIterator() -> AudioFeaturePrint.FeatureSequence.AsyncIterator](audiofeatureprint/featuresequence/makeasynciterator.md)
  Constructs an iterator.
- [AudioFeaturePrint.FeatureSequence.AsyncIterator](audiofeatureprint/featuresequence/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [AudioFeaturePrint.FeatureSequence.Feature](audiofeatureprint/featuresequence/feature.md)
  The feature type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audiofeatureprint/featuresequence/iterator)*