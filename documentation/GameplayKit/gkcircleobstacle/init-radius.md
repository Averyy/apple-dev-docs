# init(radius:)

**Framework**: GameplayKit  
**Kind**: init

Initializes a circular obstacle with the specified radius.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(radius: Float)
```

#### Return Value

A circular obstacle.

#### Discussion

To make agents avoid the obstacle, create a goal with the goalToAvoidObstacles:timeBeforeCollisionToAvoid: method.

For more information, see [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Parameters

- `radius`: The radius for the new obstacle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcircleobstacle/init(radius:))*