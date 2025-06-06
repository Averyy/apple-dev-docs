# withPool

**Framework**: NetworkingDriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+

## Declaration

```swift
static IOUserNetworkTxSubmissionQueue * withPool(IOUserNetworkPacketBufferPool * pool, uint32_t capacity, IOUserNetworkPacketQueueId queueId, OSObject * target, QueryFreeSpaceAction freeSpaceAction, DequeueAction dequeueAction, void * refCon, IOOptionBits options);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworktxsubmissionqueue/withpool)*