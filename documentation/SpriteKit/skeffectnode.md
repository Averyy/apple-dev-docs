# SKEffectNode

**Framework**: SpriteKit  
**Kind**: class

A node that renders its children into a separate buffer, optionally applying an effect, before drawing the final result.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
@MainActor
class SKEffectNode
```

## Mentions

- [About Node Drawing Order](about-node-drawing-order.md)
- [Adding a Video to a Scene](adding-a-video-to-a-scene.md)
- [Warping SpriteKit Content By Using an Effect Node](warping-spritekit-content-by-using-an-effect-node.md)
- [Creating a New Node By Rendering To a Texture](creating-a-new-node-by-rendering-to-a-texture.md)
- [Animate the Warping of a Sprite](animate-the-warping-of-a-sprite.md)

#### Overview

An [`SKEffectNode`](skeffectnode.md) object renders its children into a buffer and optionally applies a Core Image filter to this rendered output. Because effect nodes conform to [`SKWarpable`](skwarpable.md), you can also use them to apply distortions to nodes that don’t implement the protocol, such as shape and video nodes. Use effect nodes to incorporate sophisticated special effects into a scene or to cache the contents of a static subtree for faster rendering performance.

Each time a new frame is rendered using the effect node, the effect node follows these steps:

1. It draws its children into a private framebuffer.
2. It applies a Core Image effect to the private framebuffer. This stage is optional; see the [`filter`](skeffectnode/filter.md) and [`shouldEnableEffects`](skeffectnode/shouldenableeffects.md) properties.
3. It blends the contents of its private framebuffer into its parent’s framebuffer, using one of the standard sprite blend modes.
4. It discards its private framebuffer. This step is optional; see the [`shouldRasterize`](skeffectnode/shouldrasterize.md) property.

## Topics

### Applying Core Image Filters with an Effect Node
- [Applying Special Effects to a Node’s Children](applying-special-effects-to-a-node-s-children.md)
  Apply the Core Image suite of filters to child nodes of an effect node.
- [var filter: CIFilter?](skeffectnode/filter.md)
  The Core Image filter to apply.
- [var shouldEnableEffects: Bool](skeffectnode/shouldenableeffects.md)
  A Boolean value that determines whether the effect node applies the filter to its children as they are drawn.
- [var shouldCenterFilter: Bool](skeffectnode/shouldcenterfilter.md)
  A Boolean value that determines whether the effect node automatically sets the filter’s image center.
### Warping Nodes with an Effect Node
- [Warping SpriteKit Content By Using an Effect Node](warping-spritekit-content-by-using-an-effect-node.md)
  Distort the child nodes of an effect node by applying a warping effect.
### Applying a Shader with an Effect Node
- [var shader: SKShader?](skeffectnode/shader.md)
  A custom shader that is called when the effect node is blended into the parent’s framebuffer.
- [var attributeValues: [String : SKAttributeValue]](skeffectnode/attributevalues.md)
  The values of each attribute associated with the node’s attached shader.
- [func setValue(SKAttributeValue, forAttribute: String)](skeffectnode/setvalue(_:forattribute:).md)
  Sets an attribute value for an attached shader.
- [func value(forAttributeNamed: String) -> SKAttributeValue?](skeffectnode/value(forattributenamed:).md)
  Gets the value of a shader attribute.
### Flattening an Effect Node’s Child Tree for Performance Improvement
- [Improving the Performance of Static Content](improving-the-performance-of-static-content.md)
  Flatten a portion of your node hierarchy to a single texture to improve performance.
- [var shouldRasterize: Bool](skeffectnode/shouldrasterize.md)
  A Boolean value that indicates whether the results of rendering the child nodes should be cached.
### Configuring Alpha Blending
- [var blendMode: SKBlendMode](skeffectnode/blendmode.md)
  The blend mode used to draw the node’s contents into its parent’s framebuffer.

## Relationships

### Inherits From
- [SKNode](sknode.md)
### Inherited By
- [SKScene](skscene.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [SKWarpable](skwarpable.md)
- [Sendable](../Swift/Sendable.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [class SKCropNode](skcropnode.md)
  A node that masks pixels drawn by its children so that only some pixels are seen.
- [class SKTransformNode](sktransformnode.md)
  A node that allows its children to rotate in 3D.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skeffectnode)*