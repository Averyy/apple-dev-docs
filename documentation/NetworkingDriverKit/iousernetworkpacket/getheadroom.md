# GetHeadroom

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the number of bytes reserved at the front of the packet’s buffer.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual kern_return_t GetHeadroom(uint8_t *headroom) const;
```

## Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

## Parameters

- `headroom`: On return, the headroom value.

## See Also

### Getting the Packet Information
- [GetLinkHeaderLength](./getlinkheaderlength-8dlhu.md)
  Gets the number of bytes to use for the link header.
- [GetDataOffset](./getdataoffset-4tw7y.md)
  Gets the offset to the beginning of the packet’s data.
- [GetDataLength](./getdatalength-8km3n.md)
  Gets the number of bytes of data in the packet.
- [GetMemorySegmentOffset](./getmemorysegmentoffset-39e4c.md)
  Gets the offset to the beginning of the packet in the corresponding memory buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacket/getheadroom)*