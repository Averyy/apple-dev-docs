# DeallocatePackets

**Framework**: NetworkingDriverKit  
**Kind**: method

Disposes of any resources associated with the specified packets and makes them available for reuse.

**Availability**:
- DriverKit ?+
- Unknown ?+ - Deprecated

## Declaration

```swift
kern_return_t DeallocatePackets(IOUserNetworkPacket * * packets, uint32_t packetsCount);
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

#### Discussion

After you move one or more packets to the appropriate completion queue, call this method to recycle those packets. Recycling packets makes them available for use with new incoming or outgoing packets.

## Parameters

- `packets`: An array of packets to deallocate. It is a programmer error to specify   or an invalid pointer for this parameter.
- `packetsCount`: The number of items in the   parameter.

## See Also

- [DeallocatePacket](iousernetworkpacketbufferpool/deallocatepacket-3i02n.md)
  Disposes of any resources associated with the packet and makes the packet available for reuse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacketbufferpool/deallocatepackets-186ya)*