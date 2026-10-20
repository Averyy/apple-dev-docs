# NSFileProviderTestingOperationType.deletion

**Framework**: File Provider  
**Kind**: case  
**Role**: Case

Propagates the deletion of the source item from the target location.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
case deletion
```

```c
NSFileProviderTestingOperationTypeDeletion
```

## See Also

### Types
- [NSFileProviderTestingOperationType.childrenEnumeration](./childrenenumeration.md)
  Lists an item’s content.
- [NSFileProviderTestingOperationType.collisionResolution](./collisionresolution.md)
  Resolves a collision by renaming the new item.
- [NSFileProviderTestingOperationType.contentFetch](./contentfetch.md)
  Fetches an item’s content.
- [NSFileProviderTestingOperationType.creation](./creation.md)
  Propagates the creation of a source item to the target location.
- [NSFileProviderTestingOperationType.ingestion](./ingestion.md)
  Alerts the system to changes to either the local or remote storage.
- [NSFileProviderTestingOperationType.lookup](./lookup.md)
  Looks up an item.
- [NSFileProviderTestingOperationType.modification](./modification.md)
  Propagates a change from the source item to the target location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidertestingoperationtype/deletion)*