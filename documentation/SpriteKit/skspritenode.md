# SKSpriteNode

**Framework**: SpriteKit  
**Kind**: class

An image or solid color.

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
class SKSpriteNode
```

## Mentions

- [Getting Started with Shape Nodes](getting-started-with-shape-nodes.md)
- [Animate the Warping of a Sprite](animate-the-warping-of-a-sprite.md)
- [Adding a Video to a Scene](adding-a-video-to-a-scene.md)
- [Customizing the Behavior of a Node](customizing-the-behavior-of-a-node.md)
- [Getting Started with Nodes](getting-started-with-nodes.md)
- [Drawing SpriteKit Content in a View](drawing-spritekit-content-in-a-view.md)
- [Loading and Using Textures](loading-and-using-textures.md)

#### Overview

`SKSpriteNode` is an onscreen graphical element that can be initialized from an image or a solid color. SpriteKit adds functionality to its ability to display images using the functions discussed below.

## Topics

### Creating a Sprite from an Image Filename
- [Getting Started with Sprite Nodes](getting-started-with-sprite-nodes.md)
  Learn the basics about using images, also known as sprites, with SpriteKit.
- [convenience init(imageNamed: String)](skspritenode/init(imagenamed:).md)
  Initializes a textured sprite using an image file.
- [convenience init(imageNamed: String, normalMapped: Bool)](skspritenode/init(imagenamed:normalmapped:).md)
  Initializes a textured sprite using an image file, optionally adding a normal map to simulate 3D lighting.
### Creating a Sprite from a Texture
- [convenience init(texture: SKTexture?)](skspritenode/init(texture:).md)
  Initializes a textured sprite using an existing texture object.
- [init(texture: SKTexture?, color: UIColor, size: CGSize)](skspritenode/init(texture:color:size:).md)
  Initializes a textured sprite in color using an existing texture object.
- [convenience init(texture: SKTexture?, size: CGSize)](skspritenode/init(texture:size:).md)
  Initializes a textured sprite using an existing texture object but with a specified size.
- [convenience init(texture: SKTexture?, normalMap: SKTexture?)](skspritenode/init(texture:normalmap:).md)
  Initializes a textured sprite with a normal map to simulate 3D lighting.
- [var texture: SKTexture?](skspritenode/texture.md)
  The texture used to draw the sprite.
### Creating a Solid-Color Sprite
- [convenience init(color: UIColor, size: CGSize)](skspritenode/init(color:size:).md)
  Initializes a single-color sprite node.
### Initializing a Sprite from an Archive
- [init?(coder: NSCoder)](skspritenode/init(coder:).md)
  Tells you when to initialize a sprite from an archive.
### Setting a Sprite’s Size and Position
- [Using the Anchor Point to Move a Sprite](using-the-anchor-point-to-move-a-sprite.md)
  Learn how the anchor point affects a sprite’s position.
- [var size: CGSize](skspritenode/size.md)
  The dimensions of the sprite, in points.
- [func scale(to: CGSize)](skspritenode/scale(to:).md)
  Scales the sprite node to a specified size.
- [var anchorPoint: CGPoint](skspritenode/anchorpoint.md)
  Defines the point in the sprite that corresponds to the node’s position.
### Scaling a Sprite in Nine Parts
- [Resizing a Sprite in Nine Parts](resizing-a-sprite-in-nine-parts.md)
  Scale a sprite using nine-part algorithm.
- [var centerRect: CGRect](skspritenode/centerrect.md)
  Enable nine-part stretching of the sprite’s texture.
### Tinting a Sprite
- [Tinting a Sprite](tinting-a-sprite.md)
  Provide a color and blend factor to additively color your sprite.
- [var color: UIColor](skspritenode/color.md)
  The sprite’s color.
- [var colorBlendFactor: CGFloat](skspritenode/colorblendfactor.md)
  A floating-point value that describes how the color is blended with the sprite’s texture.
### Configuring Alpha Blendling
- [Blending a Sprite with Different Interpretations of Alpha](blending-a-sprite-with-different-interpretations-of-alpha.md)
  Reinterpret a sprite’s alpha property to react differently to the objects below it.
- [var blendMode: SKBlendMode](skspritenode/blendmode.md)
  The blend mode used to draw the sprite into the parent’s framebuffer.
- [enum SKBlendMode](skblendmode.md)
  The modes that describe how the source and destination pixel colors are used to calculate the new destination color.
### Lighting a Sprite
- [Lighting a Sprite with Light Nodes](lighting-a-sprite-with-light-nodes.md)
  Add lighting and shadows to your scene with light nodes.
- [var lightingBitMask: UInt32](skspritenode/lightingbitmask.md)
  A mask that defines how this sprite is lit by light nodes in the scene.
- [var shadowedBitMask: UInt32](skspritenode/shadowedbitmask.md)
  A mask that defines which lights add shadows to the sprite.
- [var shadowCastBitMask: UInt32](skspritenode/shadowcastbitmask.md)
  A mask that defines which lights are occluded by this sprite.
- [var normalTexture: SKTexture?](skspritenode/normaltexture.md)
  A texture that specifies the normal map for the sprite.
### Adding a Custom Shader to a Sprite
- [Applying Shaders to a Sprite](applying-shaders-to-a-sprite.md)
  Write custom GLSL code that modifies the look of your sprite.
- [var shader: SKShader?](skspritenode/shader.md)
  A text file that defines code that does custom per-pixel drawing or colorization.
- [var attributeValues: [String : SKAttributeValue]](skspritenode/attributevalues.md)
  The values of each attribute associated with the node’s attached shader.
- [func setValue(SKAttributeValue, forAttribute: String)](skspritenode/setvalue(_:forattribute:).md)
  Sets an attribute value for an attached shader.
- [func value(forAttributeNamed: String) -> SKAttributeValue?](skspritenode/value(forattributenamed:).md)
  Sets the value of a shader attribute.
### Animating a Sprite by Changing its Texture
- [Animating a Sprite by Changing its Texture](animating-a-sprite-by-changing-its-texture.md)
  Load a sequence of images and play them back at a rate you define, while optionally looping the resulting animation.
### Instance Properties
- [var customPlaygroundQuickLook: PlaygroundQuickLook](skspritenode/customplaygroundquicklook.md)
  A custom playground quick look for this instance.

## Relationships

### Inherits From
- [SKNode](sknode.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
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
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [Maximizing Node Drawing Performance](maximizing-node-drawing-performance.md)
  Structure your nodes for maximum performance.
- [class SKShapeNode](skshapenode.md)
  A mathematical shape that can be stroked or filled.
- [class SKEmitterNode](skemitternode.md)
  A source of various particle effects.
- [class SKLabelNode](sklabelnode.md)
  A graphical element that draws text.
- [class SKVideoNode](skvideonode.md)
  A graphical element that plays video content.
- [class SKTileMapNode](sktilemapnode.md)
  A two-dimensional array of images.
- [class SK3DNode](sk3dnode.md)
  3D SceneKit content drawn as a flattened sprite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode)*