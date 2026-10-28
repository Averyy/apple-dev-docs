# movabilityHint

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A value that indicates how SceneKit should handle the node when rendering movement-related effects.

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
var movabilityHint: SCNMovabilityHint { get set }
```

```objc
@property (nonatomic) SCNMovabilityHint movabilityHint;
```

## Discussion

This property controls how the node contributes to various motion-related effects during rendering. The default value is [`SCNMovabilityHint.fixed`](../scnmovabilityhint/fixed.md). If the movability hint is [`SCNMovabilityHint.movable`](../scnmovabilityhint/movable.md):

- The node’s content is not affected by motion blur effects. (See the [`motionBlurIntensity`](../scncamera/motionblurintensity.md) camera property, which applies motion blur effects for camera movement but not subject movement.)
- The node does not contribute to environmental lighting of other objects. Environmental lighting is an aspect of physically based rendering (see [`physicallyBased`](../scnmaterial/lightingmodel-swift.struct/physicallybased.md)), in which surfaces tend to pick up the color of other scene content around them. SceneKit performs environmental lighting by rendering light probes—small, omnidirectional snapshots of the scene’s contents, as visible from at various points around the scene. Light probes are static, so nodes that are expected to move should not contribute to the lighting environment for other surfaces.

This value is merely a hint that communicates to SceneKit’s rendering system about how you want to move content in your scene; it does not affect your ability to change the node’s position or add animations or physics to the node.

## See Also

### Modifying the Node Visibility
- [var isHidden: Bool](./ishidden.md)
  A Boolean value that determines the visibility of the node’s contents. Animatable.
- [var opacity: CGFloat](./opacity.md)
  The opacity value of the node. Animatable.
- [var renderingOrder: Int](./renderingorder.md)
  The order the node’s content is drawn in relative to that of other nodes.
- [var castsShadow: Bool](./castsshadow.md)
  A Boolean value that determines whether SceneKit renders the node’s contents into shadow maps.
- [enum SCNMovabilityHint](../scnmovabilityhint.md)
  Values that inform SceneKit’s rendering for movement-related effects, used by the [`movabilityHint`](./movabilityhint.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/movabilityhint)*