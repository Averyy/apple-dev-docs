# Schema.Version

**Framework**: SwiftData  
**Kind**: struct  
**Role**: Structure

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
- [static func == (Schema.Version, Schema.Version) -> Bool](./version-swift.struct/eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are equal.
- [static func < (Schema.Version, Schema.Version) -> Bool](./version-swift.struct/op%28_,_%29.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
### Initializers
- [init(Int, Int, Int)](./version-swift.struct/init%28_,_,_%29.md)
  Initializes a version struct with the provided components of a semantic version.
### Instance Properties
- [var description: String](./version-swift.struct/description.md)
  A textual description of the version object.
- [let major: Int](./version-swift.struct/major.md)
  The major version according to the semantic versioning standard.
- [let minor: Int](./version-swift.struct/minor.md)
  The minor version according to the semantic versioning standard.
- [let patch: Int](./version-swift.struct/patch.md)
  The patch version according to the semantic versioning standard.

## Relationships

### Conforms To
- [Comparable](../../Swift/comparable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/version-swift.struct)*