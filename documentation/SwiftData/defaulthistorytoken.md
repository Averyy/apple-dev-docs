# DefaultHistoryToken

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
struct DefaultHistoryToken
```

## Topics

### Operators
- [static func == (DefaultHistoryToken, DefaultHistoryToken) -> Bool](defaulthistorytoken/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func < (DefaultHistoryToken, DefaultHistoryToken) -> Bool](defaulthistorytoken/_(_:_:).md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
### Initializers
- [init(from: any Decoder) throws](defaulthistorytoken/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](defaulthistorytoken/hashvalue.md)
  The hash value.
- [var id: Int](defaulthistorytoken/id-swift.property.md)
  The stable identity of the entity associated with this instance.
- [var tokenValue: DefaultHistoryToken.TokenType?](defaulthistorytoken/tokenvalue.md)
### Instance Methods
- [func encode(to: any Encoder) throws](defaulthistorytoken/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](defaulthistorytoken/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [DefaultHistoryToken.ID](defaulthistorytoken/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
- [DefaultHistoryToken.TokenType](defaulthistorytoken/tokentype.md)
### Default Implementations
- [Comparable Implementations](defaulthistorytoken/comparable-implementations.md)
- [Equatable Implementations](defaulthistorytoken/equatable-implementations.md)

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [HistoryToken](historytoken.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/defaulthistorytoken)*