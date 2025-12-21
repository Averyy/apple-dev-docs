# init(splinePoints:count:)

**Framework**: SpriteKit  
**Kind**: init

Creates a shape node from a series of spline points.

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
convenience init(splinePoints points: UnsafeMutablePointer<CGPoint>, count numPoints: Int)
```

## Mentions

- [Creating a Shape Node from an Array of Points](creating-a-shape-node-from-an-array-of-points.md)

#### Return Value

A new shape node is created. The node is created with a path that starts at the first point in the array, joining each pair of points with a quadratic curve. The control points are calculated automatically based on previous points in the array.

## Parameters

- `points`: An array of Core Graphics points.
- `numPoints`: The number of points in the array.

## See Also

- [Creating a Shape Node from an Array of Points](creating-a-shape-node-from-an-array-of-points.md)
  Create jagged or smooth shapes from the same array of points.
- [convenience init(points: UnsafeMutablePointer<CGPoint>, count: Int)](skshapenode/init(points:count:).md)
  Creates a shape node from a series of points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/init(splinepoints:count:))*