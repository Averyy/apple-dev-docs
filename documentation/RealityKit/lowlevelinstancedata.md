# LowLevelInstanceData

**Framework**: RealityKit  
**Kind**: class

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final class LowLevelInstanceData
```

## Topics

### Initializers
- [convenience init(instanceCount: Int) throws](lowlevelinstancedata/init(instancecount:).md)
- [init(instanceCount: Int, instanceCapacity: Int) throws](lowlevelinstancedata/init(instancecount:instancecapacity:).md)
### Instance Properties
- [var instanceCapacity: Int](lowlevelinstancedata/instancecapacity.md)
  The current number of instances this LowLevelInstanceData will draw, when set on a MeshInstancesComponent.
- [var instanceCount: Int](lowlevelinstancedata/instancecount.md)
### Instance Methods
- [func read(using: any MTLCommandBuffer) -> any MTLBuffer](lowlevelinstancedata/read(using:).md)
  Retrieve the current per instance transform data, for GPU reading.
- [func replace(using: any MTLCommandBuffer) -> any MTLBuffer](lowlevelinstancedata/replace(using:).md)
  Retrieve an MTLBuffer that can be used to replace the per instance transform data on GPU using Metal.
- [func replaceMutableTransforms((UnsafeMutableBufferPointer<float4x4>) -> Void)](lowlevelinstancedata/replacemutabletransforms(_:).md)
  Replace the per instance transform data synchronously on the CPU.
- [func withMutableTransforms((UnsafeMutableBufferPointer<float4x4>) -> Void)](lowlevelinstancedata/withmutabletransforms(_:).md)
  Update the per instance transform data synchronously on the CPU. The transform buffer provided is only valid for the lifetime of the callback.
- [func withTransforms((UnsafeBufferPointer<float4x4>) -> Void)](lowlevelinstancedata/withtransforms(_:).md)
  Read the per instance transform data synchronously on the CPU. The transform buffer provided is only valid for the lifetime of the callback.

## See Also

- [Creating a spatial drawing app with RealityKit](creating-a-spatial-drawing-app-with-realitykit.md)
  Use low-level mesh and texture APIs to achieve fast updates to a person’s brush strokes by integrating RealityKit with ARKit and SwiftUI.
- [Creating a plane with low-level mesh](creating-a-plane-with-low-level-mesh.md)
  Create a low-level mesh and set its vertex positions and normals to form a plane.
- [class LowLevelMesh](lowlevelmesh.md)
  A container for vertex data that you can use to create and update meshes using your own format.
- [LowLevelMesh.Descriptor](lowlevelmesh/descriptor-swift.struct.md)
  An object that describes the data format and layout of the buffers in a low-level mesh.
- [LowLevelMesh.Part](lowlevelmesh/part.md)
  An object that describes a range of primitives to display, and their material index.
- [LowLevelMesh.Layout](lowlevelmesh/layout.md)
  An object that describes a set of attributes that share a buffer index, offset, and stride.
- [LowLevelMesh.Attribute](lowlevelmesh/attribute.md)
  An object that determines how to store vertex attribute data in memory and map it to RealityKit shader attributes.
- [LowLevelMesh.VertexSemantic](lowlevelmesh/vertexsemantic.md)
  Designates the intended usage of a vertex attribute.
- [LowLevelMesh.PartsCollection](lowlevelmesh/partscollection.md)
  An object that holds a mutable collection low-level mesh parts.
- [class LowLevelBuffer](lowlevelbuffer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelinstancedata)*