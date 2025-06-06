# Dictionary.Index

**Framework**: Swift  
**Kind**: struct

The position of a key-value pair in a dictionary.

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
struct Index
```

#### Overview

Dictionary has two subscripting interfaces:

1. Subscripting with a key, yielding an optional value: ```swift
v = d[k]!
```
2. Subscripting with an index, yielding a key-value pair: ```swift
(k, v) = d[i]
```

## Topics

### Default Implementations
- [Comparable Implementations](dictionary/index/comparable-implementations.md)
- [Equatable Implementations](dictionary/index/equatable-implementations.md)
- [Hashable Implementations](dictionary/index/hashable-implementations.md)

## Relationships

### Conforms To
- [Comparable](comparable.md)
- [Copyable](copyable.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)

## See Also

- [Dictionary.Keys](dictionary/keys-swift.struct.md)
  A view of a dictionary’s keys.
- [Dictionary.Values](dictionary/values-swift.struct.md)
  A view of a dictionary’s values.
- [Dictionary.Indices](dictionary/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [Dictionary.Iterator](dictionary/iterator.md)
  An iterator over the members of a `Dictionary<Key, Value>`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/index)*