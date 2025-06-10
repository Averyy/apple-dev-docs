# Schema.Unique.CodingKeys

**Framework**: SwiftData  
**Kind**: enum

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+
- Swift 5.9+

## Declaration

```swift
enum CodingKeys
```

## Topics

### Operators
- [static func == (Schema.Unique<T>.CodingKeys, Schema.Unique<T>.CodingKeys) -> Bool](schema/unique/codingkeys/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [Schema.Unique.CodingKeys.constraints](schema/unique/codingkeys/constraints.md)
### Initializers
- [init?(intValue: Int)](schema/unique/codingkeys/init(intvalue:).md)
  Creates a new instance from the specified integer.
- [init?(stringValue: String)](schema/unique/codingkeys/init(stringvalue:).md)
  Creates a new instance from the given string.
### Instance Properties
- [var hashValue: Int](schema/unique/codingkeys/hashvalue.md)
  The hash value.
- [var intValue: Int?](schema/unique/codingkeys/intvalue.md)
  The value to use in an integer-indexed collection (e.g. an int-keyed dictionary).
- [var stringValue: String](schema/unique/codingkeys/stringvalue.md)
  The string to use in a named collection (e.g. a string-keyed dictionary).
### Instance Methods
- [func hash(into: inout Hasher)](schema/unique/codingkeys/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [CodingKey Implementations](schema/unique/codingkeys/codingkey-implementations.md)
- [Equatable Implementations](schema/unique/codingkeys/equatable-implementations.md)

## Relationships

### Conforms To
- [CodingKey](../Swift/CodingKey.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/unique/codingkeys)*