# view(_:nodeFor:)

**Framework**: ARKit  
**Kind**: method

Asks the delegate to provide a SpriteKit node corresponding to a newly added anchor.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func view(_ view: ARSKView, nodeFor anchor: ARAnchor) -> SKNode?
```

## Mentions

- [Providing 2D Virtual Content with SpriteKit](providing-2d-virtual-content-with-spritekit.md)

#### Return Value

A new SpriteKit node, which ARKit will add to the scene and update to follow its corresponding AR anchor.

#### Discussion

Depending on the session configuration, ARKit may automatically add anchors to a session, such as the origin of the world coordinate system and detected planes. ARKit also calls this method to provide visual content for any [`ARAnchor`](aranchor.md) objects you manually add using the session’s [`add(anchor:)`](arsession/add(anchor:).md) method.

You can implement this method to provide a new [`SKNode`](https://developer.apple.com/documentation/SpriteKit/SKNode) object (or instance of any system or custom [`SKNode`](https://developer.apple.com/documentation/SpriteKit/SKNode) subclass) you plan to use as a visual representation of the anchor.

Note that ARKit controls the node’s position, rotation, and scale to simulate a billboarded 3D effect even for 2D sprites. If you provide a `SKTransformLayer` node, ARKit applies a 3D transformation.

Alternatively, if you do not implement this method, ARKit creates an empty node, and you can implement the [`view(_:didAdd:for:)`](arskviewdelegate/view(_:didadd:for:).md) method instead to provide visual content by adding children to that node.

## Parameters

- `view`: The   object rendering the scene.
- `anchor`: The anchor for which a node is requested.

## See Also

- [func view(ARSKView, didAdd: SKNode, for: ARAnchor)](arskviewdelegate/view(_:didadd:for:).md)
  Tells the delegate that a SpriteKit node corresponding to a new AR anchor has been added to the scene.
- [func view(ARSKView, willUpdate: SKNode, for: ARAnchor)](arskviewdelegate/view(_:willupdate:for:).md)
  Tells the delegate that a SpriteKit node’s properties will be updated to match the current state of its corresponding anchor.
- [func view(ARSKView, didUpdate: SKNode, for: ARAnchor)](arskviewdelegate/view(_:didupdate:for:).md)
  Tells the delegate that a SpriteKit node’s properties have been updated to match the current state of its corresponding anchor.
- [func view(ARSKView, didRemove: SKNode, for: ARAnchor)](arskviewdelegate/view(_:didremove:for:).md)
  Tells the delegate that the SpriteKit node corresponding to an AR anchor has been removed from the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskviewdelegate/view(_:nodefor:))*