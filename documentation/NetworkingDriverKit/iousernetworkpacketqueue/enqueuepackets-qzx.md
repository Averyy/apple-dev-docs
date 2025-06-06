# EnqueuePackets

**Framework**: NetworkingDriverKit  
**Kind**: method

Adds multiple network packets to the queue for processing.

**Availability**:
- DriverKit ?+

## Declaration

```swift
uint32_t EnqueuePackets(IOUserNetworkPacket * * packets, uint32_t packetCount);
```

#### Return Value

The number of packets actually added to the queue.

#### Discussion

Call this method when you are ready to submit multiple packets to a completion queue for processing. After the system processes the enqueued network packets, it recycles them and makes them available on the corresponding submission queue.

## Parameters

- `packets`: An array of network packets you want to add to the queue.
- `packetCount`: The number of network packets in the   parameter.

## See Also

- [EnqueuePacket](iousernetworkpacketqueue/enqueuepacket.md)
  Adds a single network packet to the queue for processing.
- [DequeuePacket](iousernetworkpacketqueue/dequeuepacket.md)
  Retrieves a single network packet from the queue.
- [DequeuePackets](iousernetworkpacketqueue/dequeuepackets.md)
  Retrieves multiple network packets from the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacketqueue/enqueuepackets-qzx)*