# isHidden

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines the visibility of the node’s contents. Animatable.

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
var isHidden: Bool { get set }
```

```objc
@property (nonatomic, getter=isHidden) BOOL hidden;
```

## Discussion

The default value of this property is NO, specifying that SceneKit should render geometries and use lights attached to the node or its children. Change this property’s value to [`true`](../../Swift/true.md) to exclude attached geometries and lights from rendering. (Cameras attached to the node or its children are not affected by this property.) Hiding a node also hides its child nodes recursively.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md). Hiding or showing a node in an animation results in a fade-in or fade-out effect.

## See Also

### Modifying the Node Visibility
- [var opacity: CGFloat](./opacity.md)
  The opacity value of the node. Animatable.
- [var renderingOrder: Int](./renderingorder.md)
  The order the node’s content is drawn in relative to that of other nodes.
- [var castsShadow: Bool](./castsshadow.md)
  A Boolean value that determines whether SceneKit renders the node’s contents into shadow maps.
- [var movabilityHint: SCNMovabilityHint](./movabilityhint.md)
  A value that indicates how SceneKit should handle the node when rendering movement-related effects.
- [enum SCNMovabilityHint](../scnmovabilityhint.md)
  Values that inform SceneKit’s rendering for movement-related effects, used by the [`movabilityHint`](./movabilityhint.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/ishidden)*