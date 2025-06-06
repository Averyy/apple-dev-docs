# didAdd(to:)

**Framework**: Core Data  
**Kind**: method

Invoked after the persistent store has been added to the persistent store coordinator.

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
func didAdd(to coordinator: NSPersistentStoreCoordinator)
```

#### Discussion

The default implementation does nothing. You can override this method in a subclass in order to perform any kind of setup necessary before the load method is invoked.

## Parameters

- `coordinator`: The persistent store coordinator to which the receiver was added.

## See Also

- [func willRemove(from: NSPersistentStoreCoordinator?)](nspersistentstore/willremove(from:).md)
  Invoked before the persistent store is removed from the persistent store coordinator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstore/didadd(to:))*