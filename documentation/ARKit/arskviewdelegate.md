# ARSKViewDelegate

**Framework**: ARKit  
**Kind**: protocol

Methods you can implement to mediate the automatic synchronization of SpriteKit content with an AR session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol ARSKViewDelegate : ARSessionObserver, SKViewDelegate
```

#### Overview

Implement this protocol to provide SpriteKit content corresponding to [`ARAnchor`](aranchor.md) objects tracked by the view’s AR session, or to manage the view’s automatic updating of such content.

This protocol extends the [`ARSessionObserver`](arsessionobserver.md) protocol, so your session delegate can also implement those methods to respond to changes in session status.

## Topics

### Handling Content Updates
- [func view(ARSKView, nodeFor: ARAnchor) -> SKNode?](arskviewdelegate/view(_:nodefor:).md)
  Asks the delegate to provide a SpriteKit node corresponding to a newly added anchor.
- [func view(ARSKView, didAdd: SKNode, for: ARAnchor)](arskviewdelegate/view(_:didadd:for:).md)
  Tells the delegate that a SpriteKit node corresponding to a new AR anchor has been added to the scene.
- [func view(ARSKView, willUpdate: SKNode, for: ARAnchor)](arskviewdelegate/view(_:willupdate:for:).md)
  Tells the delegate that a SpriteKit node’s properties will be updated to match the current state of its corresponding anchor.
- [func view(ARSKView, didUpdate: SKNode, for: ARAnchor)](arskviewdelegate/view(_:didupdate:for:).md)
  Tells the delegate that a SpriteKit node’s properties have been updated to match the current state of its corresponding anchor.
- [func view(ARSKView, didRemove: SKNode, for: ARAnchor)](arskviewdelegate/view(_:didremove:for:).md)
  Tells the delegate that the SpriteKit node corresponding to an AR anchor has been removed from the scene.

## Relationships

### Inherits From
- [ARSessionObserver](arsessionobserver.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [SKViewDelegate](../SpriteKit/SKViewDelegate.md)

## See Also

- [var delegate: (any ARSKViewDelegate)?](arskview/delegate.md)
  An object you provide to mediate synchronization of the view’s AR scene information with SpriteKit content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskviewdelegate)*