# ODQuerySynchronize(_:)

**Framework**: Open Directory  
**Kind**: func  
**Role**: Function

Restarts a query, disposing of any results it has obtained.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func ODQuerySynchronize(_ query: ODQueryRef!)
```

```c
extern void ODQuerySynchronize(ODQueryRef query);
```

## Discussion

If `inQuery` was originally scheduled in a run loop with [`ODQueryScheduleWithRunLoop(_:_:_:)`](./odqueryschedulewithrunloop%28_,_,_%29.md), the query’s callback function is called with `inResults` set to `NULL`, `inError.error` set to `kODErrorQuerySynchronize`, and `inError.domain` set to `kODErrorDomainFramework`.

## Parameters

- `query`: The query.

## See Also

### Working with Queries
- [func ODQueryCopyResults(ODQueryRef!, Bool, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](./odquerycopyresults%28_,_,_%29.md)
  Returns results from a query synchronously.
- [func ODQueryCreateWithNode(CFAllocator!, ODNodeRef!, CFTypeRef!, String!, ODMatchType, CFTypeRef!, CFTypeRef!, CFIndex, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODQueryRef>!](./odquerycreatewithnode%28_,_,_,_,_,_,_,_,_%29.md)
  Creates a query with a node using provided parameters.
- [func ODQueryCreateWithNodeType(CFAllocator!, ODNodeType, CFTypeRef!, String!, ODMatchType, CFTypeRef!, CFTypeRef!, CFIndex, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODQueryRef>!](./odquerycreatewithnodetype%28_,_,_,_,_,_,_,_,_%29.md)
  Creates a query for a particular node type using provided parameters.
- [func ODQueryGetTypeID() -> CFTypeID](./odquerygettypeid%28%29.md)
  Returns the type ID for an Open Directory query.
- [func ODQueryScheduleWithRunLoop(ODQueryRef!, CFRunLoop!, CFString!)](./odqueryschedulewithrunloop%28_,_,_%29.md)
  Retrieves results from a query asynchronously by scheduling the query in a run loop.
- [func ODQuerySetCallback(ODQueryRef!, ODQueryCallback!, UnsafeMutableRawPointer!)](./odquerysetcallback%28_,_,_%29.md)
  Sets the callback for an asynchronous query.
- [func ODQuerySetDispatchQueue(ODQueryRef!, dispatch_queue_t!)](./odquerysetdispatchqueue%28_,_%29.md)
  Retrieves results from a query asynchronously by adding the query to a dispatch queue.
- [func ODQueryUnscheduleFromRunLoop(ODQueryRef!, CFRunLoop!, CFString!)](./odqueryunschedulefromrunloop%28_,_,_%29.md)
  Removes a query from a specified run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odquerysynchronize(_:))*