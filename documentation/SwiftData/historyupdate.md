# HistoryUpdate

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
protocol HistoryUpdate<Model> : Sendable
```

## Topics

### Associated Types
- [associatedtype ChangeIdentifier : Comparable, Hashable, Sendable](historyupdate/changeidentifier-swift.associatedtype.md)
- [associatedtype Model : PersistentModel](historyupdate/model.md)
- [associatedtype TransactionIdentifier : Comparable, Hashable, Sendable](historyupdate/transactionidentifier-swift.associatedtype.md)
### Instance Properties
- [var changeIdentifier: Self.ChangeIdentifier](historyupdate/changeidentifier-swift.property.md)
- [var changedPersistentIdentifier: PersistentIdentifier](historyupdate/changedpersistentidentifier.md)
- [var transactionIdentifier: Self.TransactionIdentifier](historyupdate/transactionidentifier-swift.property.md)
- [var updatedAttributes: [any PartialKeyPath<Self.Model> & Sendable]](historyupdate/updatedattributes.md)
### Type Aliases
- [HistoryUpdate.PropertyUpdate](historyupdate/propertyupdate.md)

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [DefaultHistoryUpdate](defaulthistoryupdate.md)

## See Also

- [enum HistoryChange](historychange.md)
  Values that describe data history transactions.
- [protocol HistoryDelete](historydelete.md)
  An interface that enables a custom data store to delete items from the history of changes to its persisted models.
- [protocol HistoryInsert](historyinsert.md)
- [protocol HistoryToken](historytoken.md)
- [protocol HistoryTransaction](historytransaction.md)
- [struct HistoryTombstone](historytombstone.md)
- [struct DefaultHistoryInsert](defaulthistoryinsert.md)
- [struct DefaultHistoryUpdate](defaulthistoryupdate.md)
- [struct DefaultHistoryDelete](defaulthistorydelete.md)
- [struct DefaultHistoryToken](defaulthistorytoken.md)
- [struct DefaultHistoryTransaction](defaulthistorytransaction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historyupdate)*