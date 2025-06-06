# Resource.Localization

**Framework**: PackageDescription  
**Kind**: enum

Defines the explicit type of localization for resources.

**Availability**:
- SwiftPM 5.3+

## Declaration

```swift
enum Localization
```

## Topics

### Enumeration Cases
- [Resource.Localization.base](resource/localization/base.md)
  A constant that represents base internationalization.
- [Resource.Localization.default](resource/localization/default.md)
  A constant that represents default localization.
### Hashing
- [func hash(into: inout Hasher)](resource/localization/hash(into:).md)
  Hashes the localization by feeding the item into the given hasher.
- [var hashValue: Int](resource/localization/hashvalue.md)
  The localization’s hash value.
### Operator Functions
- [static func != (Self, Self) -> Bool](resource/localization/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Creating a Value
- [init?(rawValue: String)](resource/localization/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Accessing the Raw Value
- [var rawValue: String](resource/localization/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [Resource.Localization.RawValue](resource/localization/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](resource/localization/equatable-implementations.md)
- [RawRepresentable Implementations](resource/localization/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [static func process(String, localization: Resource.Localization?) -> Resource](resource/process(_:localization:).md)
  Applies a platform-specific rules to the resource at the given path.
- [static func copy(String) -> Resource](resource/copy(_:).md)
  Applies the copy rule to a resource at the given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/resource/localization)*