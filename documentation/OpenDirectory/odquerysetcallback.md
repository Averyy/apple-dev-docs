# ODQuerySetCallback(_:_:_:)

**Framework**: Open Directory  
**Kind**: func

Sets the callback for an asynchronous query.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func ODQuerySetCallback(_ query: ODQueryRef!, _ callback: ODQueryCallback!, _ userInfo: UnsafeMutableRawPointer!)
```

## Parameters

- `query`: The query.
- `callback`: The callback function.
- `userInfo`: A user-defined pointer to be passed back to the callback function.

## See Also

- [typealias ODQueryCallback](odquerycallback.md)
  A callback function called as results from a scheduled query are returned.
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
- [func ODQuerySetDispatchQueue(ODQueryRef!, dispatch_queue_t!)](odquerysetdispatchqueue(_:_:).md)
  Retrieves results from a query asynchronously by adding the query to a dispatch queue.
- [func ODQuerySynchronize(ODQueryRef!)](odquerysynchronize(_:).md)
  Restarts a query, disposing of any results it has obtained.
- [func ODQueryUnscheduleFromRunLoop(ODQueryRef!, CFRunLoop!, CFString!)](odqueryunschedulefromrunloop(_:_:_:).md)
  Removes a query from a specified run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odquerysetcallback(_:_:_:))*