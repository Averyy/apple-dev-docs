# SCNHitTestResult

**Framework**: SceneKit  
**Kind**: class

Information about the result of a scene-space or view-space search for scene elements.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class SCNHitTestResult
```

#### Overview

Hit-testing is the process of finding elements of a scene located at a specified point, or along a specified line segment (or ). An [`SCNHitTestResult`](scnhittestresult.md) object provides details about one result from a hit-test search. There are three ways to perform a hit-test search. Use the [`hitTest(_:options:)`](scnscenerenderer/hittest(_:options:).md) method of an [`SCNView`](scnview.md) object (or other scene renderer), the [`hitTestWithSegment(from:to:options:)`](scnnode/hittestwithsegment(from:to:options:).md) method of a node, or the [`rayTestWithSegment(from:to:options:)`](scnphysicsworld/raytestwithsegment(from:to:options:).md) method of your scene’s physics world.

When you perform a hit-test search, SceneKit looks for [`SCNGeometry`](scngeometry.md) objects along the ray you specify. For each intersection between the ray and and a geometry, SceneKit creates a hit-test result to provide information about both the [`SCNNode`](scnnode.md) object containing the geometry and the location of the intersection on the geometry’s surface.

## Topics

### Retrieving Information About a Hit-Test Result
- [var node: SCNNode](scnhittestresult/node.md)
  The node whose geometry intersects the search ray.
- [var geometryIndex: Int](scnhittestresult/geometryindex.md)
  The index of the geometry element whose surface the search ray intersects.
- [var faceIndex: Int](scnhittestresult/faceindex.md)
  The index of the primitive in the geometry element intersected by the search ray.
- [var localCoordinates: SCNVector3](scnhittestresult/localcoordinates.md)
  The point of intersection between the geometry and the search ray, in the local coordinate system of the node containing the geometry.
- [var worldCoordinates: SCNVector3](scnhittestresult/worldcoordinates.md)
  The point of intersection between the geometry and the search ray, in the scene’s world coordinate system.
- [var localNormal: SCNVector3](scnhittestresult/localnormal.md)
  The surface normal vector at the point of intersection, in the local coordinate system of the node containing the geometry intersected by the search ray.
- [var worldNormal: SCNVector3](scnhittestresult/worldnormal.md)
  The surface normal vector at the point of intersection, in the scene’s world coordinate system.
- [var modelTransform: SCNMatrix4](scnhittestresult/modeltransform.md)
  The world transform matrix of the node containing the intersection.
- [func textureCoordinates(withMappingChannel: Int) -> CGPoint](scnhittestresult/texturecoordinates(withmappingchannel:).md)
  Returns the texture coordinates at the point of intersection for the specified texture mapping channel.
### Instance Properties
- [var boneNode: SCNNode?](scnhittestresult/bonenode.md)
- [var simdLocalCoordinates: simd_float3](scnhittestresult/simdlocalcoordinates.md)
- [var simdLocalNormal: simd_float3](scnhittestresult/simdlocalnormal.md)
- [var simdModelTransform: simd_float4x4](scnhittestresult/simdmodeltransform.md)
- [var simdWorldCoordinates: simd_float3](scnhittestresult/simdworldcoordinates.md)
- [var simdWorldNormal: simd_float3](scnhittestresult/simdworldnormal.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol SCNSceneRenderer](scnscenerenderer.md)
  Methods and properties common to the [`SCNView`](scnview.md), [`SCNLayer`](scnlayer.md), and [`SCNRenderer`](scnrenderer.md) classes.
- [protocol SCNSceneRendererDelegate](scnscenerendererdelegate.md)
  Methods your app can implement to participate in SceneKit’s animation loop or perform additional rendering.
- [class SCNLayer](scnlayer.md)
  A Core Animation layer that renders a SceneKit scene as its content.
- [class SCNRenderer](scnrenderer.md)
  A renderer for displaying a SceneKit scene in an existing Metal workflow or OpenGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnhittestresult)*