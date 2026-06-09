# Data.Iterator

**Framework**: Foundation  
**Kind**: struct

An iterator that operates over the contents of data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct Iterator
```

## Relationships

### Conforms To
- [IteratorProtocol](../Swift/IteratorProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func makeIterator() -> Data.Iterator](data/makeiterator.md)
  Returns an iterator over the contents of the data.
- [func enumerateBytes((UnsafeBufferPointer<UInt8>, Data.Index, inout Bool) -> Void)](data/enumeratebytes(_:).md)
  Enumerates the contents of the data’s buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/iterator)*