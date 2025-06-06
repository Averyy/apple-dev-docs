# session(_:didUpdate:)

**Framework**: ARKit  
**Kind**: method

Tells the delegate that the session has adjusted the properties of one or more anchors.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func session(_ session: ARSession, didUpdate anchors: [ARAnchor])
```

#### Discussion

Depending on the session configuration, ARKit may automatically update the properties of anchors in a session.

If you display an AR experience using SceneKit or SpriteKit, you can implement one of the following methods instead to track not only the anchors in the session but also any corresponding SceneKit or SpriteKit content:

- [`ARSCNView`](arscnview.md): [`renderer(_:willUpdate:for:)`](arscnviewdelegate/renderer(_:willupdate:for:).md) or [`renderer(_:didUpdate:for:)`](arscnviewdelegate/renderer(_:didupdate:for:).md)
- [`ARSKView`](arskview.md): [`view(_:willUpdate:for:)`](arskviewdelegate/view(_:willupdate:for:).md) or [`view(_:didUpdate:for:)`](arskviewdelegate/view(_:didupdate:for:).md)

## Parameters

- `session`: The session providing information.
- `anchors`: The anchors whose properties have changed.

## See Also

- [func session(ARSession, didAdd: [ARAnchor])](arsessiondelegate/session(_:didadd:).md)
  Tells the delegate that one or more anchors have been added to the session.
- [func session(ARSession, didRemove: [ARAnchor])](arsessiondelegate/session(_:didremove:).md)
  Tells the delegate that one or more anchors have been removed from the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsessiondelegate/session(_:didupdate:)-3qtt8)*