# renderAsWireframe

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

Display only wireframe placeholders for geometries in the scene.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
static var renderAsWireframe: SCNDebugOptions { get }
```

```c
SCNDebugOptionRenderAsWireframe
```

#### Discussion

Unlike the [`showWireframe`](./showwireframe.md) option, this option disables normal surface rendering, displaying only the wireframe for each geometry.

## See Also

### Debugging Geometry and Animation
- [static var showBoundingBoxes: SCNDebugOptions](./showboundingboxes.md)
  Display the bounding boxes for any nodes with content.
- [static var showWireframe: SCNDebugOptions](./showwireframe.md)
  Display geometries in the scene with wireframe rendering.
- [static var showSkeletons: SCNDebugOptions](./showskeletons.md)
  Display visualizations of the skeletal animation parameters for relevant geometries.
- [static var showCreases: SCNDebugOptions](./showcreases.md)
  Display nonsmoothed crease regions for geometries affected by surface subdivision.
- [static var showConstraints: SCNDebugOptions](./showconstraints.md)
  Display visualizations of the constraint objects acting on nodes in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scndebugoptions/renderaswireframe)*