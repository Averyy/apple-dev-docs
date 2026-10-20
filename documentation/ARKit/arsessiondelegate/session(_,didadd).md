# session(_:didAdd:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that one or more anchors have been added to the session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
optional func session(_ session: ARSession, didAdd anchors: [ARAnchor])
```

```objc
- (void) session:(ARSession *) session didAddAnchors:(NSArray<__kindof ARAnchor *> *) anchors;
```

#### Discussion

Depending on the session configuration, ARKit may automatically add anchors to a session.

If you display an AR experience using SceneKit or SpriteKit, you can instead implement one of the following methods instead to track not only the addition of anchors to the session but also how to add SceneKit or SpriteKit content to the corresponding scene:

- [`ARSCNView`](../arscnview.md): [`renderer(_:nodeFor:)`](../arscnviewdelegate/renderer%28_,nodefor%29.md) or [`renderer(_:didAdd:for:)`](../arscnviewdelegate/renderer%28_,didadd,for%29.md)
- [`ARSKView`](../arskview.md): [`node(for:)`](../arskview/node%28for%29.md) or [`view(_:didAdd:for:)`](../arskviewdelegate/view%28_,didadd,for%29.md)

## Parameters

- `session`: The session providing information.
- `anchors`: The anchors newly added to the session.

## See Also

### Handling Content Updates
- [func session(ARSession, didUpdate: [ARAnchor])](./session%28_,didupdate%29-3qtt8.md)
  Tells the delegate that the session has adjusted the properties of one or more anchors.
- [func session(ARSession, didRemove: [ARAnchor])](./session%28_,didremove%29.md)
  Tells the delegate that one or more anchors have been removed from the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsessiondelegate/session(_:didadd:))*