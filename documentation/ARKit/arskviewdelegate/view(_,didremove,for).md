# view(_:didRemove:for:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the SpriteKit node corresponding to an AR anchor has been removed from the scene.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
optional func view(_ view: ARSKView, didRemove node: SKNode, for anchor: ARAnchor)
```

```objc
- (void) view:(ARSKView *) view didRemoveNode:(SKNode *) node forAnchor:(ARAnchor *) anchor;
```

## Discussion

Depending on the session configuration, ARKit may automatically remove anchors from a session. The view calls this method once for each removed anchor.

## Parameters

- `view`: The [`ARSKView`](../arskview.md) object rendering the scene.
- `node`: The removed SpriteKit node.
- `anchor`: The AR anchor corresponding to the node.

## See Also

### Handling Content Updates
- [func view(ARSKView, nodeFor: ARAnchor) -> SKNode?](./view%28_,nodefor%29.md)
  Asks the delegate to provide a SpriteKit node corresponding to a newly added anchor.
- [func view(ARSKView, didAdd: SKNode, for: ARAnchor)](./view%28_,didadd,for%29.md)
  Tells the delegate that a SpriteKit node corresponding to a new AR anchor has been added to the scene.
- [func view(ARSKView, willUpdate: SKNode, for: ARAnchor)](./view%28_,willupdate,for%29.md)
  Tells the delegate that a SpriteKit node’s properties will be updated to match the current state of its corresponding anchor.
- [func view(ARSKView, didUpdate: SKNode, for: ARAnchor)](./view%28_,didupdate,for%29.md)
  Tells the delegate that a SpriteKit node’s properties have been updated to match the current state of its corresponding anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskviewdelegate/view(_:didremove:for:))*