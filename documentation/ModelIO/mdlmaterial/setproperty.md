# setProperty(_:)

**Framework**: Model I/O  
**Kind**: method

Adds a new material property to or replaces an existing material property in the material.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setProperty(_ property: MDLMaterialProperty)
```

#### Discussion

If the material already contains a material property with the same name or semantic, this method replaces that material property. Otherwise, this method adds the specified material property to the material.

## Parameters

- `property`: The material property object to add to the material.

## See Also

- [func propertyNamed(String) -> MDLMaterialProperty?](mdlmaterial/propertynamed(_:).md)
  Returns the material property with the specified name.
- [func property(with: MDLMaterialSemantic) -> MDLMaterialProperty?](mdlmaterial/property(with:).md)
  Returns the material property for the specified material semantic.
- [func properties(with: MDLMaterialSemantic) -> [MDLMaterialProperty]](mdlmaterial/properties(with:).md)
  Returns the complete list of material properties that match the specified material semantic.
- [func remove(MDLMaterialProperty)](mdlmaterial/remove(_:).md)
  Removes the specified material property from the material.
- [func removeAllProperties()](mdlmaterial/removeallproperties.md)
  Removes all material properties from the material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterial/setproperty(_:))*