# allowsResting

**Framework**: SceneKit  
**Kind**: property

A Boolean value that specifies whether SceneKit can automatically mark the physics body at rest.

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
var allowsResting: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true) (the default), SceneKit keeps track of whether the body is moving or affected by forces, automatically setting its [`isResting`](scnphysicsbody/isresting.md) property to [`true`](https://developer.apple.com/documentation/Swift/true) when it is “at rest.” The physics simulation runs faster when simulating fewer bodies, so treating a body as resting temporarily removes it from the simulation to improve performance.

SceneKit automatically returns a resting body to the simulation if another body collides with it, if you change its position or velocity, or if you apply a force to it. However, SceneKit uses a faster, less accurate simulation when deciding whether to change a body’s [`isResting`](scnphysicsbody/isresting.md) property back to [`false`](https://developer.apple.com/documentation/Swift/false). If testing your app reveals unexpected physics behaviors involving resting bodies, changing those bodies’ allowsResting property to [`false`](https://developer.apple.com/documentation/Swift/false) may improve simulation accuracy.

## See Also

- [var isResting: Bool](scnphysicsbody/isresting.md)
  A Boolean value that indicates whether the physics body is at rest.
- [func setResting(Bool)](scnphysicsbody/setresting(_:).md)
  Tells SceneKit whether to treat the body as currently being in motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbody/allowsresting)*