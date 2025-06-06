# session(_:didRemove:)

**Framework**: ARKit  
**Kind**: method

Tells the delegate that one or more anchors have been removed from the session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func session(_ session: ARSession, didRemove anchors: [ARAnchor])
```

#### Discussion

Depending on the session configuration, ARKit may automatically remove anchors from a session.

If you display an AR experience using SceneKit or SpriteKit, you can instead implement one of the following methods instead to track not only the anchors in the session but also any corresponding SceneKit or SpriteKit content:

- [`ARSCNView`](arscnview.md): [`renderer(_:didRemove:for:)`](arscnviewdelegate/renderer(_:didremove:for:).md)
- [`ARSKView`](arskview.md): [`view(_:didRemove:for:)`](arskviewdelegate/view(_:didremove:for:).md)

## Parameters

- `session`: The session providing information.
- `anchors`: The anchors newly removed from the session.

## See Also

- [func session(ARSession, didAdd: [ARAnchor])](arsessiondelegate/session(_:didadd:).md)
  Tells the delegate that one or more anchors have been added to the session.
- [func session(ARSession, didUpdate: [ARAnchor])](arsessiondelegate/session(_:didupdate:)-3qtt8.md)
  Tells the delegate that the session has adjusted the properties of one or more anchors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsessiondelegate/session(_:didremove:))*