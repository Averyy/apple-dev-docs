# init(bytesNoCopy:deallocator:)

**Framework**: Dispatch  
**Kind**: init  
**Role**: Initializer

Initialize a data object without copying the bytes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Swift - Deprecated in 4.0

> **Deprecated**: Use init(bytesNoCopy: UnsafeRawBufferPointer, deallocater: Deallocator) instead

## Declaration

```swift
init(bytesNoCopy bytes: UnsafeBufferPointer<UInt8>, deallocator: DispatchData.Deallocator = .free)
```

## Parameters

- `bytes`: A pointer to the bytes.
- `deallocator`: Specifies the mechanism to free the indicated buffer.

## See Also

### Deprecated
- [init(bytes: UnsafeBufferPointer<UInt8>)](./init%28bytes%29-mkbp.md)
  Initialize a data object with copied memory content.
- [func append(UnsafePointer<UInt8>, count: Int)](./append%28_,count%29.md)
- [func copyBytes(to: UnsafeMutablePointer<UInt8>, count: Int)](./copybytes%28to,count%29-4ffyj.md)
- [func copyBytes(to: UnsafeMutablePointer<UInt8>, from: Range<DispatchData.Index>)](./copybytes%28to,from%29-6ztcb.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchdata/init(bytesnocopy:deallocator:)-7h08w)*