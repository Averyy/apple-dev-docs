# Material.Color

**Framework**: RealityKit  
**Kind**: typealias  
**Role**: Type Alias

An alias for the color type that’s appropriate for the current platform.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
typealias Color = UIColor
```

*macOS*

```swift
typealias Color = NSColor
```

## See Also

### Material types
- [protocol Material](../material.md)
  A type that describes the material aspects of a mesh, like color and texture.
- [typealias Parameters](./parameters.md)
  The parameter type that custom materials uses for properties the framework passes to shader functions.
- [struct MaterialParameterTypes](../materialparametertypes.md)
  A set of types that material parameters can use.
- [struct MaterialParameters](../materialparameters.md)
- [enum MaterialColorParameter](../materialcolorparameter.md)
  The color parameter applied to a material.
- [enum MaterialScalarParameter](../materialscalarparameter.md)
  The scalar parameter applied to a material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/material/color)*