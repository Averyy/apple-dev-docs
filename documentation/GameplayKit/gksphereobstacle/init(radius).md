# init(radius:)

**Framework**: GameplayKit  
**Kind**: init  
**Role**: Initializer

Initializes a spherical obstacle with the specified radius.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(radius: Float)
```

```objc
- (instancetype) initWithRadius:(float) radius;
```

## Return Value

A spherical obstacle.

## Discussion

To make agents avoid the obstacle, create a goal with the goalToAvoidObstacles:timeBeforeCollisionToAvoid: method.

## Parameters

- `radius`: The radius for the new obstacle.

## See Also

### Creating an Obstacle
- [+ obstacleWithRadius:](./obstaclewithradius_.md)
  Creates a spherical obstacle with the specified radius.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gksphereobstacle/init(radius:))*