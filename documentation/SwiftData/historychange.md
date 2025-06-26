# HistoryChange

**Framework**: SwiftData  
**Kind**: enum

Values that describe data history transactions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+
- Swift 5.9+

## Declaration

```swift
enum HistoryChange
```

## Topics

### Operations
- [case delete(any HistoryDelete)](historychange/delete(_:).md)
  A value that indicates a delete operation.
- [case insert(any HistoryInsert)](historychange/insert(_:).md)
  A value that indicates an insertion operation.
- [case update(any HistoryUpdate)](historychange/update(_:).md)
  A value that indicates an update operation.
### Getting information about a change
- [var changedPersistentIdentifier: PersistentIdentifier](historychange/changedpersistentidentifier.md)
  The persistent identifier of the change.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol HistoryDelete](historydelete.md)
  An interface that enables a custom data store to delete items from the history of changes to its persisted models.
- [protocol HistoryInsert](historyinsert.md)
- [protocol HistoryToken](historytoken.md)
- [protocol HistoryTransaction](historytransaction.md)
- [protocol HistoryUpdate](historyupdate.md)
- [struct HistoryTombstone](historytombstone.md)
- [struct DefaultHistoryInsert](defaulthistoryinsert.md)
- [struct DefaultHistoryUpdate](defaulthistoryupdate.md)
- [struct DefaultHistoryDelete](defaulthistorydelete.md)
- [struct DefaultHistoryToken](defaulthistorytoken.md)
- [struct DefaultHistoryTransaction](defaulthistorytransaction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historychange)*