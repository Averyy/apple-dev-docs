# renderingOrder

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The order the node’s content is drawn in relative to that of other nodes.

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
var renderingOrder: Int { get set }
```

```objc
@property (nonatomic) NSInteger renderingOrder;
```

## Discussion

Nodes with greater rendering orders are rendered last. Defaults to zero.

## See Also

### Modifying the Node Visibility
- [var isHidden: Bool](./ishidden.md)
  A Boolean value that determines the visibility of the node’s contents. Animatable.
- [var opacity: CGFloat](./opacity.md)
  The opacity value of the node. Animatable.
- [var castsShadow: Bool](./castsshadow.md)
  A Boolean value that determines whether SceneKit renders the node’s contents into shadow maps.
- [var movabilityHint: SCNMovabilityHint](./movabilityhint.md)
  A value that indicates how SceneKit should handle the node when rendering movement-related effects.
- [enum SCNMovabilityHint](../scnmovabilityhint.md)
  Values that inform SceneKit’s rendering for movement-related effects, used by the [`movabilityHint`](./movabilityhint.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/renderingorder)*