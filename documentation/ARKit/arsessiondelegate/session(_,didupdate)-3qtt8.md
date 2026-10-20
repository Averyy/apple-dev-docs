# session(_:didUpdate:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the session has adjusted the properties of one or more anchors.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
optional func session(_ session: ARSession, didUpdate anchors: [ARAnchor])
```

```objc
- (void) session:(ARSession *) session didUpdateAnchors:(NSArray<__kindof ARAnchor *> *) anchors;
```

#### Discussion

Depending on the session configuration, ARKit may automatically update the properties of anchors in a session.

If you display an AR experience using SceneKit or SpriteKit, you can implement one of the following methods instead to track not only the anchors in the session but also any corresponding SceneKit or SpriteKit content:

- [`ARSCNView`](../arscnview.md): [`renderer(_:willUpdate:for:)`](../arscnviewdelegate/renderer%28_,willupdate,for%29.md) or [`renderer(_:didUpdate:for:)`](../arscnviewdelegate/renderer%28_,didupdate,for%29.md)
- [`ARSKView`](../arskview.md): [`view(_:willUpdate:for:)`](../arskviewdelegate/view%28_,willupdate,for%29.md) or [`view(_:didUpdate:for:)`](../arskviewdelegate/view%28_,didupdate,for%29.md)

## Parameters

- `session`: The session providing information.
- `anchors`: The anchors whose properties have changed.

## See Also

### Handling Content Updates
- [func session(ARSession, didAdd: [ARAnchor])](./session%28_,didadd%29.md)
  Tells the delegate that one or more anchors have been added to the session.
- [func session(ARSession, didRemove: [ARAnchor])](./session%28_,didremove%29.md)
  Tells the delegate that one or more anchors have been removed from the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsessiondelegate/session(_:didupdate:)-3qtt8)*