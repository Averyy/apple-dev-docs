# IOAddressSegment

**Framework**: DriverKit  
**Kind**: struct  
**Role**: Structure

A structure that describes the location and size of a block of memory.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
struct IOAddressSegment;
```

## Topics

### Getting the Address Information
- [address](./ioaddresssegment/address.md)
  The address of the buffer in the current process’ virtual memory space.
- [length](./ioaddresssegment/length.md)
  The size of the memory buffer, in bytes.

## See Also

### Managing the Buffer Contents
- [SetLength](./iobuffermemorydescriptor/setlength.md)
  Changes the length of the memory buffer.
- [GetAddressRange](./iobuffermemorydescriptor/getaddressrange.md)
  Returns the address and length of the memory buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioaddresssegment)*