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

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [static func process(String, localization: Resource.Localization?) -> Resource](resource/process(_:localization:).md)
  Applies a platform-specific rules to the resource at the given path.
- [static func copy(String) -> Resource](resource/copy(_:).md)
  Applies the copy rule to a resource at the given path.
- [static func embedInCode(String) -> Resource](resource/embedincode(_:).md)
  Applies the embed rule to a resource at the given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/resource/localization)*