# synchronize()

**Framework**: Open Directory  
**Kind**: method  
**Role**: Instance Method

Restarts a query, disposing of any results it has obtained.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func synchronize()
```

```objc
- (void) synchronize;
```

#### Discussion

If the query was originally scheduled in a run loop with [`schedule(in:forMode:)`](./schedule%28in,formode%29.md), the delegate is called with `inResults` set to `nil`, `[inError code]` set to `kODErrorQuerySynchronize`, and `[inError domain]` set to `kODErrorDomainFramework`.

## See Also

### Managing Asynchronous Queries
- [var delegate: (any ODQueryDelegate)!](./delegate.md)
  The query’s delegate.
- [var operationQueue: OperationQueue!](./operationqueue.md)
  The queue on which asynchronous results are delivered to the delegate.
- [func schedule(in: RunLoop!, forMode: String!)](./schedule%28in,formode%29.md)
  Retrieves results from a query asynchronously by scheduling the query in a run loop.
- [func remove(from: RunLoop!, forMode: String!)](./remove%28from,formode%29.md)
  Removes the query from a specified run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odquery/synchronize())*