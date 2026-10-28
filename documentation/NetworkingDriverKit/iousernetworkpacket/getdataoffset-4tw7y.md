# GetDataOffset

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the offset to the beginning of the packet’s data.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual kern_return_t GetDataOffset(uint16_t *offset) const;
```

## Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

## Parameters

- `offset`: On return, the offset value.

## See Also

### Getting the Packet Information
- [GetHeadroom](./getheadroom.md)
  Gets the number of bytes reserved at the front of the packet’s buffer.
- [GetLinkHeaderLength](./getlinkheaderlength-8dlhu.md)
  Gets the number of bytes to use for the link header.
- [GetDataLength](./getdatalength-8km3n.md)
  Gets the number of bytes of data in the packet.
- [GetMemorySegmentOffset](./getmemorysegmentoffset-39e4c.md)
  Gets the offset to the beginning of the packet in the corresponding memory buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacket/getdataoffset-4tw7y)*