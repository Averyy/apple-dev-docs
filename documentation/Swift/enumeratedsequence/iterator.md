# EnumeratedSequence.Iterator

**Framework**: Swift  
**Kind**: struct

The iterator for `EnumeratedSequence`.

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

An instance of this iterator wraps a base iterator and yields successive `Int` values, starting at zero, along with the elements of the underlying base iterator. The following example enumerates the elements of an array:

```swift
var iterator = ["foo", "bar"].enumerated().makeIterator()
iterator.next() // (0, "foo")
iterator.next() // (1, "bar")
iterator.next() // nil
```

To create an instance, call `enumerated().makeIterator()` on a sequence or collection.

## Topics

### Default Implementations
- [IteratorProtocol Implementations](enumeratedsequence/iterator/iteratorprotocol-implementations.md)
- [Sequence Implementations](enumeratedsequence/iterator/sequence-implementations.md)

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [IteratorProtocol](iteratorprotocol.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
- [Sequence](sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/enumeratedsequence/iterator)*