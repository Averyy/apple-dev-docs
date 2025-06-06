# DefaultHistoryInsert

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
struct DefaultHistoryInsert<Model> where Model : PersistentModel
```

## Topics

### Operators
- [static func == (DefaultHistoryInsert<Model>, DefaultHistoryInsert<Model>) -> Bool](defaulthistoryinsert/==(_:_:).md)
### Instance Properties
- [let changeIdentifier: DefaultHistoryInsert<Model>.ChangeIdentifier](defaulthistoryinsert/changeidentifier-swift.property.md)
- [let changedPersistentIdentifier: PersistentIdentifier](defaulthistoryinsert/changedpersistentidentifier.md)
- [let transactionIdentifier: DefaultHistoryInsert<Model>.TransactionIdentifier](defaulthistoryinsert/transactionidentifier-swift.property.md)
### Instance Methods
- [func hash(into: inout Hasher)](defaulthistoryinsert/hash(into:).md)
### Type Aliases
- [DefaultHistoryInsert.ChangeIdentifier](defaulthistoryinsert/changeidentifier-swift.typealias.md)
- [DefaultHistoryInsert.TransactionIdentifier](defaulthistoryinsert/transactionidentifier-swift.typealias.md)

## Relationships

### Conforms To
- [HistoryInsert](historyinsert.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/defaulthistoryinsert)*