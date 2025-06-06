# CopyDataQueue

**Framework**: NetworkingDriverKit  
**Kind**: method

Returns the dispatch queue that this object uses to execute tasks.

**Availability**:
- DriverKit ?+

## Declaration

```swift
kern_return_t CopyDataQueue(IODataQueueDispatchSource * * dataQueue);
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

## Parameters

- `dataQueue`: On return, a pointer to the dispatch source that this object uses to generate tasks.

## See Also

- [SetDataQueue](iousernetworkpacketqueue/setdataqueue.md)
  Assigns the specified dispatch source to this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacketqueue/copydataqueue)*