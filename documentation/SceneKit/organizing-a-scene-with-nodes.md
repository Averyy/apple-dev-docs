# Organizing a Scene with Nodes

**Framework**: SceneKit

Use nodes to define the structure of a scene.

#### Overview

SceneKit implements content as a hierarchical tree structure of nodes, also known as a . A scene consists of a root node, which defines a coordinate space for the world of the scene, and other nodes that populate the world with visible content. SceneKit displays scenes in a view, processing the scene graph and performing animations before efficiently rendering each frame on the GPU.

Before working with SceneKit, you should be familiar with basic graphics concepts such as coordinate systems and the mathematics of three-dimensional geometry. SceneKit uses a right-handed coordinate system where (by default) the direction of view is along the negative z-axis, as illustrated below.

![Diagram of the SceneKit coordinate system: the positive x-axis points to the camera’s right, the positive y-axis points up, and the positive z-axis points toward and behind the camera.](https://docs-assets.developer.apple.com/published/987639a03a6a623b029b41f757b15aca/media-2929768%402x.png)

## See Also

- [class SCNNode](scnnode.md)
  A structural element of a scene graph, representing a position and transform in a 3D coordinate space, to which you can attach geometry, lights, cameras, or other displayable content.
- [class SCNReferenceNode](scnreferencenode.md)
  A scene graph node that serves as a placeholder for content to be loaded from a separate scene file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/organizing-a-scene-with-nodes)*