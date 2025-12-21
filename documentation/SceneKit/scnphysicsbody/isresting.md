# isResting

**Framework**: SceneKit  
**Kind**: property

A Boolean value that indicates whether the physics body is at rest.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var isResting: Bool { get }
```

#### Discussion

This property’s default value is [`false`](https://developer.apple.com/documentation/Swift/false), but SceneKit’s physics simulation may automatically set it to [`true`](https://developer.apple.com/documentation/Swift/true) if the body is not moving and not affected by any forces. A resting body does not participate in the simulation until another body collides with it or you change its position or velocity or apply a force to it.

## See Also

- [var allowsResting: Bool](scnphysicsbody/allowsresting.md)
  A Boolean value that specifies whether SceneKit can automatically mark the physics body at rest.
- [func setResting(Bool)](scnphysicsbody/setresting(_:).md)
  Tells SceneKit whether to treat the body as currently being in motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbody/isresting)*