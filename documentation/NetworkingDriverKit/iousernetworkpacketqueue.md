# IOUserNetworkPacketQueue

**Framework**: NetworkingDriverKit  
**Kind**: class

The base class for the queues that manage the packets moving to and from your device.

**Availability**:
- DriverKit ?+

## Declaration

```swift
class IOUserNetworkPacketQueue;
```

#### Overview

This class provides the common functionality for the submission and completion queues you use to manage network packets. You do not create instances of this class directly. Instead, you instantiate the following concrete subclasses:

- [`IOUserNetworkRxSubmissionQueue`](iousernetworkrxsubmissionqueue.md)
- [`IOUserNetworkRxCompletionQueue`](iousernetworkrxcompletionqueue.md)
- [`IOUserNetworkTxSubmissionQueue`](iousernetworktxsubmissionqueue.md)
- [`IOUserNetworkTxCompletionQueue`](iousernetworktxcompletionqueue.md)

Submission queues contain the packets that your driver dequeues and processes. After you process the dequeued packets, you place them on the matching completion queue to let the system know that you are finished with them. The system eventually recycles the completed packets back to the corresponding submission queue so that the cycle may begin again.

## Topics

### Configuring the Packet Queue
- [init](iousernetworkpacketqueue/init.md)
  Initializes the packet submission queue.
- [free](iousernetworkpacketqueue/free.md)
  Performs any final cleanup for the queue.
### Enabling the Packet Queue
- [SetEnable](iousernetworkpacketqueue/setenable-76sm5.md)
  Enables or disables the queue.
### Queueing and Dequeueing Packets
- [EnqueuePacket](iousernetworkpacketqueue/enqueuepacket.md)
  Adds a single network packet to the queue for processing.
- [EnqueuePackets](iousernetworkpacketqueue/enqueuepackets-qzx.md)
  Adds multiple network packets to the queue for processing.
- [DequeuePacket](iousernetworkpacketqueue/dequeuepacket.md)
  Retrieves a single network packet from the queue.
- [DequeuePackets](iousernetworkpacketqueue/dequeuepackets.md)
  Retrieves multiple network packets from the queue.
### Configuring the Queue Attributes
- [SetPacketBufferPool](iousernetworkpacketqueue/setpacketbufferpool.md)
  Assigns the specified buffer pool with this queue.
- [SetPacketDirection](iousernetworkpacketqueue/setpacketdirection.md)
  Specifies whether packets flow into or out of the queue.
### Managing the Data Queue
- [CopyDataQueue](iousernetworkpacketqueue/copydataqueue.md)
  Returns the dispatch queue that this object uses to execute tasks.
- [SetDataQueue](iousernetworkpacketqueue/setdataqueue.md)
  Assigns the specified dispatch source to this object.
### Instance Methods
- [enqueuePackets](iousernetworkpacketqueue/enqueuepackets-13ln6.md)
- [requestDequeue](iousernetworkpacketqueue/requestdequeue.md)
- [requestEnqueue](iousernetworkpacketqueue/requestenqueue.md)
- [setEnable](iousernetworkpacketqueue/setenable-8eikm.md)
- [setPacketPoller](iousernetworkpacketqueue/setpacketpoller.md)

## Relationships

### Inherits From
- [OSObject](../DriverKit/OSObject.md)
### Inherited By
- [IOUserNetworkRxCompletionQueue](iousernetworkrxcompletionqueue.md)
- [IOUserNetworkRxSubmissionQueue](iousernetworkrxsubmissionqueue.md)
- [IOUserNetworkTxCompletionQueue](iousernetworktxcompletionqueue.md)
- [IOUserNetworkTxSubmissionQueue](iousernetworktxsubmissionqueue.md)

## See Also

- [IOUserNetworkRxSubmissionQueue](iousernetworkrxsubmissionqueue.md)
  The queue that receives packets from the device.
- [IOUserNetworkRxCompletionQueue](iousernetworkrxcompletionqueue.md)
  The queue you use to store packets that you successfully transferred to the networking stack.
- [IOUserNetworkTxSubmissionQueue](iousernetworktxsubmissionqueue.md)
  The queue that receives packets from the networking stack.
- [IOUserNetworkTxCompletionQueue](iousernetworktxcompletionqueue.md)
  The queue you use to store packets that you successfully transferred to the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacketqueue)*