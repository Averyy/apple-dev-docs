# GetLinkHeaderLength

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the number of bytes to use for the link header.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual kern_return_t GetLinkHeaderLength(uint8_t *length) const;
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

## Parameters

- `length`: On return, the link header length value.

## See Also

### Getting the Packet Information
- [GetHeadroom](./getheadroom.md)
  Gets the number of bytes reserved at the front of the packet’s buffer.
- [GetDataOffset](./getdataoffset-4tw7y.md)
  Gets the offset to the beginning of the packet’s data.
- [GetDataLength](./getdatalength-8km3n.md)
  Gets the number of bytes of data in the packet.
- [GetMemorySegmentOffset](./getmemorysegmentoffset-39e4c.md)
  Gets the offset to the beginning of the packet in the corresponding memory buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacket/getlinkheaderlength-8dlhu)*