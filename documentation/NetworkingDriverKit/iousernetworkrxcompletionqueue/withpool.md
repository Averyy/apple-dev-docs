# withPool

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Static Method

**Availability**:
- DriverKit

## Declaration

```c
static IOUserNetworkRxCompletionQueue * withPool(IOUserNetworkPacketBufferPool *pool, uint32_t capacity, IOUserNetworkPacketQueueId queueId, OSObject *target, EnqueueAction action, void *refCon, IOOptionBits options);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkrxcompletionqueue/withpool)*