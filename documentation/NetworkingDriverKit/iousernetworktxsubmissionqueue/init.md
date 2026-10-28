# init

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Instance Method

Initializes the packet submission queue.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual bool init();
```

## Return Value

`YES` if initialization was successful, or `NO` if it wasn’t.

## Discussion

Don’t call this method directly. Instead, use the `IOUserNetworkTxSubmissionQueue/Create` method to create a new [`IOUserNetworkTxSubmissionQueue`](../iousernetworktxsubmissionqueue.md) object.

## See Also

### Creating the Submission Queue
- [free](./free.md)
  Performs any final cleanup for the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworktxsubmissionqueue/init)*