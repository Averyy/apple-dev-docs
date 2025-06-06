# NSPersistentHistoryChangeType

**Framework**: Core Data  
**Kind**: enum

The types of changes to managed objects reflected in persistent history.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
enum NSPersistentHistoryChangeType
```

## Topics

### Change Types
- [NSPersistentHistoryChangeType.delete](nspersistenthistorychangetype/delete.md)
  The deletion of a managed object from the persistent store.
- [NSPersistentHistoryChangeType.insert](nspersistenthistorychangetype/insert.md)
  The insertion of a managed object into the persistent store.
- [NSPersistentHistoryChangeType.update](nspersistenthistorychangetype/update.md)
  An update to a managed object’s properties in the persistent store.
### Initializers
- [init?(rawValue: Int)](nspersistenthistorychangetype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var changeID: Int64](nspersistenthistorychange/changeid.md)
  The change’s numeric identifier.
- [var changeType: NSPersistentHistoryChangeType](nspersistenthistorychange/changetype.md)
  The type of change to the managed object in the persistent store.
- [var changedObjectID: NSManagedObjectID](nspersistenthistorychange/changedobjectid.md)
  The identifier of the managed object that changed. (swift) Declaration: @property(readonly, copy) NSManagedObjectID *changedObjectID; (objc) Availability: iOS: 11.0 — iPadOS: 11.0 — Mac Catalyst: 13.1 — macOS: 10.13 — tvOS: 11.0 — visionOS: 1.0 — watchOS: 4.0 (objc,swift) }
- [var tombstone: [AnyHashable : Any]?](nspersistenthistorychange/tombstone.md)
  A dictionary of attributes marked for preservation after deletion, and their values when deleted.
- [var transaction: NSPersistentHistoryTransaction?](nspersistenthistorychange/transaction.md)
  The persistent history transaction containing this change.
- [var updatedProperties: Set<NSPropertyDescription>?](nspersistenthistorychange/updatedproperties.md)
  The set of properties that were updated on the managed object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistenthistorychangetype)*