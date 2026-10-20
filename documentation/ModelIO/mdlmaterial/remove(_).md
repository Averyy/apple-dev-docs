# remove(_:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method

Removes the specified material property from the material.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func remove(_ property: MDLMaterialProperty)
```

```objc
- (void) removeProperty:(MDLMaterialProperty *) property;
```

#### Discussion

This method has no effect if the specified material property is not contained in the material.

## Parameters

- `property`: The material property object to remove.

## See Also

### Working with individual material properties
- [func propertyNamed(String) -> MDLMaterialProperty?](./propertynamed%28_%29.md)
  Returns the material property with the specified name.
- [func property(with: MDLMaterialSemantic) -> MDLMaterialProperty?](./property%28with%29.md)
  Returns the material property for the specified material semantic.
- [func properties(with: MDLMaterialSemantic) -> [MDLMaterialProperty]](./properties%28with%29.md)
  Returns the complete list of material properties that match the specified material semantic.
- [func setProperty(MDLMaterialProperty)](./setproperty%28_%29.md)
  Adds a new material property to or replaces an existing material property in the material.
- [func removeAllProperties()](./removeallproperties%28%29.md)
  Removes all material properties from the material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterial/remove(_:))*