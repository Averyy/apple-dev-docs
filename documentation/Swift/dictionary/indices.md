# Dictionary.Indices

**Framework**: Swift  
**Kind**: typealias  
**Role**: Type Alias

A type that represents the indices that are valid for subscripting the collection, in ascending order.

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
typealias Indices = DefaultIndices<Dictionary<Key, Value>>
```

Available when `Key` conforms to `Hashable`.

## See Also

### Supporting Types
- [Dictionary.Keys](./keys-swift.struct.md)
  A view of a dictionary’s keys.
- [Dictionary.Values](./values-swift.struct.md)
  A view of a dictionary’s values.
- [Dictionary.Index](./index.md)
  The position of a key-value pair in a dictionary.
- [Dictionary.Iterator](./iterator.md)
  An iterator over the members of a `Dictionary<Key, Value>`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/indices)*