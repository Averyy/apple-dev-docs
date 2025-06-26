# DataStoreSnapshotCodingKey

**Framework**: SwiftData  
**Kind**: enum

The key space to use when implementing custom coders and decoders for data store snapshots,

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
enum DataStoreSnapshotCodingKey
```

## Topics

### Creating a coding key
- [init?(stringValue: String)](datastoresnapshotcodingkey/init(stringvalue:).md)
  Creates a new instance from the given string.
### Values that describe coding keys
- [DataStoreSnapshotCodingKey.persistentIdentifier](datastoresnapshotcodingkey/persistentidentifier.md)
  A value that represents a persistent identifier.
### Instance Properties
- [var intValue: Int?](datastoresnapshotcodingkey/intvalue.md)
  The value to use in an integer-indexed collection, such as an integer-keyed dictionary.
- [var stringValue: String](datastoresnapshotcodingkey/stringvalue.md)
  The string to use in a named collection (e.g. a string-keyed dictionary).
### Enumeration Cases
- [DataStoreSnapshotCodingKey.modeledProperty(_:)](datastoresnapshotcodingkey/modeledproperty(_:).md)
  A value that represents the name of the modeled property.
### Initializers
- [init?(intValue: Int)](datastoresnapshotcodingkey/init(intvalue:).md)
  Creates a new instance from the specified integer.
### Default Implementations
- [CodingKey Implementations](datastoresnapshotcodingkey/codingkey-implementations.md)

## Relationships

### Conforms To
- [CodingKey](../Swift/CodingKey.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/datastoresnapshotcodingkey)*