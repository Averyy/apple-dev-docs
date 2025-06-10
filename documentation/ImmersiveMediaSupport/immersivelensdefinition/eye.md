# ImmersiveLensDefinition.Eye

**Framework**: Immersive Media Support  
**Kind**: enum

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum Eye
```

## Topics

### Enumeration Cases
- [ImmersiveLensDefinition.Eye.left](immersivelensdefinition/eye/left.md)
  Represents the left eye
- [ImmersiveLensDefinition.Eye.right](immersivelensdefinition/eye/right.md)
  Represents the right eye
### Initializers
- [init?(rawValue: Int)](immersivelensdefinition/eye/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: Int](immersivelensdefinition/eye/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [ImmersiveLensDefinition.Eye.RawValue](immersivelensdefinition/eye/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](immersivelensdefinition/eye/equatable-implementations.md)
- [RawRepresentable Implementations](immersivelensdefinition/eye/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [ImmersiveLensDefinition.STMapType](immersivelensdefinition/stmaptype.md)
  An enum listing the valid values for STMap generation output when using the [`generateSTMap(device:cameraEye:stmapType:into:)`](immersivelensdefinition/generatestmap(device:cameraeye:stmaptype:into:).md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivelensdefinition/eye)*