# Creating a Shape Node from an Array of Points

**Framework**: SpriteKit

Create jagged or smooth shapes from the same array of points.

#### Overview

An [`SKShapeNode`](skshapenode.md) object can be initialized with an array of points describing a path. The [`init(splinePoints:count:)`](skshapenode/init(splinepoints:count:).md) method can smoothly interpolate between these points to create a curve rather than the series of straight lines created by [`init(points:count:)`](skshapenode/init(points:count:).md). The following Swift code shows how to create two shape nodes using the same array of points for both initializers.

```swift
var points = [CGPoint(x: 0, y: 0),               
              CGPoint(x: 100, y: 100),               
              CGPoint(x: 200, y: -50),               
              CGPoint(x: 300, y: 30),               
              CGPoint(x: 400, y: 20)]         
let linearShapeNode = SKShapeNode(points: &points,                                   
                                  count: points.count)          
let splineShapeNode = SKShapeNode(splinePoints: &points,                                   
                                  count: points.count)
```

The following image shows `linearShapeNode` in blue and `splineShapeNode` in red.

![Shape nodes created from points](https://docs-assets.developer.apple.com/published/d8c3df98083749ec51557e7d89d034b5/media-2975239%402x.png)

## See Also

- [convenience init(points: UnsafeMutablePointer<CGPoint>, count: Int)](skshapenode/init(points:count:).md)
  Creates a shape node from a series of points.
- [convenience init(splinePoints: UnsafeMutablePointer<CGPoint>, count: Int)](skshapenode/init(splinepoints:count:).md)
  Creates a shape node from a series of spline points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/creating-a-shape-node-from-an-array-of-points)*