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

Don’t call this method directly. Instead, use the [`Create`](iousernetworkrxcompletionqueue/create.md) method to create a new [`IOUserNetworkRxCompletionQueue`](iousernetworkrxcompletionqueue.md) object.

## See Also

- [Create](iousernetworkrxcompletionqueue/create.md)
  Creates a queue that you use to deliver packets received from your hardware device.
- [free](iousernetworkrxcompletionqueue/free.md)
  Performs any final cleanup for the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkrxcompletionqueue/init)*