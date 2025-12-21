# Integrating virtual objects with your environment

**Framework**: RealityKit

Create an immersive game using native anchor support, environmental blending, model manipulation, and mesh instance duplication.

**Availability**:
- visionOS 26.0+
- Xcode 26.0+

#### Overview

> **Note**: This sample code project is associated with WWDC25 session 287: [`What’s new in RealityKit`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2025/287).

#### Configure the Sample Code Project

This sample won’t build and run in Simulator. Instead, you’ll need to build the sample and run it on Apple Vision Pro.

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
- [class LowLevelInstanceData](lowlevelinstancedata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/integrating-virtual-objects-with-your-environment)*