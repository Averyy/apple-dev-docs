# CheckForWork

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Checks for events to handle.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
virtual kern_return_t CheckForWork(bool synchronous);
```

## Return Value

[`kIOReturnSuccess`](../kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../error-codes.md).

## Discussion

Don’t override this method or call it from your own code. The dispatch source uses this method internally to check for events.

## See Also

### Performing Internal Tasks
- [CopyDataAvailableHandler](./copydataavailablehandler.md)
  A private method that the dispatch source uses to detect enqueued data.
- [CopyDataServicedHandler](./copydataservicedhandler.md)
  A private method that the dispatch source uses to detect dequeued data.
- [CopyMemory](./copymemory.md)
  A private method that the dispatch source uses to copy memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodataqueuedispatchsource/checkforwork)*