# renderer(_:didAdd:for:)

**Framework**: ARKit  
**Kind**: method

Tells the delegate that a SceneKit node corresponding to a new AR anchor has been added to the scene.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func renderer(_ renderer: any SCNSceneRenderer, didAdd node: SCNNode, for anchor: ARAnchor)
```

#### Discussion

Depending on the session configuration, ARKit may automatically add anchors to a session. The view calls this method once for each new anchor. ARKit also calls this method to provide visual content for any [`ARAnchor`](aranchor.md) objects you manually add using the session’s [`add(anchor:)`](arsession/add(anchor:).md) method.

You can provide visual content for the anchor by attaching geometry (or other SceneKit features) to this node or by adding child nodes.

Alternatively, you can implement the [`renderer(_:nodeFor:)`](arscnviewdelegate/renderer(_:nodefor:).md) method to create your own node (or instance of an [`SCNNode`](https://developer.apple.com/documentation/SceneKit/SCNNode) subclass) for an anchor.

## Parameters

- `renderer`: The   object rendering the scene.
- `node`: The newly added SceneKit node.
- `anchor`: The AR anchor corresponding to the node.

## See Also

- [func renderer(any SCNSceneRenderer, nodeFor: ARAnchor) -> SCNNode?](arscnviewdelegate/renderer(_:nodefor:).md)
  Asks the delegate to provide a SceneKit node corresponding to a newly added anchor.
- [func renderer(any SCNSceneRenderer, willUpdate: SCNNode, for: ARAnchor)](arscnviewdelegate/renderer(_:willupdate:for:).md)
  Tells the delegate that a SceneKit node’s properties will be updated to match the current state of its corresponding anchor.
- [func renderer(any SCNSceneRenderer, didUpdate: SCNNode, for: ARAnchor)](arscnviewdelegate/renderer(_:didupdate:for:).md)
  Tells the delegate that a SceneKit node’s properties have been updated to match the current state of its corresponding anchor.
- [func renderer(any SCNSceneRenderer, didRemove: SCNNode, for: ARAnchor)](arscnviewdelegate/renderer(_:didremove:for:).md)
  Tells the delegate that the SceneKit node corresponding to a removed AR anchor has been removed from the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnviewdelegate/renderer(_:didadd:for:))*