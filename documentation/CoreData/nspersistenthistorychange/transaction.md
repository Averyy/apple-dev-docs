# transaction

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The persistent history transaction containing this change.

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
var transaction: NSPersistentHistoryTransaction? { get }
```

```objc
@property (strong, readonly, nullable) NSPersistentHistoryTransaction * transaction;
```

## See Also

### Inspecting Change Details
- [var changeID: Int64](./changeid.md)
  The change’s numeric identifier.
- [var changeType: NSPersistentHistoryChangeType](./changetype.md)
  The type of change to the managed object in the persistent store.
- [enum NSPersistentHistoryChangeType](../nspersistenthistorychangetype.md)
  The types of changes to managed objects reflected in persistent history.
- [var changedObjectID: NSManagedObjectID](./changedobjectid.md)
  The identifier of the managed object that changed. (swift) Declaration: @property(readonly, copy) NSManagedObjectID *changedObjectID; (objc) Availability: iOS: 11.0 — iPadOS: 11.0 — Mac Catalyst: 13.1 — macOS: 10.13 — tvOS: 11.0 — visionOS: 1.0 — watchOS: 4.0 (objc,swift) }
- [var tombstone: [AnyHashable : Any]?](./tombstone.md)
  A dictionary of attributes marked for preservation after deletion, and their values when deleted.
- [var updatedProperties: Set<NSPropertyDescription>?](./updatedproperties.md)
  The set of properties that were updated on the managed object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistenthistorychange/transaction)*