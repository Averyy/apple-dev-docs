# ARSCNViewDelegate

**Framework**: ARKit  
**Kind**: protocol

Methods you can implement to mediate the automatic synchronization of SceneKit content with an AR session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol ARSCNViewDelegate : ARSessionObserver, SCNSceneRendererDelegate
```

## Mentions

- [Providing 3D Virtual Content with SceneKit](providing-3d-virtual-content-with-scenekit.md)

#### Overview

Implement this protocol to provide SceneKit content corresponding to [`ARAnchor`](aranchor.md) objects tracked by the view’s AR session, or to manage the view’s automatic updating of such content.

This protocol extends the [`ARSessionObserver`](arsessionobserver.md) protocol, so your session delegate can also implement those methods to respond to changes in session status.

## Topics

### Handling Content Updates
- [func renderer(any SCNSceneRenderer, nodeFor: ARAnchor) -> SCNNode?](arscnviewdelegate/renderer(_:nodefor:).md)
  Asks the delegate to provide a SceneKit node corresponding to a newly added anchor.
- [func renderer(any SCNSceneRenderer, didAdd: SCNNode, for: ARAnchor)](arscnviewdelegate/renderer(_:didadd:for:).md)
  Tells the delegate that a SceneKit node corresponding to a new AR anchor has been added to the scene.
- [func renderer(any SCNSceneRenderer, willUpdate: SCNNode, for: ARAnchor)](arscnviewdelegate/renderer(_:willupdate:for:).md)
  Tells the delegate that a SceneKit node’s properties will be updated to match the current state of its corresponding anchor.
- [func renderer(any SCNSceneRenderer, didUpdate: SCNNode, for: ARAnchor)](arscnviewdelegate/renderer(_:didupdate:for:).md)
  Tells the delegate that a SceneKit node’s properties have been updated to match the current state of its corresponding anchor.
- [func renderer(any SCNSceneRenderer, didRemove: SCNNode, for: ARAnchor)](arscnviewdelegate/renderer(_:didremove:for:).md)
  Tells the delegate that the SceneKit node corresponding to a removed AR anchor has been removed from the scene.

## Relationships

### Inherits From
- [ARSessionObserver](arsessionobserver.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [SCNSceneRendererDelegate](../SceneKit/SCNSceneRendererDelegate.md)

## See Also

- [var delegate: (any ARSCNViewDelegate)?](arscnview/delegate.md)
  An object you provide to mediate synchronization of the view’s AR scene information with SceneKit content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnviewdelegate)*