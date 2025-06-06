# changeID

**Framework**: Core Data  
**Kind**: property

The change’s numeric identifier.

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
var changeID: Int64 { get }
```

## See Also

- [var changeType: NSPersistentHistoryChangeType](nspersistenthistorychange/changetype.md)
  The type of change to the managed object in the persistent store.
- [enum NSPersistentHistoryChangeType](nspersistenthistorychangetype.md)
  The types of changes to managed objects reflected in persistent history.
- [var changedObjectID: NSManagedObjectID](nspersistenthistorychange/changedobjectid.md)
  The identifier of the managed object that changed. (swift) Declaration: @property(readonly, copy) NSManagedObjectID *changedObjectID; (objc) Availability: iOS: 11.0 — iPadOS: 11.0 — Mac Catalyst: 13.1 — macOS: 10.13 — tvOS: 11.0 — visionOS: 1.0 — watchOS: 4.0 (objc,swift) }
- [var tombstone: [AnyHashable : Any]?](nspersistenthistorychange/tombstone.md)
  A dictionary of attributes marked for preservation after deletion, and their values when deleted.
- [var transaction: NSPersistentHistoryTransaction?](nspersistenthistorychange/transaction.md)
  The persistent history transaction containing this change.
- [var updatedProperties: Set<NSPropertyDescription>?](nspersistenthistorychange/updatedproperties.md)
  The set of properties that were updated on the managed object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistenthistorychange/changeid)*