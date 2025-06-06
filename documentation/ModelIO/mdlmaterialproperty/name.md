# name

**Framework**: Model I/O  
**Kind**: property

A descriptive name for the material property.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var name: String { get set }
```

#### Discussion

A material property’s name is not used for rendering, but it can be useful in debugging. Model Model I/O  may set a material property’s name to a format-specific value when loading materials from an [`MDLAsset`](mdlasset.md) object.

## See Also

- [var semantic: MDLMaterialSemantic](mdlmaterialproperty/semantic.md)
  The semantic meaning for the material property’s value.
- [var type: MDLMaterialPropertyType](mdlmaterialproperty/type.md)
  The data type stored in the material property’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterialproperty/name)*