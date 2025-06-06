# perform(_:)

**Framework**: Core Data  
**Kind**: method

Executes the provided closure asynchronously on the coordinator’s queue.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func perform(_ block: @escaping () -> Void)
```

## Parameters

- `block`: The closure to execute.

## See Also

- [func perform<T>(() throws -> T) async rethrows -> T](nspersistentstorecoordinator/perform(_:)-74udx.md)
  Executes the provided closure asynchronously on the coordinator’s queue and awaits the result.
- [func performAndWait<T>(() throws -> T) rethrows -> T](nspersistentstorecoordinator/performandwait(_:)-15ude.md)
  Executes the provided closure on the coordinator’s queue and waits for it to finish.
- [func performAndWait(() -> Void)](nspersistentstorecoordinator/performandwait(_:)-d3kq.md)
  Executes the provided closure on the coordinator’s queue and waits for it to finish.
- [func execute(NSPersistentStoreRequest, with: NSManagedObjectContext) throws -> Any](nspersistentstorecoordinator/execute(_:with:).md)
  Executes the specified request on each of the coordinator’s persistent stores.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/perform(_:)-7jqb)*