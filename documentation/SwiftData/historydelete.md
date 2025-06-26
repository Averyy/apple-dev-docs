# HistoryDelete

**Framework**: SwiftData  
**Kind**: protocol

An interface that enables a custom data store to delete items from the history of changes to its persisted models.

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
protocol HistoryDelete<Model> : Sendable
```

## Topics

### History deletion properites
- [var changeIdentifier: Self.ChangeIdentifier](historydelete/changeidentifier-swift.property.md)
  The change identifier of the delete operation.
- [var changedPersistentIdentifier: PersistentIdentifier](historydelete/changedpersistentidentifier.md)
  The changed persistent identifier of the delete operation.
- [var tombstone: HistoryTombstone<Self.Model>](historydelete/tombstone.md)
  The value the framework uses to represent information about data the Swift Data previously deleted from a model.
- [var transactionIdentifier: Self.TransactionIdentifier](historydelete/transactionidentifier-swift.property.md)
  The delete operation’s transaction identifier.
### Associated types
- [associatedtype ChangeIdentifier : Comparable, Hashable, Sendable](historydelete/changeidentifier-swift.associatedtype.md)
  The type associated with the change identifier.
- [associatedtype Model : PersistentModel](historydelete/model.md)
  The type associated with the persistent model.
- [associatedtype TransactionIdentifier : Comparable, Hashable, Sendable](historydelete/transactionidentifier-swift.associatedtype.md)
  The type associated with the transaction identifier.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [DefaultHistoryDelete](defaulthistorydelete.md)

## See Also

- [enum HistoryChange](historychange.md)
  Values that describe data history transactions.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historydelete)*