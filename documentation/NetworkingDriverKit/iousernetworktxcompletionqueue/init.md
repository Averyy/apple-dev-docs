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

Don’t call this method directly. Instead, use the [`Create`](iousernetworktxcompletionqueue/create.md) method to create a new [`IOUserNetworkTxCompletionQueue`](iousernetworktxcompletionqueue.md) object.

## See Also

- [Create](iousernetworktxcompletionqueue/create.md)
  Creates a queue that tells the system which packets you transmitted to your device.
- [free](iousernetworktxcompletionqueue/free.md)
  Performs any final cleanup for the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworktxcompletionqueue/init)*