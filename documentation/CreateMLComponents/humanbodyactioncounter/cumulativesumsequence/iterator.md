# HumanBodyActionCounter.CumulativeSumSequence.Iterator

**Framework**: Create ML Components  
**Kind**: struct

An async iterator of cumulative count sequence.

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
- [func next() async throws -> TemporalFeature<Float>?](humanbodyactioncounter/cumulativesumsequence/iterator/next.md)
  Advances to the next element and returns it, or nil if no next element exists.
### Type Aliases
- [HumanBodyActionCounter.CumulativeSumSequence.Iterator.Element](humanbodyactioncounter/cumulativesumsequence/iterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](humanbodyactioncounter/cumulativesumsequence/iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)

## See Also

- [func makeAsyncIterator() -> HumanBodyActionCounter.CumulativeSumSequence.Iterator](humanbodyactioncounter/cumulativesumsequence/makeasynciterator.md)
  Constructs an iterator.
- [HumanBodyActionCounter.CumulativeSumSequence.AsyncIterator](humanbodyactioncounter/cumulativesumsequence/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [HumanBodyActionCounter.CumulativeSumSequence.Feature](humanbodyactioncounter/cumulativesumsequence/feature.md)
  The feature type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/humanbodyactioncounter/cumulativesumsequence/iterator)*