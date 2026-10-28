# anchor(for:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Returns the AR anchor associated with the specified SpriteKit node, if any.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
func anchor(for node: SKNode) -> ARAnchor?
```

```objc
- (ARAnchor *) anchorForNode:(SKNode *) node;
```

## Return Value

The [`ARAnchor`](../aranchor.md) object tracking the node, or `nil` if the node is not associated with an anchor or not in the view’s scene.

## Parameters

- `node`: A SpriteKit node in the view’s scene.

## See Also

### Mapping Content to Real-World Positions
- [func node(for: ARAnchor) -> SKNode?](./node%28for%29.md)
  Returns the SpriteKit node associated with the specified AR anchor, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskview/anchor(for:))*