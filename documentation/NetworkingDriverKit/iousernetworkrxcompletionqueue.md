# IOUserNetworkRxCompletionQueue

**Framework**: NetworkingDriverKit  
**Kind**: class

The queue you use to store packets that you successfully transferred to the networking stack.

**Availability**:
- DriverKit ?+

## Declaration

```swift
class IOUserNetworkRxCompletionQueue;
```

#### Overview

Create an [`IOUserNetworkRxCompletionQueue`](iousernetworkrxcompletionqueue.md) object and use it to deliver packets from your hardware device to the networking stack. As data arrives from your hardware, place the data into empty packets that you dequeued from an [`IOUserNetworkRxSubmissionQueue`](iousernetworkrxsubmissionqueue.md) object. Deliver the resulting packets to the system by enqueueing them on your [`IOUserNetworkRxCompletionQueue`](iousernetworkrxcompletionqueue.md) object. After you enqueue the packets, the system transfers the packet data to the networking stack, recycles the packets, and places the packets back in your submission queue.

## Topics

### Creating the Completion Queue
- [Create](iousernetworkrxcompletionqueue/create.md)
  Creates a queue that you use to deliver packets received from your hardware device.
- [init](iousernetworkrxcompletionqueue/init.md)
  Initializes the packet submission queue.
- [free](iousernetworkrxcompletionqueue/free.md)
  Performs any final cleanup for the queue.
### Instance Methods
- [initWithPool](iousernetworkrxcompletionqueue/initwithpool.md)
- [setPacketPoller](iousernetworkrxcompletionqueue/setpacketpoller.md)
### Type Methods
- [withPool](iousernetworkrxcompletionqueue/withpool.md)

## Relationships

### Inherits From
- [IOUserNetworkPacketQueue](iousernetworkpacketqueue.md)

## See Also

- [IOUserNetworkRxSubmissionQueue](iousernetworkrxsubmissionqueue.md)
  The queue that receives packets from the device.
- [IOUserNetworkTxSubmissionQueue](iousernetworktxsubmissionqueue.md)
  The queue that receives packets from the networking stack.
- [IOUserNetworkTxCompletionQueue](iousernetworktxcompletionqueue.md)
  The queue you use to store packets that you successfully transferred to the device.
- [IOUserNetworkPacketQueue](iousernetworkpacketqueue.md)
  The base class for the queues that manage the packets moving to and from your device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkrxcompletionqueue)*