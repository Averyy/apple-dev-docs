# MusicPropertySource

**Framework**: MusicKit  
**Kind**: enum

An enumeration that specifies which source to use when requesting properties and relationships.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum MusicPropertySource
```

## Topics

### Operators
- [static func == (MusicPropertySource, MusicPropertySource) -> Bool](musicpropertysource/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [MusicPropertySource.catalog](musicpropertysource/catalog.md)
  The source representing the Apple Music catalog.
- [MusicPropertySource.library](musicpropertysource/library.md)
  The source representing the user’s music library.
### Initializers
- [init(from: any Decoder) throws](musicpropertysource/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](musicpropertysource/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](musicpropertysource/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](musicpropertysource/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [MusicPropertySource.AllCases](musicpropertysource/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
### Type Properties
- [static var allCases: [MusicPropertySource]](musicpropertysource/allcases-swift.type.property.md)
  A collection of all values of this type.
### Default Implementations
- [Equatable Implementations](musicpropertysource/equatable-implementations.md)

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicpropertysource)*