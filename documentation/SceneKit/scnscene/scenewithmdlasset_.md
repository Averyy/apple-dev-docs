# sceneWithMDLAsset:

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates a scene from the specified Model I/O asset.

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
+ (instancetype) sceneWithMDLAsset:(MDLAsset *) mdlAsset;
```

## Return Value

A new scene object.

## Discussion

The Model I/O framework provides universal support for import, export, description, and processing of several 3D asset file formats and related resources. (For details, see [Model I/O](../../ModelIO/ModelIO.md).) The [`MDLAsset`](../../ModelIO/mdlasset.md) class is a generic container for 3D objects. Importing a Model I/O asset creates a SceneKit scene containing nodes, geometries, materials, cameras, and lights corresponding to the objects stored in the asset.

## Parameters

- `mdlAsset`: A Model I/O asset object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/scenewithmdlasset:)*