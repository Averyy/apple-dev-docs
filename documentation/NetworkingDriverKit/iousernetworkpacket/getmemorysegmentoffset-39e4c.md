# GetMemorySegmentOffset

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the offset to the beginning of the packet in the corresponding memory buffer.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual kern_return_t GetMemorySegmentOffset(uint64_t *offset) const;
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

## Parameters

- `offset`: On return, the memory segment offset value.

## See Also

### Getting the Packet Information
- [GetHeadroom](./getheadroom.md)
  Gets the number of bytes reserved at the front of the packet’s buffer.
- [GetLinkHeaderLength](./getlinkheaderlength-8dlhu.md)
  Gets the number of bytes to use for the link header.
- [GetDataOffset](./getdataoffset-4tw7y.md)
  Gets the offset to the beginning of the packet’s data.
- [GetDataLength](./getdatalength-8km3n.md)
  Gets the number of bytes of data in the packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacket/getmemorysegmentoffset-39e4c)*