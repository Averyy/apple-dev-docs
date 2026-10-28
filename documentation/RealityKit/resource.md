# Resource

**Framework**: RealityKit  
**Kind**: protocol  
**Role**: Protocol

A shared resource you use to configure a component, like a material, mesh, or texture.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@preconcurrency
protocol Resource : Sendable
```

## Overview

Resources can be costly to load or create. Share and reuse resources as much as possible.

## Relationships

### Inherits From
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Conforming Types
- [AnimationGraphResource](./animationgraphresource.md)
- [AnimationResource](./animationresource.md)
- [AudioBufferResource](./audiobufferresource.md)
- [AudioFileGroupResource](./audiofilegroupresource.md)
- [AudioFileResource](./audiofileresource.md)
- [AudioResource](./audioresource.md)
- [BehaviorTreeResource](./behaviortreeresource.md)
- [BlendShapeWeightsMapping](./blendshapeweightsmapping.md)
- [ClothMeshResource](./clothmeshresource.md)
- [ClothPoseResource](./clothposeresource.md)
- [DiffuseProbeResource](./diffuseproberesource.md)
- [EnvironmentResource](./environmentresource.md)
- [IKResource](./ikresource.md)
- [LightmapResource](./lightmapresource.md)
- [MeshResource](./meshresource.md)
- [NavigationMeshResource](./navigationmeshresource.md)
- [PhysicsMaterialResource](./physicsmaterialresource.md)
- [ReverbMeshResource](./reverbmeshresource.md)
- [ShapeResource](./shaperesource.md)
- [SkeletonResource](./skeletonresource.md)
- [TextureResource](./textureresource.md)

## See Also

### Loading an entity from a file
- [Generating procedural textures](../visionOS/generating-procedural-textures-in-visionos.md)
  Display a 3D model that generates procedural textures in a reality view.
- [Loading entities from a file](./loading-entities-from-a-file.md)
  Retrieve an entity from storage on disk using a synchronous or an asynchronous load operation.
- [Stored entities](./stored-entities.md)
  Manage entities that you store as assets on disk.
- [Creating USD files for Apple devices](../USD/creating-usd-files-for-apple-devices.md)
  Generate 3D assets that render as expected.
- [convenience init(contentsOf: URL, withName: String?) async throws](./entity/init%28contentsof,withname%29.md)
  Creates an entity by asynchronously loading it from a file URL.
- [convenience init(named: String, in: Bundle?) async throws](./entity/init%28named,in%29.md)
  Creates an entity by asynchronously loading it from a bundle.
- [struct ReferenceComponent](./referencecomponent.md)
  A component that can load another entity from a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/resource)*