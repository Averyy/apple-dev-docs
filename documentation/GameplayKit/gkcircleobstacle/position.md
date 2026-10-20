# position

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

The position of the obstacle.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var position: vector_float2 { get set }
```

```objc
@property (nonatomic, assign) vector_float2 position;
```

#### Discussion

The coordinate system for agents and obstacles is arbitrary; you may choose how to map agent and obstacle positions and sizes into your game scene.

## See Also

### Placing an Obstacle
- [var radius: Float](./radius.md)
  The radius of the obstacle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcircleobstacle/position)*