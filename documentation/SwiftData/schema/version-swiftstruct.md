# Schema.Version

**Framework**: SwiftData  
**Kind**: struct

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Swift 5.9+

## Declaration

```swift
struct Version
```

## Topics

### Operators
- [static func == (Schema.Version, Schema.Version) -> Bool](schema/version-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func < (Schema.Version, Schema.Version) -> Bool](schema/version-swift.struct/_(_:_:).md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
### Initializers
- [init(Int, Int, Int)](schema/version-swift.struct/init(_:_:_:).md)
  Initializes a version struct with the provided components of a semantic version.
- [init(from: any Decoder) throws](schema/version-swift.struct/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var description: String](schema/version-swift.struct/description.md)
  A textual description of the version object.
- [var hashValue: Int](schema/version-swift.struct/hashvalue.md)
  The hash value.
- [let major: Int](schema/version-swift.struct/major.md)
  The major version according to the semantic versioning standard.
- [let minor: Int](schema/version-swift.struct/minor.md)
  The minor version according to the semantic versioning standard.
- [let patch: Int](schema/version-swift.struct/patch.md)
  The patch version according to the semantic versioning standard.
### Instance Methods
- [func encode(to: any Encoder) throws](schema/version-swift.struct/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](schema/version-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Comparable Implementations](schema/version-swift.struct/comparable-implementations.md)
- [Equatable Implementations](schema/version-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/version-swift.struct)*