# init(bytes:)

**Framework**: Dispatch  
**Kind**: init  
**Role**: Initializer

Initialize a data object with copied memory content.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Swift - Deprecated in 4.0

> **Deprecated**: Use init(bytes: UnsafeRawBufferPointer) instead

## Declaration

```swift
init(bytes buffer: UnsafeBufferPointer<UInt8>)
```

## Parameters

- `buffer`: A pointer to the memory. It will be copied.

## See Also

### Deprecated
- [init(bytesNoCopy: UnsafeBufferPointer<UInt8>, deallocator: DispatchData.Deallocator)](./init%28bytesnocopy,deallocator%29-7h08w.md)
  Initialize a data object without copying the bytes.
- [func append(UnsafePointer<UInt8>, count: Int)](./append%28_,count%29.md)
- [func copyBytes(to: UnsafeMutablePointer<UInt8>, count: Int)](./copybytes%28to,count%29-4ffyj.md)
- [func copyBytes(to: UnsafeMutablePointer<UInt8>, from: Range<DispatchData.Index>)](./copybytes%28to,from%29-6ztcb.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchdata/init(bytes:)-mkbp)*