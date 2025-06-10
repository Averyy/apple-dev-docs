# MaterialColorParameter

**Framework**: RealityKit  
**Kind**: enum

The color parameter applied to a material.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
enum MaterialColorParameter
```

## Topics

### Selecting color parameters
- [MaterialColorParameter.color(_:)](materialcolorparameter/color(_:)-7gx04.md)
  A color value in macOS.
- [MaterialColorParameter.texture(_:)](materialcolorparameter/texture(_:).md)
  A texture resource.
### Comparing material color parameters
- [static func == (MaterialColorParameter, MaterialColorParameter) -> Bool](materialcolorparameter/==(_:_:).md)
  Indicates whether two color parameters are equal.
- [func hash(into: inout Hasher)](materialcolorparameter/hash(into:).md)
  Hashes the essential components of the color parameter by feeding them into the given hash function.
### Enumeration Cases
- [MaterialColorParameter.color(_:)](materialcolorparameter/color(_:)-49aw0.md)
  A color value in macOS.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [protocol Material](material.md)
  A type that describes the material aspects of a mesh, like color and texture.
- [typealias Color](material/color.md)
  An alias for the color type that’s appropriate for the current platform.
- [typealias Parameters](material/parameters.md)
  The parameter type that custom materials uses for properties the framework passes to shader functions.
- [struct MaterialParameterTypes](materialparametertypes.md)
  A set of types that material parameters can use.
- [struct MaterialParameters](materialparameters.md)
- [enum MaterialScalarParameter](materialscalarparameter.md)
  The scalar parameter applied to a material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/materialcolorparameter)*