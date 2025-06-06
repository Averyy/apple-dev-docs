# LazyFilterSequence.Iterator

**Framework**: Swift  
**Kind**: struct

An iterator over the elements traversed by some base iterator that also satisfy a given predicate.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@frozen
struct Iterator
```

#### Overview

> **Note**: This is the associated `Iterator` of `LazyFilterSequence` and `LazyFilterCollection`.

## Topics

### Instance Properties
- [var base: Base.Iterator](lazyfiltersequence/iterator/base.md)
  The underlying iterator whose elements are being filtered.
### Default Implementations
- [IteratorProtocol Implementations](lazyfiltersequence/iterator/iteratorprotocol-implementations.md)
- [Sequence Implementations](lazyfiltersequence/iterator/sequence-implementations.md)

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [IteratorProtocol](iteratorprotocol.md)
- [Sequence](sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazyfiltersequence/iterator)*