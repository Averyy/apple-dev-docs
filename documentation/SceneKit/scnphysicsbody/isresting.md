# isResting

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the physics body is at rest.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var isResting: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isResting;
```

## Discussion

This property’s default value is [`false`](../../Swift/false.md), but SceneKit’s physics simulation may automatically set it to [`true`](../../Swift/true.md) if the body is not moving and not affected by any forces. A resting body does not participate in the simulation until another body collides with it or you change its position or velocity or apply a force to it.

## See Also

### Defining When a Body Can Move
- [var allowsResting: Bool](./allowsresting.md)
  A Boolean value that specifies whether SceneKit can automatically mark the physics body at rest.
- [func setResting(Bool)](./setresting%28_%29.md)
  Tells SceneKit whether to treat the body as currently being in motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbody/isresting)*