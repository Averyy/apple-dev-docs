# setResting(_:)

**Framework**: SceneKit  
**Kind**: method

Tells SceneKit whether to treat the body as currently being in motion.

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
func setResting(_ resting: Bool)
```

#### Discussion

When a body is at rest, SceneKit assumes that the body will not move unless another body collides with it, you change the body’s position or velocity directly, or you apply a force to the body. Resting bodies don’t participate in the physics simulation, reducing the performance cost of physics calculations and ensuring that those bodies don’t move unexpectedly.

By default, SceneKit automatically determines whether to treat a body as resting (see [`isResting`](scnphysicsbody/isresting.md) and [`allowsResting`](scnphysicsbody/allowsresting.md)). Use this method only if you need to override this behavior. For example, you might set a body to resting if you change its position to reflect an external influence, and don’t want the physics simulation to make the body appear to settle into place after the move.

## Parameters

- `resting`: A Boolean value indicating whether to treat the body as at rest.

## See Also

- [var isResting: Bool](scnphysicsbody/isresting.md)
  A Boolean value that indicates whether the physics body is at rest.
- [var allowsResting: Bool](scnphysicsbody/allowsresting.md)
  A Boolean value that specifies whether SceneKit can automatically mark the physics body at rest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbody/setresting(_:))*