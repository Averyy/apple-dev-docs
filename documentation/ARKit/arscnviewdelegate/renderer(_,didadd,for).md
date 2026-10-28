# renderer(_:didAdd:for:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a SceneKit node corresponding to a new AR anchor has been added to the scene.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
optional func renderer(_ renderer: any SCNSceneRenderer, didAdd node: SCNNode, for anchor: ARAnchor)
```

```objc
- (void) renderer:(id<SCNSceneRenderer>) renderer didAddNode:(SCNNode *) node forAnchor:(ARAnchor *) anchor;
```

## Discussion

Depending on the session configuration, ARKit may automatically add anchors to a session. The view calls this method once for each new anchor. ARKit also calls this method to provide visual content for any [`ARAnchor`](../aranchor.md) objects you manually add using the session’s [`add(anchor:)`](../arsession/add%28anchor%29.md) method.

You can provide visual content for the anchor by attaching geometry (or other SceneKit features) to this node or by adding child nodes.

Alternatively, you can implement the [`renderer(_:nodeFor:)`](./renderer%28_,nodefor%29.md) method to create your own node (or instance of an [`SCNNode`](../../SceneKit/scnnode.md) subclass) for an anchor.

## Parameters

- `renderer`: The [`ARSCNView`](../arscnview.md) object rendering the scene.
- `node`: The newly added SceneKit node.
- `anchor`: The AR anchor corresponding to the node.

## See Also

### Handling Content Updates
- [func renderer(any SCNSceneRenderer, nodeFor: ARAnchor) -> SCNNode?](./renderer%28_,nodefor%29.md)
  Asks the delegate to provide a SceneKit node corresponding to a newly added anchor.
- [func renderer(any SCNSceneRenderer, willUpdate: SCNNode, for: ARAnchor)](./renderer%28_,willupdate,for%29.md)
  Tells the delegate that a SceneKit node’s properties will be updated to match the current state of its corresponding anchor.
- [func renderer(any SCNSceneRenderer, didUpdate: SCNNode, for: ARAnchor)](./renderer%28_,didupdate,for%29.md)
  Tells the delegate that a SceneKit node’s properties have been updated to match the current state of its corresponding anchor.
- [func renderer(any SCNSceneRenderer, didRemove: SCNNode, for: ARAnchor)](./renderer%28_,didremove,for%29.md)
  Tells the delegate that the SceneKit node corresponding to a removed AR anchor has been removed from the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnviewdelegate/renderer(_:didadd:for:))*