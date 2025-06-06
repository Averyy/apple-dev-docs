# Converting Coordinate Spaces

**Framework**: SpriteKit

Convert positions across the various coordinate spaces in a scene.

#### Overview

When working with the node tree, sometimes you need to convert a position from one coordinate space to another. For example, when specifying joints in the physics system, the joint positions are specified in scene coordinates. So, if you have those points in a local coordinate system, you need to convert them to the scene’s coordinate space.

The following code shows how to convert a node’s position into the scene coordinate system. The scene is asked to perform the conversion. Remember that a node’s position is specified in its parent’s coordinate system, so the code passes `node.parent` as the node to convert from. You could perform the same conversion in reverse by calling the [`convert(_:to:)`](sknode/convert(_:to:).md) method.

One situation where you need to perform coordinate conversions is when you perform event handling. Mouse and touch events need to be converted from window coordinates to view coordinates, and from there into the scene. To simplify the code you need to write, SpriteKit adds a few convenience methods:

- In iOS, use the [`location(in:)`](https://developer.apple.com/documentation/UIKit/UITouch/location(in:)-44h4k) and [`previousLocation(in:)`](https://developer.apple.com/documentation/UIKit/UITouch/previousLocation(in:)-ea29) on [`UITouch`](https://developer.apple.com/documentation/UIKit/UITouch) objects to convert a touch location into a node’s coordinate system.
- In macOS, use the [`location(in:)`](https://developer.apple.com/documentation/AppKit/NSEvent/location(in:)) method on [`NSEvent`](https://developer.apple.com/documentation/AppKit/NSEvent) objects to convert a mouse event into a node’s coordinate system.

## See Also

- [func convert(CGPoint, from: SKNode) -> CGPoint](sknode/convert(_:from:).md)
  Converts a point from the coordinate system of another node in the node tree to the coordinate system of this node.
- [func convert(CGPoint, to: SKNode) -> CGPoint](sknode/convert(_:to:).md)
  Converts a point in this node’s coordinate system to the coordinate system of another node in the node tree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/converting-coordinate-spaces)*