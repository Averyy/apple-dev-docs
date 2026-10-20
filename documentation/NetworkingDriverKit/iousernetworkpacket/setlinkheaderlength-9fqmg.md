# SetLinkHeaderLength

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Instance Method

Changes the number of bytes to use for the link header to the specified value.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual kern_return_t SetLinkHeaderLength(uint8_t length);
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

## Parameters

- `length`: The new length value, specified in bytes

## See Also

### Configuring the Packet State Information
- [SetHeadroom](./setheadroom.md)
  Changes the number of bytes to reserve at the front of the packet’s buffer to the specified value.
- [SetDataOffset](./setdataoffset-16kx3.md)
  Changes the offset to the beginning of the packet’s data to the specified value.
- [SetDataLength](./setdatalength-788b.md)
  Changes the number of bytes of data in the packet to the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacket/setlinkheaderlength-9fqmg)*