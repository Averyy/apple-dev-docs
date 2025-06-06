# ODQueryUnscheduleFromRunLoop(_:_:_:)

**Framework**: Open Directory  
**Kind**: func

Removes a query from a specified run loop.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func ODQueryUnscheduleFromRunLoop(_ query: ODQueryRef!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!)
```

## Parameters

- `query`: The query.
- `runLoop`: The run loop.
- `runLoopMode`: The mode to remove the query from.

## See Also

- [func ODQueryCopyResults(ODQueryRef!, Bool, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](odquerycopyresults(_:_:_:).md)
  Returns results from a query synchronously.
- [func ODQueryCreateWithNode(CFAllocator!, ODNodeRef!, CFTypeRef!, String!, ODMatchType, CFTypeRef!, CFTypeRef!, CFIndex, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODQueryRef>!](odquerycreatewithnode(_:_:_:_:_:_:_:_:_:).md)
  Creates a query with a node using provided parameters.
- [func ODQueryCreateWithNodeType(CFAllocator!, ODNodeType, CFTypeRef!, String!, ODMatchType, CFTypeRef!, CFTypeRef!, CFIndex, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODQueryRef>!](odquerycreatewithnodetype(_:_:_:_:_:_:_:_:_:).md)
  Creates a query for a particular node type using provided parameters.
- [func ODQueryGetTypeID() -> CFTypeID](odquerygettypeid().md)
  Returns the type ID for an Open Directory query.
- [func ODQueryScheduleWithRunLoop(ODQueryRef!, CFRunLoop!, CFString!)](odqueryschedulewithrunloop(_:_:_:).md)
  Retrieves results from a query asynchronously by scheduling the query in a run loop.
- [func ODQuerySetCallback(ODQueryRef!, ODQueryCallback!, UnsafeMutableRawPointer!)](odquerysetcallback(_:_:_:).md)
  Sets the callback for an asynchronous query.
- [func ODQuerySetDispatchQueue(ODQueryRef!, dispatch_queue_t!)](odquerysetdispatchqueue(_:_:).md)
  Retrieves results from a query asynchronously by adding the query to a dispatch queue.
- [func ODQuerySynchronize(ODQueryRef!)](odquerysynchronize(_:).md)
  Restarts a query, disposing of any results it has obtained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odqueryunschedulefromrunloop(_:_:_:))*