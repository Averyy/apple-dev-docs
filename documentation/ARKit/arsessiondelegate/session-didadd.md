# session(_:didAdd:)

**Framework**: ARKit  
**Kind**: method

Tells the delegate that one or more anchors have been added to the session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func session(_ session: ARSession, didAdd anchors: [ARAnchor])
```

#### Discussion

Depending on the session configuration, ARKit may automatically add anchors to a session.

If you display an AR experience using SceneKit or SpriteKit, you can instead implement one of the following methods instead to track not only the addition of anchors to the session but also how to add SceneKit or SpriteKit content to the corresponding scene:

- [`ARSCNView`](arscnview.md): [`renderer(_:nodeFor:)`](arscnviewdelegate/renderer(_:nodefor:).md) or [`renderer(_:didAdd:for:)`](arscnviewdelegate/renderer(_:didadd:for:).md)
- [`ARSKView`](arskview.md): [`node(for:)`](arskview/node(for:).md) or [`view(_:didAdd:for:)`](arskviewdelegate/view(_:didadd:for:).md)

## Parameters

- `session`: The session providing information.
- `anchors`: The anchors newly added to the session.

## See Also

- [func session(ARSession, didUpdate: [ARAnchor])](arsessiondelegate/session(_:didupdate:)-3qtt8.md)
  Tells the delegate that the session has adjusted the properties of one or more anchors.
- [func session(ARSession, didRemove: [ARAnchor])](arsessiondelegate/session(_:didremove:).md)
  Tells the delegate that one or more anchors have been removed from the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsessiondelegate/session(_:didadd:))*