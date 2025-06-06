# AnyIndex

**Framework**: Swift  
**Kind**: struct

A wrapper over an underlying index that hides the specific underlying type.

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
struct AnyIndex
```

## Topics

### Initializers
- [init<BaseIndex>(BaseIndex)](anyindex/init(_:).md)
  Creates a new index wrapping `base`.
### Default Implementations
- [Comparable Implementations](anyindex/comparable-implementations.md)
- [Equatable Implementations](anyindex/equatable-implementations.md)

## Relationships

### Conforms To
- [Comparable](comparable.md)
- [Copyable](copyable.md)
- [Equatable](equatable.md)

## See Also

- [struct AnySequence](anysequence.md)
  A type-erased sequence.
- [struct AnyCollection](anycollection.md)
  A type-erased wrapper over any collection with indices that support forward traversal.
- [struct AnyBidirectionalCollection](anybidirectionalcollection.md)
  A type-erased wrapper over any collection with indices that support bidirectional traversal.
- [struct AnyRandomAccessCollection](anyrandomaccesscollection.md)
  A type-erased wrapper over any collection with indices that support random access traversal.
- [struct AnyIterator](anyiterator.md)
  A type-erased iterator of `Element`.
- [struct AnyHashable](anyhashable.md)
  A type-erased hashable value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anyindex)*