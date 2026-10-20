# propertyNamed(_:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (MDLMaterialProperty *) propertyNamed:(NSString *) name;
```

#### Return Value

The material property with the specified name, or `nil` if the material does not contain a material property with that name.

#### Discussion

Material property names are not related to their use in rendering. Instead, you can assign descriptive names to material properties and use this method to keep track of them.

## Parameters

- `name`: The [`name`](../mdlmaterialproperty/name.md) value of a material property in the material.

## See Also

### Working with individual material properties
- [func property(with: MDLMaterialSemantic) -> MDLMaterialProperty?](./property%28with%29.md)
  Returns the material property for the specified material semantic.
- [func properties(with: MDLMaterialSemantic) -> [MDLMaterialProperty]](./properties%28with%29.md)
  Returns the complete list of material properties that match the specified material semantic.
- [func setProperty(MDLMaterialProperty)](./setproperty%28_%29.md)
  Adds a new material property to or replaces an existing material property in the material.
- [func remove(MDLMaterialProperty)](./remove%28_%29.md)
  Removes the specified material property from the material.
- [func removeAllProperties()](./removeallproperties%28%29.md)
  Removes all material properties from the material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterial/propertynamed(_:))*