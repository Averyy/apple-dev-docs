# init(points:count:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Creates a shape node from a series of points.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
convenience init(points: UnsafeMutablePointer<CGPoint>, count numPoints: Int)
```

```objc
+ (instancetype) shapeNodeWithPoints:(CGPoint *) points count:(size_t) numPoints;
```

## Mentions

- [Creating a Shape Node from an Array of Points](../creating-a-shape-node-from-an-array-of-points.md)

#### Return Value

A new shape node. The node is created with a path that starts at the first point in the array, joining each adjacent pair of points with a line segment.

## Parameters

- `points`: An array of Core Graphics points. The points are relative to the node’s origin.
- `numPoints`: The number of points in the array.

## See Also

### Creating a Shape from an Array of Points
- [Creating a Shape Node from an Array of Points](../creating-a-shape-node-from-an-array-of-points.md)
  Create jagged or smooth shapes from the same array of points.
- [convenience init(splinePoints: UnsafeMutablePointer<CGPoint>, count: Int)](./init%28splinepoints,count%29.md)
  Creates a shape node from a series of spline points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/init(points:count:))*