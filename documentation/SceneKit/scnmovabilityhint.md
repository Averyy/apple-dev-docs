# SCNMovabilityHint

**Framework**: SceneKit  
**Kind**: enum  
**Role**: Enumeration

Values that inform SceneKit’s rendering for movement-related effects, used by the [`movabilityHint`](./scnnode/movabilityhint.md) property.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
enum SCNMovabilityHint
```

```c
enum SCNMovabilityHint : NSInteger;
```

## Topics

### Constants
- [SCNMovabilityHint.fixed](./scnmovabilityhint/fixed.md)
  The node is not expected to move over time.
- [SCNMovabilityHint.movable](./scnmovabilityhint/movable.md)
  The node is expected to move over time.
### Initializers
- [init?(rawValue: Int)](./scnmovabilityhint/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Modifying the Node Visibility
- [var isHidden: Bool](./scnnode/ishidden.md)
  A Boolean value that determines the visibility of the node’s contents. Animatable.
- [var opacity: CGFloat](./scnnode/opacity.md)
  The opacity value of the node. Animatable.
- [var renderingOrder: Int](./scnnode/renderingorder.md)
  The order the node’s content is drawn in relative to that of other nodes.
- [var castsShadow: Bool](./scnnode/castsshadow.md)
  A Boolean value that determines whether SceneKit renders the node’s contents into shadow maps.
- [var movabilityHint: SCNMovabilityHint](./scnnode/movabilityhint.md)
  A value that indicates how SceneKit should handle the node when rendering movement-related effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmovabilityhint)*