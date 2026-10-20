# Dictionary.Iterator

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

An iterator over the members of a `Dictionary<Key, Value>`.

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

Available when `Key` conforms to `Hashable`.

## Topics

### Default Implementations
- [CustomReflectable Implementations](./iterator/customreflectable-implementations.md)
- [IteratorProtocol Implementations](./iterator/iteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [Copyable](../copyable.md)
- [CustomReflectable](../customreflectable.md)
- [Escapable](../escapable.md)
- [IteratorProtocol](../iteratorprotocol.md)
- [Sendable](../sendable.md)
- [SendableMetatype](../sendablemetatype.md)

## See Also

### Supporting Types
- [Dictionary.Keys](./keys-swift.struct.md)
  A view of a dictionary’s keys.
- [Dictionary.Values](./values-swift.struct.md)
  A view of a dictionary’s values.
- [Dictionary.Index](./index.md)
  The position of a key-value pair in a dictionary.
- [Dictionary.Indices](./indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/iterator)*