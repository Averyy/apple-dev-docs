# renderAsWireframe

**Framework**: SceneKit  
**Kind**: property

Display only wireframe placeholders for geometries in the scene.

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
static var renderAsWireframe: SCNDebugOptions { get }
```

#### Discussion

Unlike the [`showWireframe`](scndebugoptions/showwireframe.md) option, this option disables normal surface rendering, displaying only the wireframe for each geometry.

## See Also

- [static var showBoundingBoxes: SCNDebugOptions](scndebugoptions/showboundingboxes.md)
  Display the bounding boxes for any nodes with content.
- [static var showWireframe: SCNDebugOptions](scndebugoptions/showwireframe.md)
  Display geometries in the scene with wireframe rendering.
- [static var showSkeletons: SCNDebugOptions](scndebugoptions/showskeletons.md)
  Display visualizations of the skeletal animation parameters for relevant geometries.
- [static var showCreases: SCNDebugOptions](scndebugoptions/showcreases.md)
  Display nonsmoothed crease regions for geometries affected by surface subdivision.
- [static var showConstraints: SCNDebugOptions](scndebugoptions/showconstraints.md)
  Display visualizations of the constraint objects acting on nodes in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scndebugoptions/renderaswireframe)*