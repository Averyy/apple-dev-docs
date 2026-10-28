# material

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates a new material object.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```objc
+ (instancetype) material;
```

## Return Value

A new material object.

## Discussion

A newly created material contains an [`SCNMaterialProperty`](../scnmaterialproperty.md) object for each of its eight visual properties. You change a material’s appearance by setting the [`contents`](../scnmaterialproperty/contents.md) of each visual property. For information on each visual property’s default contents and how it affects a material’s appearance, see Visual Properties for Special Effects.

## See Also

### Creating a Material
- [+ materialWithMDLMaterial:](./materialwithmdlmaterial_.md)
  Creates a material from the specified Model I/O material object.
- [var name: String?](./name.md)
  A name associated with the material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/material)*