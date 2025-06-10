# opacity

**Framework**: SceneKit  
**Kind**: property

The opacity value of the node. Animatable.

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
var opacity: CGFloat { get set }
```

## Mentions

- [Animating SceneKit Content](animating-scenekit-content.md)

#### Discussion

Possible values are between `0.0` (fully transparent) and `1.0` (fully opaque). The default is `1.0`.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var isHidden: Bool](scnnode/ishidden.md)
  A Boolean value that determines the visibility of the node’s contents. Animatable.
- [var renderingOrder: Int](scnnode/renderingorder.md)
  The order the node’s content is drawn in relative to that of other nodes.
- [var castsShadow: Bool](scnnode/castsshadow.md)
  A Boolean value that determines whether SceneKit renders the node’s contents into shadow maps.
- [var movabilityHint: SCNMovabilityHint](scnnode/movabilityhint.md)
  A value that indicates how SceneKit should handle the node when rendering movement-related effects.
- [enum SCNMovabilityHint](scnmovabilityhint.md)
  Values that inform SceneKit’s rendering for movement-related effects, used by the [`movabilityHint`](scnnode/movabilityhint.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/opacity)*