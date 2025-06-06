# performAndWait(_:)

**Framework**: Core Data  
**Kind**: method

Executes the provided closure on the coordinator’s queue and waits for it to finish.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
func performAndWait<T>(_ block: () throws -> T) rethrows -> T
```

## Parameters

- `block`: The closure to execute.

## See Also

- [func perform<T>(() throws -> T) async rethrows -> T](nspersistentstorecoordinator/perform(_:)-74udx.md)
  Executes the provided closure asynchronously on the coordinator’s queue and awaits the result.
- [func perform(() -> Void)](nspersistentstorecoordinator/perform(_:)-7jqb.md)
  Executes the provided closure asynchronously on the coordinator’s queue.
- [func performAndWait(() -> Void)](nspersistentstorecoordinator/performandwait(_:)-d3kq.md)
  Executes the provided closure on the coordinator’s queue and waits for it to finish.
- [func execute(NSPersistentStoreRequest, with: NSManagedObjectContext) throws -> Any](nspersistentstorecoordinator/execute(_:with:).md)
  Executes the specified request on each of the coordinator’s persistent stores.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/performandwait(_:)-15ude)*