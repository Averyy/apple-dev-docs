# session(_:didRemove:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that one or more anchors have been removed from the session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
optional func session(_ session: ARSession, didRemove anchors: [ARAnchor])
```

```objc
- (void) session:(ARSession *) session didRemoveAnchors:(NSArray<__kindof ARAnchor *> *) anchors;
```

## Discussion

Depending on the session configuration, ARKit may automatically remove anchors from a session.

If you display an AR experience using SceneKit or SpriteKit, you can instead implement one of the following methods instead to track not only the anchors in the session but also any corresponding SceneKit or SpriteKit content:

- [`ARSCNView`](../arscnview.md): [`renderer(_:didRemove:for:)`](../arscnviewdelegate/renderer%28_,didremove,for%29.md)
- [`ARSKView`](../arskview.md): [`view(_:didRemove:for:)`](../arskviewdelegate/view%28_,didremove,for%29.md)

## Parameters

- `session`: The session providing information.
- `anchors`: The anchors newly removed from the session.

## See Also

### Handling Content Updates
- [func session(ARSession, didAdd: [ARAnchor])](./session%28_,didadd%29.md)
  Tells the delegate that one or more anchors have been added to the session.
- [func session(ARSession, didUpdate: [ARAnchor])](./session%28_,didupdate%29-3qtt8.md)
  Tells the delegate that the session has adjusted the properties of one or more anchors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsessiondelegate/session(_:didremove:))*