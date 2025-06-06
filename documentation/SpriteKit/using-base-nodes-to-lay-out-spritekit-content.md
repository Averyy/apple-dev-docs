# Using Base Nodes to Lay Out SpriteKit Content

**Framework**: SpriteKit

Use nonvisual nodes to define the layout of a scene.

#### Overview

Each onscreen element in SpriteKit is referred to as a . Nodes are either visual elements or containers of other nodes. You set up the appearance of a SpriteKit scene by adding nodes alongside and on top of each other in a hierarchical form. Collectively, this structure is referred to as the  or the .

These are the basic nonvisual nodes in SpriteKit:

- [`SKNode`](sknode.md) is a container node. It doesn’t render any content of its own, but works as a layout tool for its child nodes.
- [`SKReferenceNode`](skreferencenode.md) doesn’t define content of its own, but refers to another node or archived file that does.
- [`SKCameraNode`](skcameranode.md) defines point of view within a scene. Its inverse scale is applied to all nodes in the hierarchy except for its children. Use the children of `SKCameraNode` for UI elements that should be unaffected by zoom level.

For a list of visual elements, see Nodes that Draw in [`Nodes for Scene Building`](nodes-for-scene-building.md), which also includes some examples of using visual nodes.

## See Also

- [class SKNode](sknode.md)
  The base class of all SpriteKit nodes.
- [class SKCameraNode](skcameranode.md)
  A node that determines which parts of the scene are visible within a view.
- [class SKReferenceNode](skreferencenode.md)
  A node that’s defined in an archived `.sks` file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/using-base-nodes-to-lay-out-spritekit-content)*