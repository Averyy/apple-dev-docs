# body(at:)

**Framework**: SpriteKit  
**Kind**: method

Searches for the first physics body that contains a point.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func body(at point: CGPoint) -> SKPhysicsBody?
```

## Mentions

- [Searching the World for Physics Bodies](searching-the-world-for-physics-bodies.md)

#### Return Value

The first physics body discovered that contains the point. If no body contains the point, this method returns `nil`.

## Parameters

- `point`: A point in scene coordinates.

## See Also

- [Searching the World for Physics Bodies](searching-the-world-for-physics-bodies.md)
  Cast a ray to find the physics bodies in the scene that intersect it.
- [func body(alongRayStart: CGPoint, end: CGPoint) -> SKPhysicsBody?](skphysicsworld/body(alongraystart:end:).md)
  Searches for the first physics body that intersects a ray.
- [func body(in: CGRect) -> SKPhysicsBody?](skphysicsworld/body(in:).md)
  Searches for the first physics body that intersects the specified rectangle.
- [func enumerateBodies(alongRayStart: CGPoint, end: CGPoint, using: (SKPhysicsBody, CGPoint, CGVector, UnsafeMutablePointer<ObjCBool>) -> Void)](skphysicsworld/enumeratebodies(alongraystart:end:using:).md)
  Enumerates all the physics bodies in the scene that intersect a ray.
- [func enumerateBodies(at: CGPoint, using: (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Void)](skphysicsworld/enumeratebodies(at:using:).md)
  Enumerates all the physics bodies in the scene that contain a point.
- [func enumerateBodies(in: CGRect, using: (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Void)](skphysicsworld/enumeratebodies(in:using:).md)
  Enumerates all the physics bodies in the scene that intersect the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsworld/body(at:))*