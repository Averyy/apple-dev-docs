# SCNMovabilityHint

**Framework**: SceneKit  
**Kind**: enum

Values that inform SceneKit’s rendering for movement-related effects, used by the [`movabilityHint`](scnnode/movabilityhint.md) property.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum SCNMovabilityHint
```

## Topics

### Constants
- [SCNMovabilityHint.fixed](scnmovabilityhint/fixed.md)
  The node is not expected to move over time.
- [SCNMovabilityHint.movable](scnmovabilityhint/movable.md)
  The node is expected to move over time.
### Initializers
- [init?(rawValue: Int)](scnmovabilityhint/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var isHidden: Bool](scnnode/ishidden.md)
  A Boolean value that determines the visibility of the node’s contents. Animatable.
- [var opacity: CGFloat](scnnode/opacity.md)
  The opacity value of the node. Animatable.
- [var renderingOrder: Int](scnnode/renderingorder.md)
  The order the node’s content is drawn in relative to that of other nodes.
- [var castsShadow: Bool](scnnode/castsshadow.md)
  A Boolean value that determines whether SceneKit renders the node’s contents into shadow maps.
- [var movabilityHint: SCNMovabilityHint](scnnode/movabilityhint.md)
  A value that indicates how SceneKit should handle the node when rendering movement-related effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmovabilityhint)*