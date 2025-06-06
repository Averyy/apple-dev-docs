# IOUserNetworkTxSubmissionQueue

**Framework**: NetworkingDriverKit  
**Kind**: class

The queue that receives packets from the networking stack.

**Availability**:
- DriverKit ?+

## Declaration

```swift
class IOUserNetworkTxSubmissionQueue;
```

#### Overview

Create an [`IOUserNetworkTxSubmissionQueue`](iousernetworktxsubmissionqueue.md) in your driver and use it to dequeue empty packets. As your driver receives data from the networking stack, fill the empty packets with data send them to your hardware device. After sending the packets, enqueue them on your [`IOUserNetworkTxCompletionQueue`](iousernetworktxcompletionqueue.md) object so that the system can reclaim them and make them available for reuse later.

## Topics

### Creating the Submission Queue
- [init](iousernetworktxsubmissionqueue/init.md)
  Initializes the packet submission queue.
- [free](iousernetworktxsubmissionqueue/free.md)
  Performs any final cleanup for the queue.
### Instance Methods
- [initWithPool](iousernetworktxsubmissionqueue/initwithpool.md)
- [purgePackets](iousernetworktxsubmissionqueue/purgepackets.md)
### Type Methods
- [Create](iousernetworktxsubmissionqueue/create-64w2g.md)
- [Create](iousernetworktxsubmissionqueue/create-99dcq.md)
- [withPool](iousernetworktxsubmissionqueue/withpool.md)
- [withPoolAndServiceClass](iousernetworktxsubmissionqueue/withpoolandserviceclass.md)

## Relationships

### Inherits From
- [IOUserNetworkPacketQueue](iousernetworkpacketqueue.md)

## See Also

- [IOUserNetworkRxSubmissionQueue](iousernetworkrxsubmissionqueue.md)
  The queue that receives packets from the device.
- [IOUserNetworkRxCompletionQueue](iousernetworkrxcompletionqueue.md)
  The queue you use to store packets that you successfully transferred to the networking stack.
- [IOUserNetworkTxCompletionQueue](iousernetworktxcompletionqueue.md)
  The queue you use to store packets that you successfully transferred to the device.
- [IOUserNetworkPacketQueue](iousernetworkpacketqueue.md)
  The base class for the queues that manage the packets moving to and from your device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworktxsubmissionqueue)*