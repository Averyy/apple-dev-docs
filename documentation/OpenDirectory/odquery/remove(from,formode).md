# remove(from:forMode:)

**Framework**: Open Directory  
**Kind**: method  
**Role**: Instance Method

Removes the query from a specified run loop.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func remove(from inRunLoop: RunLoop!, forMode inMode: String!)
```

```objc
- (void) removeFromRunLoop:(NSRunLoop *) inRunLoop forMode:(NSString *) inMode;
```

## Parameters

- `inRunLoop`: The run loop.
- `inMode`: The mode to remove the query from.

## See Also

### Managing Asynchronous Queries
- [var delegate: (any ODQueryDelegate)!](./delegate.md)
  The query’s delegate.
- [var operationQueue: OperationQueue!](./operationqueue.md)
  The queue on which asynchronous results are delivered to the delegate.
- [func schedule(in: RunLoop!, forMode: String!)](./schedule%28in,formode%29.md)
  Retrieves results from a query asynchronously by scheduling the query in a run loop.
- [func synchronize()](./synchronize%28%29.md)
  Restarts a query, disposing of any results it has obtained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odquery/remove(from:formode:))*