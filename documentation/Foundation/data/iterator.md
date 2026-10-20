# Data.Iterator

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
- [IteratorProtocol](../../Swift/iteratorprotocol.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Iterating Over Bytes
- [func makeIterator() -> Data.Iterator](./makeiterator%28%29.md)
  Returns an iterator over the contents of the data.
- [func enumerateBytes((UnsafeBufferPointer<UInt8>, Data.Index, inout Bool) -> Void)](./enumeratebytes%28_%29.md)
  Enumerates the contents of the data’s buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/iterator)*