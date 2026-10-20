# withPool

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Static Method

**Availability**:
- DriverKit

## Declaration

```c
static IOUserNetworkTxCompletionQueueCompat * withPool(IOUserNetworkPacketBufferPool *pool, uint32_t capacity, IOUserNetworkPacketQueueCompatId queueId, OSObject *target, EnqueueActionCompat enqueueAction, void *refCon, IOOptionBits options);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworktxcompletionqueuecompat/withpool)*