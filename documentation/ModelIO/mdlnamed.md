# MDLNamed

**Framework**: Model I/O  
**Kind**: protocol

The common interface for Model I/O objects that expose a human-readable name.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol MDLNamed
```

#### Overview

The [`name`](mdlnamed/name.md) property defined by this protocol is adopted by many classes in Model I/O. You can use this property to assign descriptive names to objects such as meshes, materials, cameras, and scattering functions to better keep track of the objects in your app. When you load objects from or export objects to a file using the [`MDLAsset`](mdlasset.md) class, this property corresponds to the names and labels for objects that appear in popular 3D authoring tools.

## Topics

### Naming an Object
- [var name: String](mdlnamed/name.md)
  A descriptive name for the object.

## Relationships

### Conforming Types
- [MDLAreaLight](mdlarealight.md)
- [MDLCamera](mdlcamera.md)
- [MDLCheckerboardTexture](mdlcheckerboardtexture.md)
- [MDLColorSwatchTexture](mdlcolorswatchtexture.md)
- [MDLLight](mdllight.md)
- [MDLLightProbe](mdllightprobe.md)
- [MDLMaterial](mdlmaterial.md)
- [MDLMaterialProperty](mdlmaterialproperty.md)
- [MDLMaterialPropertyConnection](mdlmaterialpropertyconnection.md)
- [MDLMaterialPropertyGraph](mdlmaterialpropertygraph.md)
- [MDLMaterialPropertyNode](mdlmaterialpropertynode.md)
- [MDLMesh](mdlmesh.md)
- [MDLNoiseTexture](mdlnoisetexture.md)
- [MDLNormalMapTexture](mdlnormalmaptexture.md)
- [MDLObject](mdlobject.md)
- [MDLPackedJointAnimation](mdlpackedjointanimation.md)
- [MDLPhotometricLight](mdlphotometriclight.md)
- [MDLPhysicallyPlausibleLight](mdlphysicallyplausiblelight.md)
- [MDLPhysicallyPlausibleScatteringFunction](mdlphysicallyplausiblescatteringfunction.md)
- [MDLScatteringFunction](mdlscatteringfunction.md)
- [MDLSkeleton](mdlskeleton.md)
- [MDLSkyCubeTexture](mdlskycubetexture.md)
- [MDLStereoscopicCamera](mdlstereoscopiccamera.md)
- [MDLSubmesh](mdlsubmesh.md)
- [MDLTexture](mdltexture.md)
- [MDLURLTexture](mdlurltexture.md)
- [MDLVoxelArray](mdlvoxelarray.md)

## See Also

- [class MDLAsset](mdlasset.md)
  An indexed container for 3D objects and associated information, such as transform hierarchies, meshes, cameras, and lights.
- [class MDLObject](mdlobject.md)
  The base class for objects that are part of a 3D asset, including meshes, cameras, and lights.
- [class MDLTransform](mdltransform.md)
  A description of the local coordinate space transformations for a 3D object.
- [class MDLMesh](mdlmesh.md)
  A container for vertex buffer data to be used in rendering a 3D object.
- [class MDLSubmesh](mdlsubmesh.md)
  A container for index buffer data and material information to be used in rendering all or part of a 3D object.
- [class MDLSubmeshTopology](mdlsubmeshtopology.md)
  A description of how a submesh’s index buffer data is arranged and how that arrangement should be used to produce the submesh’s intended 3D shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlnamed)*