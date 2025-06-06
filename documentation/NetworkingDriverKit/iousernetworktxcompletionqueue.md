# IOUserNetworkTxCompletionQueue

**Framework**: NetworkingDriverKit  
**Kind**: class

The queue you use to store packets that you successfully transferred to the device.

**Availability**:
- DriverKit ?+

## Declaration

```swift
class IOUserNetworkTxCompletionQueue;
```

#### Overview

Create an [`IOUserNetworkTxCompletionQueue`](iousernetworktxcompletionqueue.md) object and use it to return packets back to the system after sending them to your hardware. The system recycles the packets you place on this queue, reusing them for new packets that it places in your [`IOUserNetworkTxSubmissionQueue`](iousernetworktxsubmissionqueue.md).

## Topics

### Creating the Completion Queue
- [Create](iousernetworktxcompletionqueue/create.md)
  Creates a queue that tells the system which packets you transmitted to your device.
- [init](iousernetworktxcompletionqueue/init.md)
  Initializes the packet submission queue.
- [free](iousernetworktxcompletionqueue/free.md)
  Performs any final cleanup for the queue.
### Instance Methods
- [initWithPool](iousernetworktxcompletionqueue/initwithpool.md)
- [setPacketPoller](iousernetworktxcompletionqueue/setpacketpoller.md)
### Type Methods
- [withPool](iousernetworktxcompletionqueue/withpool.md)

## Relationships

### Inherits From
- [IOUserNetworkPacketQueue](iousernetworkpacketqueue.md)

## See Also

- [IOUserNetworkRxSubmissionQueue](iousernetworkrxsubmissionqueue.md)
  The queue that receives packets from the device.
- [IOUserNetworkRxCompletionQueue](iousernetworkrxcompletionqueue.md)
  The queue you use to store packets that you successfully transferred to the networking stack.
- [IOUserNetworkTxSubmissionQueue](iousernetworktxsubmissionqueue.md)
  The queue that receives packets from the networking stack.
- [IOUserNetworkPacketQueue](iousernetworkpacketqueue.md)
  The base class for the queues that manage the packets moving to and from your device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworktxcompletionqueue)*