# renderer(_:nodeFor:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate to provide a SceneKit node corresponding to a newly added anchor.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
optional func renderer(_ renderer: any SCNSceneRenderer, nodeFor anchor: ARAnchor) -> SCNNode?
```

```objc
- (SCNNode *) renderer:(id<SCNSceneRenderer>) renderer nodeForAnchor:(ARAnchor *) anchor;
```

## Return Value

A new SceneKit node, which ARKit will add to the scene and update to follow its corresponding AR anchor.

## Discussion

Depending on the session configuration, ARKit may automatically add anchors to a session. ARKit also calls this method to provide visual content for any [`ARAnchor`](../aranchor.md) objects you manually add using the session’s [`add(anchor:)`](../arsession/add%28anchor%29.md) method.

You can implement this method to provide a new [`SCNNode`](../../SceneKit/scnnode.md) object (or instance of an [`SCNNode`](../../SceneKit/scnnode.md) subclass) containing any attachments you plan to use as a visual representation of the anchor. Note that ARKit controls the node’s visibility and its [`transform`](../../SceneKit/scnnode/transform.md) property, so you may find it useful to add child nodes or adjust the node’s [`pivot`](../../SceneKit/scnnode/pivot.md) property to maintain any changes to position or orientation that you make.

If you return `nil` from this method, no node is added to the scene.

Alternatively, if you do not implement this method, ARKit creates an empty node, and you can implement the [`renderer(_:didAdd:for:)`](./renderer%28_,didadd,for%29.md) method instead to provide visual content by attaching it to that node.

## Parameters

- `renderer`: The [`ARSCNView`](../arscnview.md) object rendering the scene.
- `anchor`: The anchor for which a node is requested.

## See Also

### Handling Content Updates
- [func renderer(any SCNSceneRenderer, didAdd: SCNNode, for: ARAnchor)](./renderer%28_,didadd,for%29.md)
  Tells the delegate that a SceneKit node corresponding to a new AR anchor has been added to the scene.
- [func renderer(any SCNSceneRenderer, willUpdate: SCNNode, for: ARAnchor)](./renderer%28_,willupdate,for%29.md)
  Tells the delegate that a SceneKit node’s properties will be updated to match the current state of its corresponding anchor.
- [func renderer(any SCNSceneRenderer, didUpdate: SCNNode, for: ARAnchor)](./renderer%28_,didupdate,for%29.md)
  Tells the delegate that a SceneKit node’s properties have been updated to match the current state of its corresponding anchor.
- [func renderer(any SCNSceneRenderer, didRemove: SCNNode, for: ARAnchor)](./renderer%28_,didremove,for%29.md)
  Tells the delegate that the SceneKit node corresponding to a removed AR anchor has been removed from the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnviewdelegate/renderer(_:nodefor:))*