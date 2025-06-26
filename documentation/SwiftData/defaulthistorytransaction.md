# DefaultHistoryTransaction

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
struct DefaultHistoryTransaction
```

## Topics

### Operators
- [static func == (DefaultHistoryTransaction, DefaultHistoryTransaction) -> Bool](defaulthistorytransaction/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [let author: String?](defaulthistorytransaction/author.md)
- [let bundleIdentifier: String](defaulthistorytransaction/bundleidentifier.md)
- [let changes: [HistoryChange]](defaulthistorytransaction/changes.md)
- [var hashValue: Int](defaulthistorytransaction/hashvalue.md)
  The hash value.
- [var id: Int64](defaulthistorytransaction/id-swift.property.md)
  The stable identity of the entity associated with this instance.
- [let processIdentifier: String](defaulthistorytransaction/processidentifier.md)
- [let storeIdentifier: String](defaulthistorytransaction/storeidentifier.md)
- [let timestamp: Date](defaulthistorytransaction/timestamp.md)
- [let token: DefaultHistoryTransaction.TokenType](defaulthistorytransaction/token.md)
- [let transactionIdentifier: DefaultHistoryTransaction.TransactionIdentifier](defaulthistorytransaction/transactionidentifier-swift.property.md)
### Instance Methods
- [func hash(into: inout Hasher)](defaulthistorytransaction/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [DefaultHistoryTransaction.ID](defaulthistorytransaction/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
- [DefaultHistoryTransaction.TokenType](defaulthistorytransaction/tokentype.md)
- [DefaultHistoryTransaction.TransactionIdentifier](defaulthistorytransaction/transactionidentifier-swift.typealias.md)
### Default Implementations
- [Equatable Implementations](defaulthistorytransaction/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [HistoryTransaction](historytransaction.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum HistoryChange](historychange.md)
  Values that describe data history transactions.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/defaulthistorytransaction)*