# opacity

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The opacity value of the node. Animatable.

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
var opacity: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat opacity;
```

## Mentions

- [Animating SceneKit Content](../animating-scenekit-content.md)

#### Discussion

Possible values are between `0.0` (fully transparent) and `1.0` (fully opaque). The default is `1.0`.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Modifying the Node Visibility
- [var isHidden: Bool](./ishidden.md)
  A Boolean value that determines the visibility of the node’s contents. Animatable.
- [var renderingOrder: Int](./renderingorder.md)
  The order the node’s content is drawn in relative to that of other nodes.
- [var castsShadow: Bool](./castsshadow.md)
  A Boolean value that determines whether SceneKit renders the node’s contents into shadow maps.
- [var movabilityHint: SCNMovabilityHint](./movabilityhint.md)
  A value that indicates how SceneKit should handle the node when rendering movement-related effects.
- [enum SCNMovabilityHint](../scnmovabilityhint.md)
  Values that inform SceneKit’s rendering for movement-related effects, used by the [`movabilityHint`](./movabilityhint.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/opacity)*