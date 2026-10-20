# withUnsafeMutableBytes(_:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method

Performs the given closure with an unsafe pointer to the underlying bytes of the data buffer.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func withUnsafeMutableBytes<R, E>(_ body: (UnsafeMutableRawBufferPointer) throws(E) -> R) throws(E) -> R where E : Error
```

## Parameters

- `body`: The closure to perform with the pointer.

## See Also

### Accessing buffer properties
- [var length: Int](./length.md)
  The data length of the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsmutablefiledatabuffer/withunsafemutablebytes(_:))*