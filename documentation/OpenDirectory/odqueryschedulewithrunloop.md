# ODQueryScheduleWithRunLoop(_:_:_:)

**Framework**: Open Directory  
**Kind**: func

Retrieves results from a query asynchronously by scheduling the query in a run loop.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func ODQueryScheduleWithRunLoop(_ query: ODQueryRef!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!)
```

#### Discussion

This function spawns a new thread to execute the query in `inRunLoop`. When the query is complete, the query’s callback function is called with both `inResults` and `inError` set to `NULL`. To remove an incomplete query from its run loop, call [`ODQueryUnscheduleFromRunLoop(_:_:_:)`](odqueryunschedulefromrunloop(_:_:_:).md).

## Parameters

- `query`: The query.
- `runLoop`: The run loop.
- `runLoopMode`: The mode of the run loop.

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
- [func ODQuerySetCallback(ODQueryRef!, ODQueryCallback!, UnsafeMutableRawPointer!)](odquerysetcallback(_:_:_:).md)
  Sets the callback for an asynchronous query.
- [func ODQuerySetDispatchQueue(ODQueryRef!, dispatch_queue_t!)](odquerysetdispatchqueue(_:_:).md)
  Retrieves results from a query asynchronously by adding the query to a dispatch queue.
- [func ODQuerySynchronize(ODQueryRef!)](odquerysynchronize(_:).md)
  Restarts a query, disposing of any results it has obtained.
- [func ODQueryUnscheduleFromRunLoop(ODQueryRef!, CFRunLoop!, CFString!)](odqueryunschedulefromrunloop(_:_:_:).md)
  Removes a query from a specified run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odqueryschedulewithrunloop(_:_:_:))*