# showStatistics

**Framework**: RealityKit  
**Kind**: property

Collect performance statistics and display them in the view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)

## Declaration

```swift
static let showStatistics: ARView.DebugOptions
```

#### Discussion

Add this debug option to a view’s [`debugOptions`](arview/debugoptions-swift.property.md) option set to display a variety of resource utilization metrics, overlaid on the view. The statistics update in real time so you can examine how your app performs and what resources it consumes under different usage conditions.

![A screenshot of a RealityKit app running on an iPad, showing statistics in](https://docs-assets.developer.apple.com/published/4ae6ce5c8e636852322064a0932f33d4/ARView-DebugOptions-swift-struct-showStatistics-1%402x.png)

For more information about how to use the data shown above and described below, see [`Improving the Performance of a RealityKit App`](improving-the-performance-of-a-realitykit-app.md).

##### Measure Time

Items listed under the Frame CPU Time heading show how your app makes use of CPU time. The first item indicates frame rate, which directly impacts the quality of the user’s experience. The remaining items indicate average time in milliseconds per frame that the CPU spends performing certain tasks, as described below.

##### Measure Geometry

Items under the Scene Mesh Stats heading help you optimize your content. These statistics help you to estimate the complexity of your scene.

##### Measure Memory

The items under the App Memory Usage heading help you understand how much memory your app uses.

## See Also

- [static let none: ARView.DebugOptions](arview/debugoptions-swift.struct/none.md)
  Disable all debugging overlays.
- [static let showPhysics: ARView.DebugOptions](arview/debugoptions-swift.struct/showphysics.md)
  Draw visualizations for collision objects and rigid bodies.
- [static let showAnchorOrigins: ARView.DebugOptions](arview/debugoptions-swift.struct/showanchororigins.md)
  Display anchor origins.
- [static let showAnchorGeometry: ARView.DebugOptions](arview/debugoptions-swift.struct/showanchorgeometry.md)
  Display anchor geometry.
- [static let showWorldOrigin: ARView.DebugOptions](arview/debugoptions-swift.struct/showworldorigin.md)
  Display a coordinate axis indicating the position and orientation of the AR world coordinate system.
- [static let showFeaturePoints: ARView.DebugOptions](arview/debugoptions-swift.struct/showfeaturepoints.md)
  Display a point cloud showing intermediate results of the scene analysis used to track device position.
- [static let showSceneUnderstanding: ARView.DebugOptions](arview/debugoptions-swift.struct/showsceneunderstanding.md)
  Display the depth-colored wireframe for scene-understanding meshes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/debugoptions-swift.struct/showstatistics)*