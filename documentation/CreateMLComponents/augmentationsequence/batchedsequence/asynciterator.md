# AugmentationSequence.BatchedSequence.AsyncIterator

**Framework**: Create ML Components  
**Kind**: struct

The iterator that produces batches.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct AsyncIterator
```

## Topics

### Getting the next element
- [func next() async throws -> [AugmentationSequence<Base, RandomTransformer, RandomNumberGenerator, Annotation>.Element]?](augmentationsequence/batchedsequence/asynciterator/next.md)
  Produces the next batch.
### Type Aliases
- [AugmentationSequence.BatchedSequence.AsyncIterator.Element](augmentationsequence/batchedsequence/asynciterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](augmentationsequence/batchedsequence/asynciterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/augmentationsequence/batchedsequence/asynciterator)*