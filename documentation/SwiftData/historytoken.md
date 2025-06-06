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
### Conforming Types
- [DefaultHistoryToken](defaulthistorytoken.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historytoken)*