# ImmersiveCameraLensDefinition.STMapType

**Framework**: Immersive Media Support  
**Kind**: enum

A value representing a camera lens projection type.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum STMapType
```

#### Overview

This value can be used for STMap generation output when using the `ImmersiveLensDefinition/generateSTMap(device:cameraEye:stmapType:into:)` function.

## Topics

### Operators
- [static func == (ImmersiveCameraLensDefinition.STMapType, ImmersiveCameraLensDefinition.STMapType) -> Bool](immersivecameralensdefinition/stmaptype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [ImmersiveCameraLensDefinition.STMapType.equidistant](immersivecameralensdefinition/stmaptype/equidistant.md)
  A value indicating an equidistant lens projection type.
- [ImmersiveCameraLensDefinition.STMapType.equirectangular](immersivecameralensdefinition/stmaptype/equirectangular.md)
  A value indicating an equirectangular lens projection type.
### Instance Properties
- [var hashValue: Int](immersivecameralensdefinition/stmaptype/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](immersivecameralensdefinition/stmaptype/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](immersivecameralensdefinition/stmaptype/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecameralensdefinition/stmaptype)*