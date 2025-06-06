# semantic

**Framework**: Model I/O  
**Kind**: property

The semantic meaning for the material property’s value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var semantic: MDLMaterialSemantic { get set }
```

#### Discussion

A material semantic determines how the material property’s value should be interpreted to produce a specific surface appearance in rendering. For example, the [`MDLMaterialSemantic.baseColor`](mdlmaterialsemantic/basecolor.md) semantic defines the default color of each pixel on a rendered surface before shading effects are applied.

When Model I/O  loads materials from an [`MDLAsset`](mdlasset.md) object, it automatically selects the appropriate standard semantics for the surface rendering descriptions in the asset file.

## See Also

- [var name: String](mdlmaterialproperty/name.md)
  A descriptive name for the material property.
- [var type: MDLMaterialPropertyType](mdlmaterialproperty/type.md)
  The data type stored in the material property’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterialproperty/semantic)*