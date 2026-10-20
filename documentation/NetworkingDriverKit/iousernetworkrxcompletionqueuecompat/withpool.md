# withPool

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Static Method

**Availability**:
- DriverKit

## Declaration

```c
static IOUserNetworkRxCompletionQueueCompat * withPool(IOUserNetworkPacketBufferPool *pool, uint32_t capacity, IOUserNetworkPacketQueueCompatId queueId, OSObject *target, EnqueueActionCompat action, void *refCon, IOOptionBits options);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkrxcompletionqueuecompat/withpool)*