# CopyMemory

**Framework**: DriverKit  
**Kind**: method

A private method that the dispatch source uses to copy memory.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t CopyMemory(IOMemoryDescriptor * * memory);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. See [`Error Codes`](error-codes.md).

## See Also

- [CopyDataAvailableHandler](iodataqueuedispatchsource/copydataavailablehandler.md)
  A private method that the dispatch source uses to detect enqueued data.
- [CopyDataServicedHandler](iodataqueuedispatchsource/copydataservicedhandler.md)
  A private method that the dispatch source uses to detect dequeued data.
- [CheckForWork](iodataqueuedispatchsource/checkforwork.md)
  Checks for events to handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodataqueuedispatchsource/copymemory)*