# radius

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

The radius of the obstacle.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var radius: Float { get set }
```

```objc
@property (nonatomic, assign) float radius;
```

## Discussion

The coordinate system for agents and obstacles is arbitrary; you may choose how to map agent and obstacle positions and sizes into your game scene.

## See Also

### Placing an Obstacle
- [var position: vector_float3](./position.md)
  The position of the obstacle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gksphereobstacle/radius)*