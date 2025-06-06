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

Don’t call this method directly. Instead, use the [`Create`](iousernetworkrxsubmissionqueue/create.md) method of the appropriate subclass.

## See Also

- [free](iousernetworkpacketqueue/free.md)
  Performs any final cleanup for the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacketqueue/init)*