# propertyNamed(_:)

**Framework**: Model I/O  
**Kind**: method

Returns the material property with the specified name.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func propertyNamed(_ name: String) -> MDLMaterialProperty?
```

#### Return Value

The material property with the specified name, or `nil` if the material does not contain a material property with that name.

#### Discussion

Material property names are not related to their use in rendering. Instead, you can assign descriptive names to material properties and use this method to keep track of them.

## Parameters

- `name`: The   value of a material property in the material.

## See Also

- [func property(with: MDLMaterialSemantic) -> MDLMaterialProperty?](mdlmaterial/property(with:).md)
  Returns the material property for the specified material semantic.
- [func properties(with: MDLMaterialSemantic) -> [MDLMaterialProperty]](mdlmaterial/properties(with:).md)
  Returns the complete list of material properties that match the specified material semantic.
- [func setProperty(MDLMaterialProperty)](mdlmaterial/setproperty(_:).md)
  Adds a new material property to or replaces an existing material property in the material.
- [func remove(MDLMaterialProperty)](mdlmaterial/remove(_:).md)
  Removes the specified material property from the material.
- [func removeAllProperties()](mdlmaterial/removeallproperties.md)
  Removes all material properties from the material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterial/propertynamed(_:))*