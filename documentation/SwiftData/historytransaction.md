# HistoryTransaction

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
protocol HistoryTransaction : Hashable, Identifiable, Sendable
```

## Topics

### Associated Types
- [associatedtype TokenType : Comparable, Hashable, Identifiable, Sendable](historytransaction/tokentype.md)
- [associatedtype TransactionIdentifier : Comparable, Hashable, Sendable](historytransaction/transactionidentifier-swift.associatedtype.md)
### Instance Properties
- [var author: String?](historytransaction/author.md)
- [var changes: [HistoryChange]](historytransaction/changes.md)
- [var storeIdentifier: String](historytransaction/storeidentifier.md)
- [var timestamp: Date](historytransaction/timestamp.md)
- [var token: Self.TokenType](historytransaction/token.md)
- [var transactionIdentifier: Self.TransactionIdentifier](historytransaction/transactionidentifier-swift.property.md)

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
### Conforming Types
- [DefaultHistoryTransaction](defaulthistorytransaction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historytransaction)*