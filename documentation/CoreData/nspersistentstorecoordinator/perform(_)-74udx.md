# perform(_:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Executes the provided closure asynchronously on the coordinator’s queue and awaits the result.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

## Declaration

```swift
@preconcurrency
func perform<T>(_ block: @escaping @Sendable () throws -> T) async rethrows -> T
```

## Parameters

- `block`: The closure to execute.

## See Also

### Performing tasks
- [func performAndWait<T>(() throws -> T) rethrows -> T](./performandwait%28_%29-15ude.md)
  Executes the provided closure on the coordinator’s queue and waits for it to finish.
- [func perform(() -> Void)](./perform%28_%29-7jqb.md)
  Executes the provided closure asynchronously on the coordinator’s queue.
- [func performAndWait(() -> Void)](./performandwait%28_%29-d3kq.md)
  Executes the provided closure on the coordinator’s queue and waits for it to finish.
- [func execute(NSPersistentStoreRequest, with: NSManagedObjectContext) throws -> Any](./execute%28_,with%29.md)
  Executes the specified request on each of the coordinator’s persistent stores.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/perform(_:)-74udx)*