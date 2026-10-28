# GetAddressRange

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Returns the address and length of the memory buffer.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
kern_return_t GetAddressRange(IOAddressSegment *range);
```

## Return Value

[`kIOReturnSuccess`](../kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../error-codes.md).

## Parameters

- `range`: An [`IOAddressSegment`](../ioaddresssegment.md) structure that you provide. On return, this structure contains the address and length of the memory buffer.

## See Also

### Managing the Buffer Contents
- [SetLength](./setlength.md)
  Changes the length of the memory buffer.
- [IOAddressSegment](../ioaddresssegment.md)
  A structure that describes the location and size of a block of memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iobuffermemorydescriptor/getaddressrange)*