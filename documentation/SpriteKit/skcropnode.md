# SKCropNode

**Framework**: SpriteKit  
**Kind**: class

A node that masks pixels drawn by its children so that only some pixels are seen.

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
class SKCropNode
```

## Mentions

- [About Node Drawing Order](about-node-drawing-order.md)

#### Overview

`SKCropNode` is a container node that you use to crop other nodes in the scene. You add other nodes to a crop node and set the crop node’s [`maskNode`](skcropnode/masknode.md) property. For example, here are some ways you might specify a mask:

- An untextured sprite that limits content to a rectangular portion of the scene.
- A textured sprite that works as a precise per-pixel mask.
- A collection of child nodes that form a unique shape.

You can animate the shape or contents of the mask to implement interesting effects such as hiding or revealing.

> 💡 **Tip**:  Use crop nodes sparingly. Because they require an additional offscreen memory buffer to perform the crop and add a rendering operation into the offscreen buffer, they add notably more overhead to the app.

## Topics

### First Steps
- [Cropping Nodes](cropping-nodes.md)
  Use a texture or a shape to mask pixels out of a crop node’s children.
### Setting the Mask Filter
- [var maskNode: SKNode?](skcropnode/masknode.md)
  The node used to determine the crop node’s mask.

## Relationships

### Inherits From
- [SKNode](sknode.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UICoordinateSpace](../uikit/uicoordinatespace.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIFocusItem](../uikit/uifocusitem.md)
- [UIFocusItemContainer](../uikit/uifocusitemcontainer.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [class SKEffectNode](skeffectnode.md)
  A node that renders its children into a separate buffer, optionally applying an effect, before drawing the final result.
- [class SKTransformNode](sktransformnode.md)
  A node that allows its children to rotate in 3D.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skcropnode)*