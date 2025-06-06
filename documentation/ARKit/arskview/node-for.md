# node(for:)

**Framework**: ARKit  
**Kind**: method

Returns the SpriteKit node associated with the specified AR anchor, if any.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func node(for anchor: ARAnchor) -> SKNode?
```

#### Return Value

The node whose position in the AR scene the anchor tracks, or `nil` if the anchor has no associated node or is not in the view’s AR session.

## Parameters

- `anchor`: An anchor in the view’s AR session.

## See Also

- [func anchor(for: SKNode) -> ARAnchor?](arskview/anchor(for:).md)
  Returns the AR anchor associated with the specified SpriteKit node, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskview/node(for:))*