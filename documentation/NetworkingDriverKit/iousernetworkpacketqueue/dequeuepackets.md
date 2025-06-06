# DequeuePackets

**Framework**: NetworkingDriverKit  
**Kind**: method

Retrieves multiple network packets from the queue.

**Availability**:
- DriverKit ?+

## Declaration

```swift
uint32_t DequeuePackets(IOUserNetworkPacket * * packets, uint32_t maxDequeueCount);
```

#### Return Value

The actual number of packets returned in the `packets` parameter.

#### Discussion

Call this method to retrieve multiple packets from the submission queue. This method returns as many packets as are available, up to the maximum number you specify.

## Parameters

- `packets`: On return, an array containing the next available packets.
- `maxDequeueCount`: The number of packets you want to dequeue.

## See Also

- [EnqueuePacket](iousernetworkpacketqueue/enqueuepacket.md)
  Adds a single network packet to the queue for processing.
- [EnqueuePackets](iousernetworkpacketqueue/enqueuepackets-qzx.md)
  Adds multiple network packets to the queue for processing.
- [DequeuePacket](iousernetworkpacketqueue/dequeuepacket.md)
  Retrieves a single network packet from the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacketqueue/dequeuepackets)*