# Create

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Static Method

**Availability**:
- DriverKit 24.0+

## Declaration

```c
static kern_return_t Create(IOUserNetworkPacketBufferPool *pool, OSObject *owner, IOUserNetworkServiceClass serviceClass, uint32_t capacity, uint32_t queueId, IODispatchQueue *dispatchQueue, IOUserNetworkTxSubmissionQueueCompat **queue);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworktxsubmissionqueuecompat/create-9aa1k)*