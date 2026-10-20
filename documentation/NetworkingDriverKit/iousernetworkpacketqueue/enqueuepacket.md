# EnqueuePacket

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Instance Method

Adds a single network packet to the queue for processing.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual kern_return_t EnqueuePacket(IOUserNetworkPacket *packet);
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

#### Discussion

Call this method when you are ready to submit a single packet to a completion queue for processing. After the system processes the enqueued network packet, it recycles it and makes it available on the corresponding submission queue.

## Parameters

- `packet`: The packet to add to the queue.

## See Also

### Queueing and Dequeueing Packets
- [EnqueuePackets](./enqueuepackets-qzx.md)
  Adds multiple network packets to the queue for processing.
- [DequeuePacket](./dequeuepacket.md)
  Retrieves a single network packet from the queue.
- [DequeuePackets](./dequeuepackets.md)
  Retrieves multiple network packets from the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacketqueue/enqueuepacket)*