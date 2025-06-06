# anchor(for:)

**Framework**: ARKit  
**Kind**: method

Returns the AR anchor associated with the specified SpriteKit node, if any.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func anchor(for node: SKNode) -> ARAnchor?
```

#### Return Value

The [`ARAnchor`](aranchor.md) object tracking the node, or `nil` if the node is not associated with an anchor or not in the view’s scene.

## Parameters

- `node`: A SpriteKit node in the view’s scene.

## See Also

- [func node(for: ARAnchor) -> SKNode?](arskview/node(for:).md)
  Returns the SpriteKit node associated with the specified AR anchor, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskview/anchor(for:))*