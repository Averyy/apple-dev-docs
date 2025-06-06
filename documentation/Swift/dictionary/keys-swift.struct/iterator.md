# Dictionary.Keys.Iterator

**Framework**: Swift  
**Kind**: struct

A type that provides the collection’s iteration interface and encapsulates its iteration state.

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

By default, a collection conforms to the `Sequence` protocol by supplying `IndexingIterator` as its associated `Iterator` type.

## Topics

### Instance Methods
- [func next() -> Key?](dictionary/keys-swift.struct/iterator/next.md)
  Advances to the next element and returns it, or `nil` if no next element exists.
### Type Aliases
- [Dictionary.Keys.Iterator.Element](dictionary/keys-swift.struct/iterator/element.md)
  The type of element traversed by the iterator.

## Relationships

### Conforms To
- [IteratorProtocol](iteratorprotocol.md)
- [Sendable](sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/keys-swift.struct/iterator)*