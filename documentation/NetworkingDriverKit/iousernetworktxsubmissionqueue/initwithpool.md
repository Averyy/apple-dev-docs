# initWithPool

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- DriverKit

## Declaration

```cpp
virtual bool initWithPool(IOUserNetworkPacketBufferPool *pool, IOUserNetworkServiceClass serviceClass, uint32_t capacity, IOUserNetworkPacketQueueId queueId, OSObject *target, QueryFreeSpaceAction freeSpaceAction, DequeueAction dequeueAction, void *refCon, IOOptionBits options);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworktxsubmissionqueue/initwithpool)*