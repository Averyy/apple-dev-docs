# Create

**Framework**: NetworkingDriverKit  
**Kind**: method

Creates a queue that delivers empty packets for you to fill with data from your hardware device.

**Availability**:
- DriverKit ?+

## Declaration

```swift
static kern_return_t Create(IOUserNetworkPacketBufferPool * pool, OSObject * owner, uint32_t capacity, uint32_t queueId, IODispatchQueue * dispatchQueue, IOUserNetworkRxSubmissionQueue * * queue);
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

## Parameters

- `pool`: The buffer pool containing the memory for the network packets. This parameter must not be  .
- `owner`: The object to use as the owner of the queue.
- `capacity`: The number of packets in the queue.
- `queueId`: An identifier for you to use to distinguish the queue from other queues. Specify   if you don’t use this parameter.
- `dispatchQueue`: The dispatch queue on which to execute tasks.
- `queue`: On return, the new queue object. It is a programmer error to specify   for this parameter.

## See Also

- [init](iousernetworkrxsubmissionqueue/init.md)
  Initializes the packet submission queue.
- [free](iousernetworkrxsubmissionqueue/free.md)
  Performs any final cleanup for the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkrxsubmissionqueue/create)*