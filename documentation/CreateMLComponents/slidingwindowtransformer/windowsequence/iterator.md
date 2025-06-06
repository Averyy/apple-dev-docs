# SlidingWindowTransformer.WindowSequence.Iterator

**Framework**: Create ML Components  
**Kind**: struct

An async iterator of window sequence.

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
struct Iterator
```

## Topics

### Getting the next element
- [func next() async throws -> TemporalFeature<SlidingWindowTransformer<Input>.Output>?](slidingwindowtransformer/windowsequence/iterator/next.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.
### Type Aliases
- [SlidingWindowTransformer.WindowSequence.Iterator.Element](slidingwindowtransformer/windowsequence/iterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](slidingwindowtransformer/windowsequence/iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)

## See Also

- [func makeAsyncIterator() -> SlidingWindowTransformer<Input>.WindowSequence.Iterator](slidingwindowtransformer/windowsequence/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [SlidingWindowTransformer.WindowSequence.AsyncIterator](slidingwindowtransformer/windowsequence/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [SlidingWindowTransformer.WindowSequence.Feature](slidingwindowtransformer/windowsequence/feature.md)
  The feature type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/slidingwindowtransformer/windowsequence/iterator)*