# remove(from:forMode:)

**Framework**: Open Directory  
**Kind**: method

Removes the query from a specified run loop.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func remove(from inRunLoop: RunLoop!, forMode inMode: String!)
```

## Parameters

- `inRunLoop`: The run loop.
- `inMode`: The mode to remove the query from.

## See Also

- [var delegate: (any ODQueryDelegate)!](odquery/delegate.md)
  The query’s delegate.
- [var operationQueue: OperationQueue!](odquery/operationqueue.md)
  The queue on which asynchronous results are delivered to the delegate.
- [func schedule(in: RunLoop!, forMode: String!)](odquery/schedule(in:formode:).md)
  Retrieves results from a query asynchronously by scheduling the query in a run loop.
- [func synchronize()](odquery/synchronize.md)
  Restarts a query, disposing of any results it has obtained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odquery/remove(from:formode:))*