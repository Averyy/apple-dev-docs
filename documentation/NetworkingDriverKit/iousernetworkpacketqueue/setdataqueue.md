# SetDataQueue

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Instance Method

Assigns the specified dispatch source to this object.

**Availability**:
- DriverKit

## Declaration

```c
kern_return_t SetDataQueue(IODataQueueDispatchSource *dataQueue);
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

#### Discussion

Use this method to change the dispatch queue that this object uses to perform tasks. This method releases the previous dispatch queue, if any, and retains the new object in the `dataQueue` parameter.

## Parameters

- `dataQueue`: The new data queue to use when executing tasks.

## See Also

### Managing the Data Queue
- [CopyDataQueue](./copydataqueue.md)
  Returns the dispatch queue that this object uses to execute tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacketqueue/setdataqueue)*