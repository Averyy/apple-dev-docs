# materialWithMDLMaterial:

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates a material from the specified Model I/O material object.

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
+ (instancetype) materialWithMDLMaterial:(MDLMaterial *) mdlMaterial;
```

## Return Value

A new material.

## Discussion

The Model I/O framework provides universal support for import, export, description, and processing of several 3D asset file formats and related resources. (For details, see [Model I/O](../../ModelIO/ModelIO.md).) The [`MDLMaterial`](../../ModelIO/mdlmaterial.md) class is a generic description of surface rendering to be used in rendering 3D object, supporting a superset of the attributes described by the [`SCNMaterial`](../scnmaterial.md) class.

## Parameters

- `mdlMaterial`: A Model I/O material object.

## See Also

### Creating a Material
- [+ material](./material.md)
  Creates a new material object.
- [var name: String?](./name.md)
  A name associated with the material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/materialwithmdlmaterial:)*