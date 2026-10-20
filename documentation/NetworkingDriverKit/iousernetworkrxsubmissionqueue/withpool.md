# withPool

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Static Method

**Availability**:
- DriverKit

## Declaration

```c
static IOUserNetworkRxSubmissionQueue * withPool(IOUserNetworkPacketBufferPool *pool, uint32_t capacity, uint32_t bufferCount, IOUserNetworkPacketQueueId queueId, OSObject *target, DequeueAction dequeueAction, void *refCon, IOOptionBits options);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkrxsubmissionqueue/withpool)*