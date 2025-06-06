# DeallocatePacket

**Framework**: NetworkingDriverKit  
**Kind**: method

Disposes of any resources associated with the packet and makes the packet available for reuse.

**Availability**:
- DriverKit ?+
- Unknown ?+ - Deprecated

## Declaration

```swift
kern_return_t DeallocatePacket(IOUserNetworkPacket * packet);
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

#### Discussion

After you move a packet to the appropriate completion queue, call this method to recycle the packet. Recycling the packet makes it available for use with a new incoming or outgoing packet.

## Parameters

- `packet`: The packet to deallocate. It is a programmer error to specify   or an invalid pointer for this parameter.

## See Also

- [DeallocatePackets](iousernetworkpacketbufferpool/deallocatepackets-186ya.md)
  Disposes of any resources associated with the specified packets and makes them available for reuse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacketbufferpool/deallocatepacket-3i02n)*