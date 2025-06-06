# faceCulling

**Framework**: RealityKit  
**Kind**: property

A process in which the system specifies polygons to remove before rendering a mesh using this material.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
var faceCulling: PhysicallyBasedMaterial.FaceCulling { get set }
```

#### Discussion

To improve performance, RealityKit culls polygons, or faces, that it determines won’t be visible. Discarding faces that aren’t part of the final render eliminates the need to do any calculations for those faces.

RealityKit recognizes when a face aims toward the camera (a front face) or away from the camera (a back face). This value controls the type of faces RealityKit culls.

This value defaults to [`MaterialParameterTypes.FaceCulling.back`](materialparametertypes/faceculling/back.md), which means RealityKit removes faces that point away from the camera. Most of the time, this is the correct behavior, because back faces are usually obscured by other front-facing polygons.

You can change the culling behavior to cull front faces instead or to turn off face culling altogether, but be aware that turning off face culling results in less efficient rendering and may negatively impact your app’s frame rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/faceculling-swift.property)*