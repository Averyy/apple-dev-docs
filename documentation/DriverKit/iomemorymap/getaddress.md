# GetAddress

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Returns the address of the memory block.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
uint64_t GetAddress();
```

## Return Value

The address of the first byte of the memory block in the current process.

## See Also

### Getting the Map Attributes
- [GetLength](./getlength.md)
  Returns the length of the memory block in bytes.
- [GetOffset](./getoffset.md)
  Returns the offset from the original start of the memory block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iomemorymap/getaddress)*