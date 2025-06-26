# HistoryToken

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
protocol HistoryToken : Comparable, Decodable, Encodable, Hashable, Identifiable, Sendable
```

## Topics

### Associated Types
- [associatedtype TokenType : Decodable, Encodable, Hashable, Sendable](historytoken/tokentype.md)
### Instance Properties
- [var tokenValue: Self.TokenType?](historytoken/tokenvalue.md)

## Relationships

### Inherits From
- [Comparable](../Swift/Comparable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [DefaultHistoryToken](defaulthistorytoken.md)

## See Also

- [enum HistoryChange](historychange.md)
  Values that describe data history transactions.
- [protocol HistoryDelete](historydelete.md)
  An interface that enables a custom data store to delete items from the history of changes to its persisted models.
- [protocol HistoryInsert](historyinsert.md)
- [protocol HistoryTransaction](historytransaction.md)
- [protocol HistoryUpdate](historyupdate.md)
- [struct HistoryTombstone](historytombstone.md)
- [struct DefaultHistoryInsert](defaulthistoryinsert.md)
- [struct DefaultHistoryUpdate](defaulthistoryupdate.md)
- [struct DefaultHistoryDelete](defaulthistorydelete.md)
- [struct DefaultHistoryToken](defaulthistorytoken.md)
- [struct DefaultHistoryTransaction](defaulthistorytransaction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historytoken)*