# lightWithMDLLight:

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates a light from the specified Model I/O light object.

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
+ (instancetype) lightWithMDLLight:(MDLLight *) mdlLight;
```

#### Return Value

A new light object.

#### Discussion

The Model I/O framework provides universal support for import, export, description, and processing of several 3D asset file formats and related resources. (For details, see [Model I/O](../../ModelIO/ModelIO.md).) The [`MDLLight`](../../ModelIO/mdllight.md) class is a generic description of a light source in a scene, supporting a superset of the attributes described by the [`SCNLight`](../scnlight.md) class.

## Parameters

- `mdlLight`: A Model I/O light object.

## See Also

### Creating a Light
- [+ light](./light.md)
  Creates a new light object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/lightwithmdllight:)*