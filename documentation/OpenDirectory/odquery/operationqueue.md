# operationQueue

**Framework**: Open Directory  
**Kind**: property  
**Role**: Instance Property

The queue on which asynchronous results are delivered to the delegate.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
var operationQueue: OperationQueue! { get set }
```

```objc
@property (retain, readwrite) NSOperationQueue * operationQueue;
```

## See Also

### Managing Asynchronous Queries
- [var delegate: (any ODQueryDelegate)!](./delegate.md)
  The query’s delegate.
- [func schedule(in: RunLoop!, forMode: String!)](./schedule%28in,formode%29.md)
  Retrieves results from a query asynchronously by scheduling the query in a run loop.
- [func remove(from: RunLoop!, forMode: String!)](./remove%28from,formode%29.md)
  Removes the query from a specified run loop.
- [func synchronize()](./synchronize%28%29.md)
  Restarts a query, disposing of any results it has obtained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odquery/operationqueue)*