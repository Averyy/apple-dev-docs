# view(_:didUpdate:for:)

**Framework**: ARKit  
**Kind**: method

Tells the delegate that a SpriteKit node’s properties have been updated to match the current state of its corresponding anchor.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func view(_ view: ARSKView, didUpdate node: SKNode, for anchor: ARAnchor)
```

#### Discussion

Depending on the session configuration, ARKit may automatically update anchors in a session. The view calls this method once for each updated anchor.

## Parameters

- `view`: The   object rendering the scene.
- `node`: The updated SpriteKit node.
- `anchor`: The AR anchor corresponding to the node.

## See Also

- [func view(ARSKView, nodeFor: ARAnchor) -> SKNode?](arskviewdelegate/view(_:nodefor:).md)
  Asks the delegate to provide a SpriteKit node corresponding to a newly added anchor.
- [func view(ARSKView, didAdd: SKNode, for: ARAnchor)](arskviewdelegate/view(_:didadd:for:).md)
  Tells the delegate that a SpriteKit node corresponding to a new AR anchor has been added to the scene.
- [func view(ARSKView, willUpdate: SKNode, for: ARAnchor)](arskviewdelegate/view(_:willupdate:for:).md)
  Tells the delegate that a SpriteKit node’s properties will be updated to match the current state of its corresponding anchor.
- [func view(ARSKView, didRemove: SKNode, for: ARAnchor)](arskviewdelegate/view(_:didremove:for:).md)
  Tells the delegate that the SpriteKit node corresponding to an AR anchor has been removed from the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskviewdelegate/view(_:didupdate:for:))*