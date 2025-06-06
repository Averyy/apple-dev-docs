# MaterialParameterTypes.BlendMode

**Framework**: RealityKit  
**Kind**: enum

Modes that describe how materials should be blended with content behind them.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
enum BlendMode
```

## Topics

### Operators
- [static func == (MaterialParameterTypes.BlendMode, MaterialParameterTypes.BlendMode) -> Bool](materialparametertypes/blendmode/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [MaterialParameterTypes.BlendMode.add](materialparametertypes/blendmode/add.md)
  Blend by adding the material’s color to the background color, ignoring alpha.
- [MaterialParameterTypes.BlendMode.alpha](materialparametertypes/blendmode/alpha.md)
  Blend by multiplying the material’s color value by its alpha value
### Instance Properties
- [var hashValue: Int](materialparametertypes/blendmode/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](materialparametertypes/blendmode/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](materialparametertypes/blendmode/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/materialparametertypes/blendmode)*