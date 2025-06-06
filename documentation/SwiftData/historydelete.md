# HistoryDelete

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
protocol HistoryDelete<Model> : Sendable
```

## Topics

### Associated Types
- [associatedtype ChangeIdentifier : Comparable, Hashable, Sendable](historydelete/changeidentifier-swift.associatedtype.md)
- [associatedtype Model : PersistentModel](historydelete/model.md)
- [associatedtype TransactionIdentifier : Comparable, Hashable, Sendable](historydelete/transactionidentifier-swift.associatedtype.md)
### Instance Properties
- [var changeIdentifier: Self.ChangeIdentifier](historydelete/changeidentifier-swift.property.md)
- [var changedPersistentIdentifier: PersistentIdentifier](historydelete/changedpersistentidentifier.md)
- [var tombstone: HistoryTombstone<Self.Model>](historydelete/tombstone.md)
- [var transactionIdentifier: Self.TransactionIdentifier](historydelete/transactionidentifier-swift.property.md)

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
### Conforming Types
- [DefaultHistoryDelete](defaulthistorydelete.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historydelete)*