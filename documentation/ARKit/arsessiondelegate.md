# ARSessionDelegate

**Framework**: ARKit  
**Kind**: protocol

Methods you can implement to receive captured video frame images and tracking state from an AR session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol ARSessionDelegate : ARSessionObserver
```

#### Overview

Implement this protocol if you need to work directly with [`ARFrame`](arframe.md) objects captured by the session or directly follow changes to the session’s set of tracked [`ARAnchor`](aranchor.md) objects. Typically, you adopt this protocol when building a custom view for displaying AR content—if you display content with SceneKit or SpriteKit, the [`ARSCNViewDelegate`](arscnviewdelegate.md) and [`ARSKViewDelegate`](arskviewdelegate.md) protocols provide similar information and integrate with those technologies.

This protocol extends the [`ARSessionObserver`](arsessionobserver.md) protocol, so your session delegate can also implement those methods to respond to changes in session status.

## Topics

### Receiving Camera Frames
- [func session(ARSession, didUpdate: ARFrame)](arsessiondelegate/session(_:didupdate:)-9v2kw.md)
  Provides a newly captured camera image and accompanying AR information to the delegate.
### Handling Content Updates
- [func session(ARSession, didAdd: [ARAnchor])](arsessiondelegate/session(_:didadd:).md)
  Tells the delegate that one or more anchors have been added to the session.
- [func session(ARSession, didUpdate: [ARAnchor])](arsessiondelegate/session(_:didupdate:)-3qtt8.md)
  Tells the delegate that the session has adjusted the properties of one or more anchors.
- [func session(ARSession, didRemove: [ARAnchor])](arsessiondelegate/session(_:didremove:).md)
  Tells the delegate that one or more anchors have been removed from the session.

## Relationships

### Inherits From
- [ARSessionObserver](arsessionobserver.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any ARSessionDelegate)?](arsession/delegate.md)
  An object you provide to receive captured video images and tracking information, or to respond to changes in session status.
- [var delegateQueue: dispatch_queue_t?](arsession/delegatequeue.md)
  The dispatch queue through which the session calls your delegate methods.
- [protocol ARSessionObserver](arsessionobserver.md)
  Methods you can implement to respond to changes in the state of an AR session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsessiondelegate)*