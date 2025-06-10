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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historyinsert)*