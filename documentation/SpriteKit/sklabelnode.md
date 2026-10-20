# SKLabelNode

**Framework**: SpriteKit  
**Kind**: class  
**Role**: Class

A graphical element that draws text.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class SKLabelNode
```

```objc
@interface SKLabelNode : SKNode
```

## Mentions

- [Adding Text to a Scene](./adding-text-to-a-scene.md)
- [Getting Started with Nodes](./getting-started-with-nodes.md)
- [Warping SpriteKit Content By Using an Effect Node](./warping-spritekit-content-by-using-an-effect-node.md)

#### Overview

`SKLabelNode` allows you to render text in your scene. You can define a custom style using properties such as [`fontName`](./sklabelnode/fontname.md) and [`fontColor`](./sklabelnode/fontcolor.md), or configure the look of your text with an [`NSAttributedString`](../Foundation/nsattributedstring.md).

## Topics

### Getting Started with Labels
- [Adding Text to a Scene](./adding-text-to-a-scene.md)
  Draw text in your scene, such as a health indicator or a “Game Over” banner, by using a label node.
### Creating a Label
- [init(fontNamed: String?)](./sklabelnode/init%28fontnamed%29.md)
  Initializes a new label object with a specified font.
- [convenience init(text: String?)](./sklabelnode/init%28text%29.md)
  Initializes a new label object with a text string.
- [convenience init(attributedText: NSAttributedString?)](./sklabelnode/init%28attributedtext%29.md)
  Initializes a new label object with an attributed text string.
### Setting a Label’s Text
- [var text: String?](./sklabelnode/text.md)
  The string that the label node displays.
- [var attributedText: NSAttributedString?](./sklabelnode/attributedtext.md)
  The attributed string displayed by the label.
### Specifying a Label’s Font
- [var fontColor: UIColor?](./sklabelnode/fontcolor.md)
  The color of the label.
- [var fontName: String?](./sklabelnode/fontname.md)
  The font used for the text in the label.
- [var fontSize: CGFloat](./sklabelnode/fontsize.md)
  The size of the font used in the label.
### Controlling a Label’s Alignment
- [var verticalAlignmentMode: SKLabelVerticalAlignmentMode](./sklabelnode/verticalalignmentmode.md)
  The vertical position of the text within the node.
- [enum SKLabelVerticalAlignmentMode](./sklabelverticalalignmentmode.md)
  Options for aligning text vertically.
- [var horizontalAlignmentMode: SKLabelHorizontalAlignmentMode](./sklabelnode/horizontalalignmentmode.md)
  The horizontal position of the text within the node.
- [enum SKLabelHorizontalAlignmentMode](./sklabelhorizontalalignmentmode.md)
  Options for aligning text horizontally.
### Defining a Label’s Line-Breaking Behavior
- [var preferredMaxLayoutWidth: CGFloat](./sklabelnode/preferredmaxlayoutwidth.md)
  The width, in screen points, after which line-break mode should be applied.
- [var lineBreakMode: NSLineBreakMode](./sklabelnode/linebreakmode.md)
  Determines the line-break mode for multiple lines.
- [var numberOfLines: Int](./sklabelnode/numberoflines.md)
  Determines the number of lines to draw.
### Colorizing a Label
- [var color: UIColor?](./sklabelnode/color.md)
  An alternative to the font color that can be used for animations.
- [var colorBlendFactor: CGFloat](./sklabelnode/colorblendfactor.md)
  A floating-point value that describes how the color is blended with the font color.
### Configuring Alpha Blending
- [var blendMode: SKBlendMode](./sklabelnode/blendmode.md)
  The blend mode used to draw the label into the parent’s framebuffer.

## Relationships

### Inherits From
- [SKNode](./sknode.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Nodes that Draw
- [Maximizing Node Drawing Performance](./maximizing-node-drawing-performance.md)
  Structure your nodes for maximum performance.
- [class SKSpriteNode](./skspritenode.md)
  An image or solid color.
- [class SKShapeNode](./skshapenode.md)
  A mathematical shape that can be stroked or filled.
- [class SKEmitterNode](./skemitternode.md)
  A source of various particle effects.
- [class SKVideoNode](./skvideonode.md)
  A graphical element that plays video content.
- [class SKTileMapNode](./sktilemapnode.md)
  A two-dimensional array of images.
- [class SK3DNode](./sk3dnode.md)
  3D SceneKit content drawn as a flattened sprite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sklabelnode)*