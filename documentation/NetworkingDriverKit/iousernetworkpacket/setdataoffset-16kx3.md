# SetDataOffset

**Framework**: NetworkingDriverKit  
**Kind**: method

Changes the offset to the beginning of the packet’s data to the specified value.

**Availability**:
- DriverKit ?+
- Unknown ?+ - Deprecated

## Declaration

```swift
kern_return_t SetDataOffset(uint16_t offset);
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

## Parameters

- `offset`: The new data offset value, specified in bytes from the beginning of the buffer.

## See Also

- [SetHeadroom](iousernetworkpacket/setheadroom.md)
  Changes the number of bytes to reserve at the front of the packet’s buffer to the specified value.
- [SetLinkHeaderLength](iousernetworkpacket/setlinkheaderlength-9fqmg.md)
  Changes the number of bytes to use for the link header to the specified value.
- [SetDataLength](iousernetworkpacket/setdatalength-788b.md)
  Changes the number of bytes of data in the packet to the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacket/setdataoffset-16kx3)*