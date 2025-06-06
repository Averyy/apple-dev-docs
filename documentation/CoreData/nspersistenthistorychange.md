# NSPersistentHistoryChange

**Framework**: Core Data  
**Kind**: class

A change representing the insertion, update, or deletion of a managed object in the persistent store.

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
class NSPersistentHistoryChange
```

## Mentions

- [Consuming relevant store changes](consuming-relevant-store-changes.md)

## Topics

### Inspecting Change Metadata
- [class var fetchRequest: NSFetchRequest<any NSFetchRequestResult>?](nspersistenthistorychange/fetchrequest.md)
  A fetch request that has the persistent history change as the entity.
- [class var entityDescription: NSEntityDescription?](nspersistenthistorychange/entitydescription.md)
  The entity description of the persistent history change entity.
- [class func entityDescription(with: NSManagedObjectContext) -> NSEntityDescription?](nspersistenthistorychange/entitydescription(with:).md)
  Requests an entity description for the managed object type affected by the change using the provided context.
### Inspecting Change Details
- [var changeID: Int64](nspersistenthistorychange/changeid.md)
  The change’s numeric identifier.
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

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSPersistentHistoryTransaction](nspersistenthistorytransaction.md)
  A set of changes in the persistent history based on a context save or batch operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistenthistorychange)*