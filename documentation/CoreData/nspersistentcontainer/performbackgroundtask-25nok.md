# performBackgroundTask(_:)

**Framework**: Core Data  
**Kind**: method

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
func performBackgroundTask<T>(_ block: @escaping (NSManagedObjectContext) throws -> T) async rethrows -> T
```

## See Also

- [func performBackgroundTask((NSManagedObjectContext) -> Void)](nspersistentcontainer/performbackgroundtask(_:)-39sch.md)
  Executes a closure on a private queue using an ephemeral managed object context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcontainer/performbackgroundtask(_:)-25nok)*