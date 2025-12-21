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

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)

## See Also

- [func makeAsyncIterator() -> HumanBodyActionCounter.CumulativeSumSequence.Iterator](humanbodyactioncounter/cumulativesumsequence/makeasynciterator.md)
  Constructs an iterator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/humanbodyactioncounter/cumulativesumsequence/iterator)*