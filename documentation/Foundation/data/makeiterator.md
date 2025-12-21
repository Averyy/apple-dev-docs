# makeIterator()

**Framework**: Foundation  
**Kind**: method

Returns an iterator over the contents of the data.

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
func makeIterator() -> Data.Iterator
```

#### Discussion

The iterator will increment byte-by-byte.

## See Also

- [func enumerateBytes((UnsafeBufferPointer<UInt8>, Data.Index, inout Bool) -> Void)](data/enumeratebytes(_:).md)
  Enumerates the contents of the data’s buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/makeiterator())*