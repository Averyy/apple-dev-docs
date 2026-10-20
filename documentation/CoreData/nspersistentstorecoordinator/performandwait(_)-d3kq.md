# performAndWait(_:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Executes the provided closure on the coordinator’s queue and waits for it to finish.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

> **Deprecated**: Use [`performAndWait(_:)`](./performandwait%28_%29-15ude.md) instead.

## Declaration

```swift
func performAndWait(_ block: @Sendable () -> Void)
```

```objc
- (void) performBlockAndWait:(void (^)()) block;
```

## Parameters

- `block`: The closure to execute.

## See Also

### Performing tasks
- [func perform<T>(() throws -> T) async rethrows -> T](./perform%28_%29-74udx.md)
  Executes the provided closure asynchronously on the coordinator’s queue and awaits the result.
- [func performAndWait<T>(() throws -> T) rethrows -> T](./performandwait%28_%29-15ude.md)
  Executes the provided closure on the coordinator’s queue and waits for it to finish.
- [func perform(() -> Void)](./perform%28_%29-7jqb.md)
  Executes the provided closure asynchronously on the coordinator’s queue.
- [func execute(NSPersistentStoreRequest, with: NSManagedObjectContext) throws -> Any](./execute%28_,with%29.md)
  Executes the specified request on each of the coordinator’s persistent stores.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/performandwait(_:)-d3kq)*