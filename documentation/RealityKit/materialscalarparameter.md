# MaterialScalarParameter

**Framework**: RealityKit  
**Kind**: enum

The scalar parameter applied to a material.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
enum MaterialScalarParameter
```

## Topics

### Getting scalar parameters
- [MaterialScalarParameter.float(_:)](materialscalarparameter/float(_:).md)
  A scalar, single-precision value.
- [MaterialScalarParameter.texture(_:)](materialscalarparameter/texture(_:).md)
  A one-channel texture.
### Creating a scalar parameter
- [init(floatLiteral: Float)](materialscalarparameter/init(floatliteral:).md)
  Creates a scalar parameter from a floating-point literal.
- [init(integerLiteral: Int)](materialscalarparameter/init(integerliteral:).md)
  Creates a scalar parameter from an integer literal.
- [MaterialScalarParameter.FloatLiteralType](materialscalarparameter/floatliteraltype.md)
  A type that represents a floating-point literal.
- [MaterialScalarParameter.IntegerLiteralType](materialscalarparameter/integerliteraltype.md)
  A type that represents an integer literal.
### Comparing material scalar parameters
- [static func == (MaterialScalarParameter, MaterialScalarParameter) -> Bool](materialscalarparameter/==(_:_:).md)
  Indicates whether two scalar parameters are equal.
- [static func != (Self, Self) -> Bool](materialscalarparameter/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func hash(into: inout Hasher)](materialscalarparameter/hash(into:).md)
  Hashes the essential components of the scalar parameter by feeding them into the given hash function.
- [var hashValue: Int](materialscalarparameter/hashvalue.md)
  The hash value.
### Default Implementations
- [Equatable Implementations](materialscalarparameter/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByFloatLiteral](../Swift/ExpressibleByFloatLiteral.md)
- [ExpressibleByIntegerLiteral](../Swift/ExpressibleByIntegerLiteral.md)
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
- [enum MaterialColorParameter](materialcolorparameter.md)
  The color parameter applied to a material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/materialscalarparameter)*