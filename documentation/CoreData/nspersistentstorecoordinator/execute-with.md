# execute(_:with:)

**Framework**: Core Data  
**Kind**: method

Executes the specified request on each of the coordinator’s persistent stores.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func execute(_ request: NSPersistentStoreRequest, with context: NSManagedObjectContext) throws -> Any
```

#### Return Value

An array containing managed objects, managed object IDs, or dictionaries as appropriate for a fetch request; an empty array if `request` is a save request, or `nil` if an error occurred.

#### Discussion

User defined requests return arrays of arrays, where a nested array is the result returned from a single store.

## Parameters

- `request`: A fetch or save request.
- `context`: The context against which   should be executed.

## See Also

- [func perform<T>(() throws -> T) async rethrows -> T](nspersistentstorecoordinator/perform(_:)-74udx.md)
  Executes the provided closure asynchronously on the coordinator’s queue and awaits the result.
- [func performAndWait<T>(() throws -> T) rethrows -> T](nspersistentstorecoordinator/performandwait(_:)-15ude.md)
  Executes the provided closure on the coordinator’s queue and waits for it to finish.
- [func perform(() -> Void)](nspersistentstorecoordinator/perform(_:)-7jqb.md)
  Executes the provided closure asynchronously on the coordinator’s queue.
- [func performAndWait(() -> Void)](nspersistentstorecoordinator/performandwait(_:)-d3kq.md)
  Executes the provided closure on the coordinator’s queue and waits for it to finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/execute(_:with:))*