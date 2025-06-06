# init(bytes:)

**Framework**: Dispatch  
**Kind**: init

Initialize a data object with copied memory content.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Swift ?+

## Declaration

```swift
init(bytes buffer: UnsafeBufferPointer<UInt8>)
```

## Parameters

- `buffer`: A pointer to the memory. It will be copied.

## See Also

- [init(bytesNoCopy: UnsafeBufferPointer<UInt8>, deallocator: DispatchData.Deallocator)](dispatchdata/init(bytesnocopy:deallocator:)-7h08w.md)
  Initialize a data object without copying the bytes.
- [func append(UnsafePointer<UInt8>, count: Int)](dispatchdata/append(_:count:).md)
- [func copyBytes(to: UnsafeMutablePointer<UInt8>, count: Int)](dispatchdata/copybytes(to:count:)-4ffyj.md)
- [func copyBytes(to: UnsafeMutablePointer<UInt8>, from: Range<DispatchData.Index>)](dispatchdata/copybytes(to:from:)-6ztcb.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchdata/init(bytes:)-mkbp)*