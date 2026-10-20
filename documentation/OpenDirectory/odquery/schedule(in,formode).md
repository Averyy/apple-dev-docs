# schedule(in:forMode:)

**Framework**: Open Directory  
**Kind**: method  
**Role**: Instance Method

Retrieves results from a query asynchronously by scheduling the query in a run loop.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func schedule(in inRunLoop: RunLoop!, forMode inMode: String!)
```

```objc
- (void) scheduleInRunLoop:(NSRunLoop *) inRunLoop forMode:(NSString *) inMode;
```

#### Discussion

A delegate must be set prior to calling this method; otherwise, results may be lost due to the lack of a receiver.

## Parameters

- `inRunLoop`: The run loop.
- `inMode`: The mode of the run loop.

## See Also

### Managing Asynchronous Queries
- [var delegate: (any ODQueryDelegate)!](./delegate.md)
  The query’s delegate.
- [var operationQueue: OperationQueue!](./operationqueue.md)
  The queue on which asynchronous results are delivered to the delegate.
- [func remove(from: RunLoop!, forMode: String!)](./remove%28from,formode%29.md)
  Removes the query from a specified run loop.
- [func synchronize()](./synchronize%28%29.md)
  Restarts a query, disposing of any results it has obtained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odquery/schedule(in:formode:))*