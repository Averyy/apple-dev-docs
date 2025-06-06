# PreprocessedFeatureSequence.AsyncIterator

**Framework**: Create ML Components  
**Kind**: struct

The type of asynchronous iterator that produces elements of this asynchronous sequence.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct AsyncIterator
```

## Topics

### Getting the next element
- [func next() -> TemporalFeature<Feature>?](preprocessedfeaturesequence/asynciterator/next.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.
### Type Aliases
- [PreprocessedFeatureSequence.AsyncIterator.Element](preprocessedfeaturesequence/asynciterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](preprocessedfeaturesequence/asynciterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessedfeaturesequence/asynciterator)*