# Create

**Framework**: NetworkingDriverKit  
**Kind**: method

**Availability**:
- DriverKit 24.0+

## Declaration

```swift
static kern_return_t Create(IOUserNetworkPacketBufferPool * pool, OSObject * owner, IOUserNetworkServiceClass serviceClass, uint32_t capacity, uint32_t queueId, IODispatchQueue * dispatchQueue, IOUserNetworkTxSubmissionQueueCompat * * queue);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworktxsubmissionqueuecompat/create-9aa1k)*