# withPoolAndServiceClass

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Static Method

**Availability**:
- DriverKit

## Declaration

```c
static IOUserNetworkTxSubmissionQueue * withPoolAndServiceClass(IOUserNetworkPacketBufferPool *pool, IOUserNetworkServiceClass serviceClass, uint32_t capacity, IOUserNetworkPacketQueueId queueId, OSObject *target, QueryFreeSpaceAction freeSpaceAction, DequeueAction dequeueAction, void *refCon, IOOptionBits options);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworktxsubmissionqueue/withpoolandserviceclass)*