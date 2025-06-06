# GetPacketBufferPool

**Framework**: NetworkingDriverKit  
**Kind**: method

Gets the memory buffer that contains the pakcet.

**Availability**:
- DriverKit ?+
- Unknown ?+ - Deprecated

## Declaration

```swift
kern_return_t GetPacketBufferPool(IOUserNetworkPacketBufferPool * * pool) const;
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

## Parameters

- `pool`: On return, the memory buffer containing the packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacket/getpacketbufferpool-63snl)*