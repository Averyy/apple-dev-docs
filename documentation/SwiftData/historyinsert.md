# HistoryInsert

**Framework**: SwiftData  
**Kind**: protocol

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
protocol HistoryInsert<Model> : Sendable
```

## Topics

### Associated Types
- [associatedtype ChangeIdentifier : Comparable, Hashable, Sendable](historyinsert/changeidentifier-swift.associatedtype.md)
- [associatedtype Model : PersistentModel](historyinsert/model.md)
- [associatedtype TransactionIdentifier : Comparable, Hashable, Sendable](historyinsert/transactionidentifier-swift.associatedtype.md)
### Instance Properties
- [var changeIdentifier: Self.ChangeIdentifier](historyinsert/changeidentifier-swift.property.md)
- [var changedPersistentIdentifier: PersistentIdentifier](historyinsert/changedpersistentidentifier.md)
- [var transactionIdentifier: Self.TransactionIdentifier](historyinsert/transactionidentifier-swift.property.md)

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [DefaultHistoryInsert](defaulthistoryinsert.md)

## See Also

- [enum HistoryChange](historychange.md)
  Values that describe data history transactions.
- [protocol HistoryDelete](historydelete.md)
  An interface that enables a custom data store to delete items from the history of changes to its persisted models.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historyinsert)*