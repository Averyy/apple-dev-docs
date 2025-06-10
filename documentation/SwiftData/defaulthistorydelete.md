# DefaultHistoryDelete

**Framework**: SwiftData  
**Kind**: struct

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
struct DefaultHistoryDelete<Model> where Model : PersistentModel
```

## Topics

### Operators
- [static func == (DefaultHistoryDelete<Model>, DefaultHistoryDelete<Model>) -> Bool](defaulthistorydelete/==(_:_:).md)
### Instance Properties
- [let changeIdentifier: DefaultHistoryDelete<Model>.ChangeIdentifier](defaulthistorydelete/changeidentifier-swift.property.md)
- [let changedPersistentIdentifier: PersistentIdentifier](defaulthistorydelete/changedpersistentidentifier.md)
- [let tombstone: HistoryTombstone<Model>](defaulthistorydelete/tombstone.md)
- [let transactionIdentifier: DefaultHistoryDelete<Model>.TransactionIdentifier](defaulthistorydelete/transactionidentifier-swift.property.md)
### Instance Methods
- [func hash(into: inout Hasher)](defaulthistorydelete/hash(into:).md)
### Type Aliases
- [DefaultHistoryDelete.ChangeIdentifier](defaulthistorydelete/changeidentifier-swift.typealias.md)
- [DefaultHistoryDelete.TransactionIdentifier](defaulthistorydelete/transactionidentifier-swift.typealias.md)

## Relationships

### Conforms To
- [HistoryDelete](historydelete.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/defaulthistorydelete)*