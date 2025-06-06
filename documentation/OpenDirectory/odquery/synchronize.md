# synchronize()

**Framework**: Open Directory  
**Kind**: method

Restarts a query, disposing of any results it has obtained.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func synchronize()
```

#### Discussion

If the query was originally scheduled in a run loop with [`schedule(in:forMode:)`](odquery/schedule(in:formode:).md), the delegate is called with `inResults` set to `nil`, `[inError code]` set to `kODErrorQuerySynchronize`, and `[inError domain]` set to `kODErrorDomainFramework`.

## See Also

- [var delegate: (any ODQueryDelegate)!](odquery/delegate.md)
  The query’s delegate.
- [var operationQueue: OperationQueue!](odquery/operationqueue.md)
  The queue on which asynchronous results are delivered to the delegate.
- [func schedule(in: RunLoop!, forMode: String!)](odquery/schedule(in:formode:).md)
  Retrieves results from a query asynchronously by scheduling the query in a run loop.
- [func remove(from: RunLoop!, forMode: String!)](odquery/remove(from:formode:).md)
  Removes the query from a specified run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odquery/synchronize())*