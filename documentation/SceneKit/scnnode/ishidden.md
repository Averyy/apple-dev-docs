# isHidden

**Framework**: SceneKit  
**Kind**: property

A Boolean value that determines the visibility of the node’s contents. Animatable.

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
var isHidden: Bool { get set }
```

#### Discussion

The default value of this property is NO, specifying that SceneKit should render geometries and use lights attached to the node or its children. Change this property’s value to [`true`](https://developer.apple.com/documentation/swift/true) to exclude attached geometries and lights from rendering. (Cameras attached to the node or its children are not affected by this property.) Hiding a node also hides its child nodes recursively.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md). Hiding or showing a node in an animation results in a fade-in or fade-out effect.

## See Also

- [var opacity: CGFloat](scnnode/opacity.md)
  The opacity value of the node. Animatable.
- [var renderingOrder: Int](scnnode/renderingorder.md)
  The order the node’s content is drawn in relative to that of other nodes.
- [var castsShadow: Bool](scnnode/castsshadow.md)
  A Boolean value that determines whether SceneKit renders the node’s contents into shadow maps.
- [var movabilityHint: SCNMovabilityHint](scnnode/movabilityhint.md)
  A value that indicates how SceneKit should handle the node when rendering movement-related effects.
- [enum SCNMovabilityHint](scnmovabilityhint.md)
  Values that inform SceneKit’s rendering for movement-related effects, used by the [`movabilityHint`](scnnode/movabilityhint.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/ishidden)*