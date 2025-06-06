# init

**Framework**: NetworkingDriverKit  
**Kind**: method

Initializes the packet submission queue.

**Availability**:
- DriverKit ?+

## Declaration

```swift
bool init();
```

#### Return Value

`YES` if initialization was successful, or `NO` if it wasn’t.

#### Discussion

Don’t call this method directly. Instead, use the `IOUserNetworkTxSubmissionQueue/Create` method to create a new [`IOUserNetworkTxSubmissionQueue`](iousernetworktxsubmissionqueue.md) object.

## See Also

- [free](iousernetworktxsubmissionqueue/free.md)
  Performs any final cleanup for the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworktxsubmissionqueue/init)*