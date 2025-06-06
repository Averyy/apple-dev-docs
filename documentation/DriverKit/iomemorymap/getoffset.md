# GetOffset

**Framework**: DriverKit  
**Kind**: method

Returns the offset from the original start of the memory block.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
uint64_t GetOffset();
```

#### Return Value

The number of bytes from the start of the original block of memory to the first byte of this memory map object.

#### Discussion

When creating a memory map object, you can map to a location in the middle of the underlying buffer. You might do this to access a specific structure inside that buffer. This method returns the offset from the original start of the buffer to the first byte of your mapping.

## See Also

- [GetAddress](iomemorymap/getaddress.md)
  Returns the address of the memory block.
- [GetLength](iomemorymap/getlength.md)
  Returns the length of the memory block in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iomemorymap/getoffset)*