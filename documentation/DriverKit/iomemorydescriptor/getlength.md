# GetLength

**Framework**: DriverKit  
**Kind**: method

Returns the length of the memory block represented by this object.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t GetLength(uint64_t * returnLength);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. See [`Error Codes`](error-codes.md).

#### Discussion

This method returns the effective size of the memory block, which might be less than the block’s total capacity.

## Parameters

- `returnLength`: A variable in which to put the length of the current memory block.

## See Also

- [SetLength](iobuffermemorydescriptor/setlength.md)
  Changes the length of the memory buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iomemorydescriptor/getlength)*