# enumerateBytes(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Enumerates the contents of the data’s buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+
- Swift - Deprecated in 5.0

> **Deprecated**: use `regions` or `for-in` instead

## Declaration

```swift
func enumerateBytes(_ block: (UnsafeBufferPointer<UInt8>, Data.Index, inout Bool) -> Void)
```

## Discussion

In some cases, (for example, a [`Data`](../data.md) backed by a `dispatch_data_t`, the bytes may be stored discontiguously. In those cases, this function invokes the closure for each contiguous region of bytes.

## Parameters

- `block`: The closure to invoke for each region of data. You may stop the enumeration by setting the `stop` parameter to `true`.

## See Also

### Iterating Over Bytes
- [func makeIterator() -> Data.Iterator](./makeiterator%28%29.md)
  Returns an iterator over the contents of the data.
- [struct Iterator](./iterator.md)
  An iterator that operates over the contents of data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/enumeratebytes(_:))*