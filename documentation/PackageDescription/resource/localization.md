# Resource.Localization

**Framework**: PackageDescription  
**Kind**: enum  
**Role**: Enumeration

Defines the explicit type of localization for resources.

**Availability**:
- SwiftPM 5.3+

## Declaration

```swift
enum Localization
```

## Topics

### Enumeration Cases
- [Resource.Localization.base](./localization/base.md)
  A constant that represents base internationalization.
- [Resource.Localization.default](./localization/default.md)
  A constant that represents default localization.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Applying Rules
- [static func process(String, localization: Resource.Localization?) -> Resource](./process%28_,localization%29.md)
  Applies a platform-specific rules to the resource at the given path.
- [static func copy(String) -> Resource](./copy%28_%29.md)
  Applies the copy rule to a resource at the given path.
- [static func embedInCode(String) -> Resource](./embedincode%28_%29.md)
  Applies the embed rule to a resource at the given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/resource/localization)*