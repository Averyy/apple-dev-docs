# enumerateBodies(alongRayStart:end:using:)

**Framework**: SpriteKit  
**Kind**: method

Enumerates all the physics bodies in the scene that intersect a ray.

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
func enumerateBodies(alongRayStart start: CGPoint, end: CGPoint, using block: @escaping (SKPhysicsBody, CGPoint, CGVector, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Mentions

- [Searching the World for Physics Bodies](searching-the-world-for-physics-bodies.md)

## Parameters

- `start`: The starting point for the ray in scene coordinates.
- `end`: The ending point for the ray in scene coordinates.
- `block`: A block to be called for each physics body that the ray touches. The block takes the following parameters:

## See Also

- [Searching the World for Physics Bodies](searching-the-world-for-physics-bodies.md)
  Cast a ray to find the physics bodies in the scene that intersect it.
- [func body(alongRayStart: CGPoint, end: CGPoint) -> SKPhysicsBody?](skphysicsworld/body(alongraystart:end:).md)
  Searches for the first physics body that intersects a ray.
- [func body(at: CGPoint) -> SKPhysicsBody?](skphysicsworld/body(at:).md)
  Searches for the first physics body that contains a point.
- [func body(in: CGRect) -> SKPhysicsBody?](skphysicsworld/body(in:).md)
  Searches for the first physics body that intersects the specified rectangle.
- [func enumerateBodies(at: CGPoint, using: (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Void)](skphysicsworld/enumeratebodies(at:using:).md)
  Enumerates all the physics bodies in the scene that contain a point.
- [func enumerateBodies(in: CGRect, using: (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Void)](skphysicsworld/enumeratebodies(in:using:).md)
  Enumerates all the physics bodies in the scene that intersect the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsworld/enumeratebodies(alongraystart:end:using:))*