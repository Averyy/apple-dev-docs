# willRemove(from:)

**Framework**: Core Data  
**Kind**: method

Invoked before the persistent store is removed from the persistent store coordinator.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func willRemove(from coordinator: NSPersistentStoreCoordinator?)
```

#### Discussion

The default implementation does nothing. You can override this method in a subclass in order to perform any clean-up before the store is removed from the coordinator (and deallocated).

## Parameters

- `coordinator`: The persistent store coordinator from which the receiver was removed.

## See Also

- [func didAdd(to: NSPersistentStoreCoordinator)](nspersistentstore/didadd(to:).md)
  Invoked after the persistent store has been added to the persistent store coordinator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstore/willremove(from:))*