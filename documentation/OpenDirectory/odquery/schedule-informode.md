# schedule(in:forMode:)

**Framework**: Open Directory  
**Kind**: method

Retrieves results from a query asynchronously by scheduling the query in a run loop.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func schedule(in inRunLoop: RunLoop!, forMode inMode: String!)
```

#### Discussion

A delegate must be set prior to calling this method; otherwise, results may be lost due to the lack of a receiver.

## Parameters

- `inRunLoop`: The run loop.
- `inMode`: The mode of the run loop.

## See Also

- [var delegate: (any ODQueryDelegate)!](odquery/delegate.md)
  The query’s delegate.
- [var operationQueue: OperationQueue!](odquery/operationqueue.md)
  The queue on which asynchronous results are delivered to the delegate.
- [func remove(from: RunLoop!, forMode: String!)](odquery/remove(from:formode:).md)
  Removes the query from a specified run loop.
- [func synchronize()](odquery/synchronize.md)
  Restarts a query, disposing of any results it has obtained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odquery/schedule(in:formode:))*