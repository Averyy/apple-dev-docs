# DequeuePacket

**Framework**: NetworkingDriverKit  
**Kind**: method

Retrieves a single network packet from the queue.

**Availability**:
- DriverKit ?+

## Declaration

```swift
kern_return_t DequeuePacket(IOUserNetworkPacket * * packet);
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

#### Discussion

Call this method to retrieve a single packet from a submission queue. This method returns the requested packet, or an error if no more packets are available.

## Parameters

- `packet`: On return, an array containing one element, which represents the next available packet.

## See Also

- [EnqueuePacket](iousernetworkpacketqueue/enqueuepacket.md)
  Adds a single network packet to the queue for processing.
- [EnqueuePackets](iousernetworkpacketqueue/enqueuepackets-qzx.md)
  Adds multiple network packets to the queue for processing.
- [DequeuePackets](iousernetworkpacketqueue/dequeuepackets.md)
  Retrieves multiple network packets from the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacketqueue/dequeuepacket)*