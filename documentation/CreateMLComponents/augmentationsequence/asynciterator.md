# AugmentationSequence.AsyncIterator

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

The iterator that produces elements in the augmentation sequence.

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

Available when `Base` conforms to `Sequence`, `RandomTransformer` conforms to `RandomTransformer`, `RandomNumberGenerator` conforms to `RandomNumberGenerator`, `Base.Element` is `AnnotatedFeature<RandomTransformer.Input, Annotation>`, and `RandomTransformer.Input` is `RandomTransformer.Output`.

## Topics

### Getting the next element
- [func next() async throws -> Base.Element?](./asynciterator/next%28%29.md)
  Produces the next element in the augmentation sequence.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../../Swift/asynciteratorprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/augmentationsequence/asynciterator)*