# node(for:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Returns the SpriteKit node associated with the specified AR anchor, if any.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
func node(for anchor: ARAnchor) -> SKNode?
```

```objc
- (SKNode *) nodeForAnchor:(ARAnchor *) anchor;
```

#### Return Value

The node whose position in the AR scene the anchor tracks, or `nil` if the anchor has no associated node or is not in the view’s AR session.

## Parameters

- `anchor`: An anchor in the view’s AR session.

## See Also

### Mapping Content to Real-World Positions
- [func anchor(for: SKNode) -> ARAnchor?](./anchor%28for%29.md)
  Returns the AR anchor associated with the specified SpriteKit node, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskview/node(for:))*