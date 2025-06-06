# GetAddressRange

**Framework**: DriverKit  
**Kind**: method

Returns the address and length of the memory buffer.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t GetAddressRange(IOAddressSegment * range);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. See [`Error Codes`](error-codes.md).

## Parameters

- `range`: An   structure that you provide. On return, this structure contains the address and length of the memory buffer.

## See Also

- [SetLength](iobuffermemorydescriptor/setlength.md)
  Changes the length of the memory buffer.
- [IOAddressSegment](ioaddresssegment.md)
  A structure that describes the location and size of a block of memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iobuffermemorydescriptor/getaddressrange)*