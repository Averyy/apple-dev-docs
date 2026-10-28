# castsShadow

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether SceneKit renders the node’s contents into shadow maps.

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
var castsShadow: Bool { get set }
```

```objc
@property (nonatomic) BOOL castsShadow;
```

## Discussion

SceneKit renders shadows by rendering a *shadow map* image containing silhouettes of the scene’s contents, and then projecting that image onto the scene. SceneKit performs this process once for each [`SCNLight`](../scnlight.md) object in the scene whose [`castsShadow`](../scnlight/castsshadow.md) property is [`true`](../../Swift/true.md). Because shadow map rendering re-renders portions of the scene, it incurs a performance cost. To minimize this performance cost, exclude nodes from shadow map rendering by setting the node’s [`castsShadow`](./castsshadow.md) property to [`false`](../../Swift/false.md).

For more details on shadow rendering, see [`SCNLight`](../scnlight.md).

## See Also

### Modifying the Node Visibility
- [var isHidden: Bool](./ishidden.md)
  A Boolean value that determines the visibility of the node’s contents. Animatable.
- [var opacity: CGFloat](./opacity.md)
  The opacity value of the node. Animatable.
- [var renderingOrder: Int](./renderingorder.md)
  The order the node’s content is drawn in relative to that of other nodes.
- [var movabilityHint: SCNMovabilityHint](./movabilityhint.md)
  A value that indicates how SceneKit should handle the node when rendering movement-related effects.
- [enum SCNMovabilityHint](../scnmovabilityhint.md)
  Values that inform SceneKit’s rendering for movement-related effects, used by the [`movabilityHint`](./movabilityhint.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/castsshadow)*