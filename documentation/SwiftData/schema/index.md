# Schema.Index

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
final class Index<T> where T : PersistentModel
```

## Topics

### Operators
- [static func == (Schema.Index<T>, Schema.Index<T>) -> Bool](schema/index/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(Schema.Index<T>.Types<T>...)](schema/index/init(_:)-4i37e.md)
- [init([PartialKeyPath<T>]...)](schema/index/init(_:)-527in.md)
- [init(from: any Decoder) throws](schema/index/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var debugDescription: String](schema/index/debugdescription.md)
  A textual representation of this instance, suitable for debugging.
- [var hashValue: Int](schema/index/hashvalue.md)
  The hash value.
- [let indices: [Schema.Index<T>.Types<T>]](schema/index/indices.md)
- [var isUnique: Bool](schema/index/isunique.md)
- [var name: String](schema/index/name.md)
- [var originalName: String](schema/index/originalname.md)
- [var valueType: any Any.Type](schema/index/valuetype.md)
### Instance Methods
- [func encode(to: any Encoder) throws](schema/index/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](schema/index/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Enumerations
- [Schema.Index.CodingKeys](schema/index/codingkeys.md)
- [Schema.Index.Types](schema/index/types.md)
### Default Implementations
- [Equatable Implementations](schema/index/equatable-implementations.md)
- [SchemaProperty Implementations](schema/index/schemaproperty-implementations.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [SchemaProperty](schemaproperty.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/index)*