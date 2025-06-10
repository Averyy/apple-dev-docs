# ARView.DebugOptions

**Framework**: RealityKit  
**Kind**: struct

Options for drawing overlay content in a scene that can aid in debugging.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)

## Declaration

```swift
struct DebugOptions
```

## Topics

### Configuring debug options
- [static let none: ARView.DebugOptions](arview/debugoptions-swift.struct/none.md)
  Disable all debugging overlays.
- [static let showPhysics: ARView.DebugOptions](arview/debugoptions-swift.struct/showphysics.md)
  Draw visualizations for collision objects and rigid bodies.
- [static let showStatistics: ARView.DebugOptions](arview/debugoptions-swift.struct/showstatistics.md)
  Collect performance statistics and display them in the view.
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
### Creating a debug option set
- [init(rawValue: Int)](arview/debugoptions-swift.struct/init(rawvalue:).md)
  Create a debug options enumeration from a raw value.
- [let rawValue: Int](arview/debugoptions-swift.struct/rawvalue.md)
  Options for drawing overlay content in a scene that aids in debugging the scene.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class ARView](arview.md)
  A view that enables you to display an AR experience with RealityKit.
- [typealias ARViewBase](arviewbase.md)
  The platform-specific base class for the view into which RealityKit renders content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/debugoptions-swift.struct)*