# ODQueryGetTypeID()

**Framework**: Open Directory  
**Kind**: func  
**Role**: Function

Returns the type ID for an Open Directory query.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func ODQueryGetTypeID() -> CFTypeID
```

```c
extern CFTypeID ODQueryGetTypeID();
```

#### Return Value

The type ID for an Open Directory query.

## See Also

### Working with Queries
- [func ODQueryCopyResults(ODQueryRef!, Bool, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](./odquerycopyresults%28_,_,_%29.md)
  Returns results from a query synchronously.
- [func ODQueryCreateWithNode(CFAllocator!, ODNodeRef!, CFTypeRef!, String!, ODMatchType, CFTypeRef!, CFTypeRef!, CFIndex, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODQueryRef>!](./odquerycreatewithnode%28_,_,_,_,_,_,_,_,_%29.md)
  Creates a query with a node using provided parameters.
- [func ODQueryCreateWithNodeType(CFAllocator!, ODNodeType, CFTypeRef!, String!, ODMatchType, CFTypeRef!, CFTypeRef!, CFIndex, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODQueryRef>!](./odquerycreatewithnodetype%28_,_,_,_,_,_,_,_,_%29.md)
  Creates a query for a particular node type using provided parameters.
- [func ODQueryScheduleWithRunLoop(ODQueryRef!, CFRunLoop!, CFString!)](./odqueryschedulewithrunloop%28_,_,_%29.md)
  Retrieves results from a query asynchronously by scheduling the query in a run loop.
- [func ODQuerySetCallback(ODQueryRef!, ODQueryCallback!, UnsafeMutableRawPointer!)](./odquerysetcallback%28_,_,_%29.md)
  Sets the callback for an asynchronous query.
- [func ODQuerySetDispatchQueue(ODQueryRef!, dispatch_queue_t!)](./odquerysetdispatchqueue%28_,_%29.md)
  Retrieves results from a query asynchronously by adding the query to a dispatch queue.
- [func ODQuerySynchronize(ODQueryRef!)](./odquerysynchronize%28_%29.md)
  Restarts a query, disposing of any results it has obtained.
- [func ODQueryUnscheduleFromRunLoop(ODQueryRef!, CFRunLoop!, CFString!)](./odqueryunschedulefromrunloop%28_,_,_%29.md)
  Removes a query from a specified run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odquerygettypeid())*