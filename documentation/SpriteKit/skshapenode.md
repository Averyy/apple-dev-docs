# SKShapeNode

**Framework**: SpriteKit  
**Kind**: class

A mathematical shape that can be stroked or filled.

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
class SKShapeNode
```

## Mentions

- [Getting Started with Shape Nodes](getting-started-with-shape-nodes.md)
- [Creating a Shape Node from an Array of Points](creating-a-shape-node-from-an-array-of-points.md)
- [Animate the Warping of a Sprite](animate-the-warping-of-a-sprite.md)

#### Overview

`SKShapeNode` allows you to create onscreen graphical elements from mathematical points, lines, and curves. The advantage this has over rasterized graphics, such as those displayed by textures, is that shapes are rasterized dynamically at runtime to produce crisp detail and smoother edges.

## Topics

### First Steps
- [Getting Started with Shape Nodes](getting-started-with-shape-nodes.md)
  Create a filled or stroked shape from a path object.
### Creating a Shape from a Path
- [convenience init(path: CGPath)](skshapenode/init(path:).md)
  Creates a shape node from a Core Graphics path.
- [convenience init(path: CGPath, centered: Bool)](skshapenode/init(path:centered:).md)
  Creates a shape node from a Core Graphics path, centered around its position.
- [var path: CGPath?](skshapenode/path.md)
  The path that defines the shape.
### Creating a Shape from a Rectangle
- [convenience init(rect: CGRect)](skshapenode/init(rect:).md)
  Creates a shape node with a rectangular path.
- [convenience init(rectOf: CGSize)](skshapenode/init(rectof:).md)
  Creates a shape node with a rectangular path centered on the node’s origin.
- [convenience init(rect: CGRect, cornerRadius: CGFloat)](skshapenode/init(rect:cornerradius:).md)
  Creates a shape with a rectangular path that has rounded corners.
- [convenience init(rectOf: CGSize, cornerRadius: CGFloat)](skshapenode/init(rectof:cornerradius:).md)
  Creates a shape with a rectangular path that has rounded corners centered on the node’s position.
### Creating a Circle Shape
- [convenience init(circleOfRadius: CGFloat)](skshapenode/init(circleofradius:).md)
  Creates a shape node with a circular path centered on the node’s origin.
### Creating an Ellipse Shape
- [convenience init(ellipseOf: CGSize)](skshapenode/init(ellipseof:).md)
  Creates a shape node with an elliptical path centered on the node’s origin.
- [convenience init(ellipseIn: CGRect)](skshapenode/init(ellipsein:).md)
  Creates a shape node with an elliptical path that fills the specified rectangle.
### Creating a Shape from an Array of Points
- [Creating a Shape Node from an Array of Points](creating-a-shape-node-from-an-array-of-points.md)
  Create jagged or smooth shapes from the same array of points.
- [convenience init(points: UnsafeMutablePointer<CGPoint>, count: Int)](skshapenode/init(points:count:).md)
  Creates a shape node from a series of points.
- [convenience init(splinePoints: UnsafeMutablePointer<CGPoint>, count: Int)](skshapenode/init(splinepoints:count:).md)
  Creates a shape node from a series of spline points.
### Filling a Shape
- [var fillColor: UIColor](skshapenode/fillcolor.md)
  The color used to fill the shape.
- [var fillTexture: SKTexture?](skshapenode/filltexture.md)
  The texture used to fill the shape.
### Stroking a Shape
- [var lineWidth: CGFloat](skshapenode/linewidth.md)
  The width used to stroke the path.
- [var strokeColor: UIColor](skshapenode/strokecolor.md)
  The color used to stroke the shape.
- [var strokeTexture: SKTexture?](skshapenode/stroketexture.md)
  The texture used to stroke the shape.
- [var glowWidth: CGFloat](skshapenode/glowwidth.md)
  A glow that extends outward from the stroked line.
- [var lineCap: CGLineCap](skshapenode/linecap.md)
  The style used to render the endpoints of the stroked portion of the shape node.
- [var lineJoin: CGLineJoin](skshapenode/linejoin.md)
  The junction type used when the stroked portion of the shape node is rendered.
- [var miterLimit: CGFloat](skshapenode/miterlimit.md)
  The miter limit to use when the line is stroked using a miter join style.
- [var isAntialiased: Bool](skshapenode/isantialiased.md)
  A Boolean value that determines whether the stroked path is smoothed when drawn.
### Configuring Alpha Blending
- [var blendMode: SKBlendMode](skshapenode/blendmode.md)
  The blend mode used to blend the shape into the parent’s framebuffer.
### Controlling or Animating Sroke Length
- [var lineLength: CGFloat](skshapenode/linelength.md)
  The length of the line defined by the shape node.
### Customizing Stroking or Fill Drawing
- [Controlling Shape Drawing with Shaders](controlling-shape-drawing-with-shaders.md)
  Change a shape node’s appearance by supplying custom shader code.
- [var strokeShader: SKShader?](skshapenode/strokeshader.md)
  A custom shader used to determine the color of the stroked portion of the shape node.
- [var fillShader: SKShader?](skshapenode/fillshader.md)
  A custom shader used to determine the color of the filled portion of the shape node.
- [var attributeValues: [String : SKAttributeValue]](skshapenode/attributevalues.md)
  The values of each attribute associated with the node’s attached shader.
- [func setValue(SKAttributeValue, forAttribute: String)](skshapenode/setvalue(_:forattribute:).md)
  Sets an attribute value for an attached shader.
- [func value(forAttributeNamed: String) -> SKAttributeValue?](skshapenode/value(forattributenamed:).md)
  The value of a shader attribute.
### Instance Properties
- [var customPlaygroundQuickLook: PlaygroundQuickLook](skshapenode/customplaygroundquicklook.md)
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
- [class SKSpriteNode](skspritenode.md)
  An image or solid color.
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

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode)*