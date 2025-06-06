# initWithPool

**Framework**: NetworkingDriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+

## Declaration

```swift
bool initWithPool(IOUserNetworkPacketBufferPool * pool, IOUserNetworkServiceClass serviceClass, uint32_t capacity, IOUserNetworkPacketQueueId queueId, OSObject * target, QueryFreeSpaceAction freeSpaceAction, DequeueAction dequeueAction, void * refCon, IOOptionBits options);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworktxsubmissionqueue/initwithpool)*