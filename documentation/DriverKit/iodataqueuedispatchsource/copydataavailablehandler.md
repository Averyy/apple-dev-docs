# CopyDataAvailableHandler

**Framework**: DriverKit  
**Kind**: method

A private method that the dispatch source uses to detect enqueued data.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t CopyDataAvailableHandler(OSAction * * action);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. See [`Error Codes`](error-codes.md).

## See Also

- [CopyDataServicedHandler](iodataqueuedispatchsource/copydataservicedhandler.md)
  A private method that the dispatch source uses to detect dequeued data.
- [CopyMemory](iodataqueuedispatchsource/copymemory.md)
  A private method that the dispatch source uses to copy memory.
- [CheckForWork](iodataqueuedispatchsource/checkforwork.md)
  Checks for events to handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodataqueuedispatchsource/copydataavailablehandler)*