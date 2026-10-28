# GetLength

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Returns the length of the memory block in bytes.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
uint64_t GetLength();
```

## Return Value

The number of bytes in the memory block.

## Discussion

The length represents the number of bytes that are accessible to the current process.

## See Also

### Getting the Map Attributes
- [GetAddress](./getaddress.md)
  Returns the address of the memory block.
- [GetOffset](./getoffset.md)
  Returns the offset from the original start of the memory block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iomemorymap/getlength)*