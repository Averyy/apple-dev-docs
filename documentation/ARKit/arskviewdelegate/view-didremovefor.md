# view(_:didRemove:for:)

**Framework**: ARKit  
**Kind**: method

Tells the delegate that the SpriteKit node corresponding to an AR anchor has been removed from the scene.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func view(_ view: ARSKView, didRemove node: SKNode, for anchor: ARAnchor)
```

#### Discussion

Depending on the session configuration, ARKit may automatically remove anchors from a session. The view calls this method once for each removed anchor.

## Parameters

- `view`: The   object rendering the scene.
- `node`: The removed SpriteKit node.
- `anchor`: The AR anchor corresponding to the node.

## See Also

- [func view(ARSKView, nodeFor: ARAnchor) -> SKNode?](arskviewdelegate/view(_:nodefor:).md)
  Asks the delegate to provide a SpriteKit node corresponding to a newly added anchor.
- [func view(ARSKView, didAdd: SKNode, for: ARAnchor)](arskviewdelegate/view(_:didadd:for:).md)
  Tells the delegate that a SpriteKit node corresponding to a new AR anchor has been added to the scene.
- [func view(ARSKView, willUpdate: SKNode, for: ARAnchor)](arskviewdelegate/view(_:willupdate:for:).md)
  Tells the delegate that a SpriteKit node’s properties will be updated to match the current state of its corresponding anchor.
- [func view(ARSKView, didUpdate: SKNode, for: ARAnchor)](arskviewdelegate/view(_:didupdate:for:).md)
  Tells the delegate that a SpriteKit node’s properties have been updated to match the current state of its corresponding anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskviewdelegate/view(_:didremove:for:))*