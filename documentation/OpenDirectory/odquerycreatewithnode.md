# ODQueryCreateWithNode(_:_:_:_:_:_:_:_:_:)

**Framework**: Open Directory  
**Kind**: func

Creates a query with a node using provided parameters.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func ODQueryCreateWithNode(_ allocator: CFAllocator!, _ node: ODNodeRef!, _ recordTypeOrList: CFTypeRef!, _ attribute: String!, _ matchType: ODMatchType, _ queryValueOrList: CFTypeRef!, _ returnAttributeOrList: CFTypeRef!, _ maxResults: CFIndex, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODQueryRef>!
```

#### Return Value

The created query.

## Parameters

- `allocator`: The memory allocator to use. If  , the default allocator is used.
- `node`: The node.
- `recordTypeOrList`: The type or types of record to query. Can be a   object for a single type or a   object containing   objects for multiple types.
- `attribute`: The name of the attribute to query.
- `matchType`: The type of query.
- `queryValueOrList`: The value or values to query in the attribute. Can be a   object or a   object for a single value, or a   containing   and   objects for multiple values.
- `returnAttributeOrList`: The attribute or attributes to be returned from the query. Can be a   object for a single attribute or a   object containing   objects for multiple attributes. Passing   is equivalent to passing  .
- `maxResults`: The maximum number of values to be returned.
- `error`: An error reference for error details. Can be  .

## See Also

- [func ODQueryCopyResults(ODQueryRef!, Bool, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](odquerycopyresults(_:_:_:).md)
  Returns results from a query synchronously.
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
- [func ODQueryUnscheduleFromRunLoop(ODQueryRef!, CFRunLoop!, CFString!)](odqueryunschedulefromrunloop(_:_:_:).md)
  Removes a query from a specified run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odquerycreatewithnode(_:_:_:_:_:_:_:_:_:))*