# type

**Framework**: Model I/O  
**Kind**: property

The data type stored in the material property’s value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var type: MDLMaterialPropertyType { get set }
```

#### Discussion

Each [`semantic`](mdlmaterialproperty/semantic.md) value has one or more data types that are appropriate for its value. For example, the [`MDLMaterialSemantic.baseColor`](mdlmaterialsemantic/basecolor.md) semantic provides per-pixel colors for a rendered surface, so appropriate values for that semantic include scalars (interpreted as a grayscale color), colors, texture images, or URLs that refer to texture images. The [`MDLMaterialSemantic.ambientOcclusionScale`](mdlmaterialsemantic/ambientocclusionscale.md) semantic provides a scale factor for the effect of ambient occlusion shading, so an appropriate value is a scalar or a grayscale image that varies that scalar value across the surface of the material.

## See Also

- [var name: String](mdlmaterialproperty/name.md)
  A descriptive name for the material property.
- [var semantic: MDLMaterialSemantic](mdlmaterialproperty/semantic.md)
  The semantic meaning for the material property’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterialproperty/type)*