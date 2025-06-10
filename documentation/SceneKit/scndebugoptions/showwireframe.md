# showWireframe

**Framework**: SceneKit  
**Kind**: property

Display geometries in the scene with wireframe rendering.

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
static var showWireframe: SCNDebugOptions { get }
```

#### Discussion

When this option is enabled, SceneKit still renders scene geometry with all associated materials, then overlays a wireframe rendering of the same geometry. You can use this option, for example, to debug material rendering issues.

## See Also

- [static var showBoundingBoxes: SCNDebugOptions](scndebugoptions/showboundingboxes.md)
  Display the bounding boxes for any nodes with content.
- [static var renderAsWireframe: SCNDebugOptions](scndebugoptions/renderaswireframe.md)
  Display only wireframe placeholders for geometries in the scene.
- [static var showSkeletons: SCNDebugOptions](scndebugoptions/showskeletons.md)
  Display visualizations of the skeletal animation parameters for relevant geometries.
- [static var showCreases: SCNDebugOptions](scndebugoptions/showcreases.md)
  Display nonsmoothed crease regions for geometries affected by surface subdivision.
- [static var showConstraints: SCNDebugOptions](scndebugoptions/showconstraints.md)
  Display visualizations of the constraint objects acting on nodes in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scndebugoptions/showwireframe)*