# operationQueue

**Framework**: Open Directory  
**Kind**: property

The queue on which asynchronous results are delivered to the delegate.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
var operationQueue: OperationQueue! { get set }
```

## See Also

- [var delegate: (any ODQueryDelegate)!](odquery/delegate.md)
  The query’s delegate.
- [func schedule(in: RunLoop!, forMode: String!)](odquery/schedule(in:formode:).md)
  Retrieves results from a query asynchronously by scheduling the query in a run loop.
- [func remove(from: RunLoop!, forMode: String!)](odquery/remove(from:formode:).md)
  Removes the query from a specified run loop.
- [func synchronize()](odquery/synchronize.md)
  Restarts a query, disposing of any results it has obtained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odquery/operationqueue)*