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

#### Return Value

`YES` if initialization was successful, or `NO` if it wasn’t.

#### Discussion

Don’t call this method directly. Instead, use the [`Create`](./create.md) method to create a new [`IOUserNetworkRxSubmissionQueue`](../iousernetworkrxsubmissionqueue.md) object.

## See Also

### Creating the Submission Queue
- [Create](./create.md)
  Creates a queue that delivers empty packets for you to fill with data from your hardware device.
- [free](./free.md)
  Performs any final cleanup for the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkrxsubmissionqueue/init)*