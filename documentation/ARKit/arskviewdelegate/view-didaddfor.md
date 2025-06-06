# view(_:didAdd:for:)

**Framework**: ARKit  
**Kind**: method

Tells the delegate that a SpriteKit node corresponding to a new AR anchor has been added to the scene.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func view(_ view: ARSKView, didAdd node: SKNode, for anchor: ARAnchor)
```

#### Discussion

Depending on the session configuration, ARKit may automatically add anchors to a session. The view calls this method once for each new anchor. ARKit also calls this method to provide visual content for any [`ARAnchor`](aranchor.md) objects you manually add using the session’s [`add(anchor:)`](arsession/add(anchor:).md) method.

You can provide visual content for the anchor by adding child nodes.

Alternatively, you can implement the [`view(_:nodeFor:)`](arskviewdelegate/view(_:nodefor:).md) method to create your own node (or instance of an [`SKNode`](https://developer.apple.com/documentation/SpriteKit/SKNode) subclass) for an anchor.

## Parameters

- `view`: The   object rendering the scene.
- `node`: The newly added SpriteKit node.
- `anchor`: The AR anchor corresponding to the node.

## See Also

- [func view(ARSKView, nodeFor: ARAnchor) -> SKNode?](arskviewdelegate/view(_:nodefor:).md)
  Asks the delegate to provide a SpriteKit node corresponding to a newly added anchor.
- [func view(ARSKView, willUpdate: SKNode, for: ARAnchor)](arskviewdelegate/view(_:willupdate:for:).md)
  Tells the delegate that a SpriteKit node’s properties will be updated to match the current state of its corresponding anchor.
- [func view(ARSKView, didUpdate: SKNode, for: ARAnchor)](arskviewdelegate/view(_:didupdate:for:).md)
  Tells the delegate that a SpriteKit node’s properties have been updated to match the current state of its corresponding anchor.
- [func view(ARSKView, didRemove: SKNode, for: ARAnchor)](arskviewdelegate/view(_:didremove:for:).md)
  Tells the delegate that the SpriteKit node corresponding to an AR anchor has been removed from the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskviewdelegate/view(_:didadd:for:))*