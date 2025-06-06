# GetLinkHeaderLength

**Framework**: NetworkingDriverKit  
**Kind**: method

Gets the number of bytes to use for the link header.

**Availability**:
- DriverKit ?+
- Unknown ?+ - Deprecated

## Declaration

```swift
kern_return_t GetLinkHeaderLength(uint8_t * length) const;
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

## Parameters

- `length`: On return, the link header length value.

## See Also

- [GetHeadroom](iousernetworkpacket/getheadroom.md)
  Gets the number of bytes reserved at the front of the packet’s buffer.
- [GetDataOffset](iousernetworkpacket/getdataoffset-4tw7y.md)
  Gets the offset to the beginning of the packet’s data.
- [GetDataLength](iousernetworkpacket/getdatalength-8km3n.md)
  Gets the number of bytes of data in the packet.
- [GetMemorySegmentOffset](iousernetworkpacket/getmemorysegmentoffset-39e4c.md)
  Gets the offset to the beginning of the packet in the corresponding memory buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacket/getlinkheaderlength-8dlhu)*