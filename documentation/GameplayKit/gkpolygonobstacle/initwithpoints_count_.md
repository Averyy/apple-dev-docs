# initWithPoints:count:

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Initializes a polygon obstacle with the specified list of vertices.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
- (instancetype) initWithPoints:(vector_float2 *) points count:(size_t) numPoints;
```

#### Return Value

A new polygon obstacle object.

#### Discussion

The coordinate space you define obstacles in, whether used for pathfinding or with agents, is entirely arbitrary. However, it is often convenient to define pathfinding graphs and agent simulations in a coordinate space similar to the one your game uses for display—for example, in a SpriteKit game, define obstacles in the point coordinate system of your scene.

For more information, see [GameplayKit Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Parameters

- `points`: An array of points describing a convex polygon in clockwise order.
- `numPoints`: The number of points in the array.

## See Also

### Creating a Polygon Obstacle
- [+ obstacleWithPoints:count:](./obstaclewithpoints_count_.md)
  Creates a polygon obstacle with the specified list of vertices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkpolygonobstacle/initwithpoints:count:)*