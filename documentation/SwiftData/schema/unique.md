# Schema.Unique

**Framework**: SwiftData  
**Kind**: class

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
final class Unique<T> where T : PersistentModel
```

## Topics

### Operators
- [static func == (Schema.Unique<T>, Schema.Unique<T>) -> Bool](schema/unique/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init([PartialKeyPath<T>]...)](schema/unique/init(_:).md)
- [init(from: any Decoder) throws](schema/unique/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [let constraints: [[PartialKeyPath<T>]]](schema/unique/constraints.md)
- [var debugDescription: String](schema/unique/debugdescription.md)
  A textual representation of this instance, suitable for debugging.
- [var hashValue: Int](schema/unique/hashvalue.md)
  The hash value.
- [var isUnique: Bool](schema/unique/isunique.md)
- [var name: String](schema/unique/name.md)
- [var originalName: String](schema/unique/originalname.md)
- [var valueType: any Any.Type](schema/unique/valuetype.md)
### Instance Methods
- [func encode(to: any Encoder) throws](schema/unique/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](schema/unique/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Enumerations
- [Schema.Unique.CodingKeys](schema/unique/codingkeys.md)
### Default Implementations
- [Equatable Implementations](schema/unique/equatable-implementations.md)
- [SchemaProperty Implementations](schema/unique/schemaproperty-implementations.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [SchemaProperty](schemaproperty.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/unique)*