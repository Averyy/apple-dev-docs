# Curator.Kind

**Framework**: MusicKit  
**Kind**: enum

The available kinds of curators.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum Kind
```

## Topics

### Operators
- [static func == (Curator.Kind, Curator.Kind) -> Bool](curator/kind-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [Curator.Kind.editorial](curator/kind-swift.enum/editorial.md)
  Indicates that the curator is an Apple Music curator.
- [Curator.Kind.external](curator/kind-swift.enum/external.md)
  Indicates that the curator is an external, third-party curator.
### Initializers
- [init(from: any Decoder) throws](curator/kind-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](curator/kind-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](curator/kind-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](curator/kind-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](curator/kind-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/curator/kind-swift.enum)*