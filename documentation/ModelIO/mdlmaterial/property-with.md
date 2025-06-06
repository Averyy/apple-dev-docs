# property(with:)

**Framework**: Model I/O  
**Kind**: method

Returns the material property for the specified material semantic.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func property(with semantic: MDLMaterialSemantic) -> MDLMaterialProperty?
```

#### Return Value

The material property for the specified semantic, or `nil` if the material does not contain a material property for that semantic.

#### Discussion

Material semantics identify the intended use of a material property in shading. Some semantic values, such as [`MDLMaterialSemantic.specular`](mdlmaterialsemantic/specular.md), are part of the material’s [`scatteringFunction`](mdlmaterial/scatteringfunction.md) property that determines its response to lighting; others, such as [`MDLMaterialSemantic.opacity`](mdlmaterialsemantic/opacity.md), determine other aspects of material rendering.

## Parameters

- `semantic`: The semantic value of a material property in the material.

## See Also

- [func propertyNamed(String) -> MDLMaterialProperty?](mdlmaterial/propertynamed(_:).md)
  Returns the material property with the specified name.
- [func properties(with: MDLMaterialSemantic) -> [MDLMaterialProperty]](mdlmaterial/properties(with:).md)
  Returns the complete list of material properties that match the specified material semantic.
- [func setProperty(MDLMaterialProperty)](mdlmaterial/setproperty(_:).md)
  Adds a new material property to or replaces an existing material property in the material.
- [func remove(MDLMaterialProperty)](mdlmaterial/remove(_:).md)
  Removes the specified material property from the material.
- [func removeAllProperties()](mdlmaterial/removeallproperties.md)
  Removes all material properties from the material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterial/property(with:))*