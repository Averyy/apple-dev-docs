# obstacleWithRadius:

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Type Method

Creates a circular obstacle with the specified radius.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) obstacleWithRadius:(float) radius;
```

## Return Value

A circular obstacle.

## Discussion

To make agents avoid the obstacle, create a goal with the goalToAvoidObstacles:timeBeforeCollisionToAvoid: method.

## Parameters

- `radius`: The radius for the new obstacle.

## See Also

### Creating an Obstacle
- [init(radius: Float)](./init%28radius%29.md)
  Initializes a circular obstacle with the specified radius.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcircleobstacle/obstaclewithradius:)*