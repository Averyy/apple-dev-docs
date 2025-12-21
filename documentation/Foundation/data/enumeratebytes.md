# enumerateBytes(_:)

**Framework**: Foundation  
**Kind**: method

Enumerates the contents of the data’s buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+
- Swift ?+

## Declaration

```swift
func enumerateBytes(_ block: (UnsafeBufferPointer<UInt8>, Data.Index, inout Bool) -> Void)
```

#### Discussion

In some cases, (for example, a [`Data`](data.md) backed by a `dispatch_data_t`, the bytes may be stored discontiguously. In those cases, this function invokes the closure for each contiguous region of bytes.

## Parameters

- `block`: The closure to invoke for each region of data. You may stop the enumeration by setting the   parameter to  .

## See Also

- [func makeIterator() -> Data.Iterator](data/makeiterator.md)
  Returns an iterator over the contents of the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/enumeratebytes(_:))*