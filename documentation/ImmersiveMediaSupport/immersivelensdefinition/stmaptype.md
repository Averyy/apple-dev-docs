# ImmersiveLensDefinition.STMapType

**Framework**: Immersive Media Support  
**Kind**: enum

An enum listing the valid values for STMap generation output when using the [`generateSTMap(device:cameraEye:stmapType:into:)`](immersivelensdefinition/generatestmap(device:cameraeye:stmaptype:into:).md) function.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum STMapType
```

## Topics

### Enumeration Cases
- [ImmersiveLensDefinition.STMapType.equidistant](immersivelensdefinition/stmaptype/equidistant.md)
  Equidistant lens projection type
- [ImmersiveLensDefinition.STMapType.equirectangular](immersivelensdefinition/stmaptype/equirectangular.md)
  Equirectangular lens projection type
### Initializers
- [init?(rawValue: Int)](immersivelensdefinition/stmaptype/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: Int](immersivelensdefinition/stmaptype/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [ImmersiveLensDefinition.STMapType.RawValue](immersivelensdefinition/stmaptype/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](immersivelensdefinition/stmaptype/equatable-implementations.md)
- [RawRepresentable Implementations](immersivelensdefinition/stmaptype/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [ImmersiveLensDefinition.Eye](immersivelensdefinition/eye.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivelensdefinition/stmaptype)*