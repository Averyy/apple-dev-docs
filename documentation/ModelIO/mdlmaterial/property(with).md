# property(with:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (MDLMaterialProperty *) propertyWithSemantic:(MDLMaterialSemantic) semantic;
```

#### Return Value

The material property for the specified semantic, or `nil` if the material does not contain a material property for that semantic.

#### Discussion

Material semantics identify the intended use of a material property in shading. Some semantic values, such as [`MDLMaterialSemantic.specular`](../mdlmaterialsemantic/specular.md), are part of the material’s [`scatteringFunction`](./scatteringfunction.md) property that determines its response to lighting; others, such as [`MDLMaterialSemantic.opacity`](../mdlmaterialsemantic/opacity.md), determine other aspects of material rendering.

## Parameters

- `semantic`: The semantic value of a material property in the material.

## See Also

### Working with individual material properties
- [func propertyNamed(String) -> MDLMaterialProperty?](./propertynamed%28_%29.md)
  Returns the material property with the specified name.
- [func properties(with: MDLMaterialSemantic) -> [MDLMaterialProperty]](./properties%28with%29.md)
  Returns the complete list of material properties that match the specified material semantic.
- [func setProperty(MDLMaterialProperty)](./setproperty%28_%29.md)
  Adds a new material property to or replaces an existing material property in the material.
- [func remove(MDLMaterialProperty)](./remove%28_%29.md)
  Removes the specified material property from the material.
- [func removeAllProperties()](./removeallproperties%28%29.md)
  Removes all material properties from the material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterial/property(with:))*