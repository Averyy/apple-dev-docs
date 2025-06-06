# enumerateBodies(in:using:)

**Framework**: SpriteKit  
**Kind**: method

Enumerates all the physics bodies in the scene that intersect the specified rectangle.

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
func enumerateBodies(in rect: CGRect, using block: @escaping (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Parameters

- `rect`: A rectangle in scene coordinates.
- `block`: A block to be called for each physics body that contains the point. The block takes the following parameters:

## See Also

- [Searching the World for Physics Bodies](searching-the-world-for-physics-bodies.md)
  Cast a ray to find the physics bodies in the scene that intersect it.
- [func body(alongRayStart: CGPoint, end: CGPoint) -> SKPhysicsBody?](skphysicsworld/body(alongraystart:end:).md)
  Searches for the first physics body that intersects a ray.
- [func body(at: CGPoint) -> SKPhysicsBody?](skphysicsworld/body(at:).md)
  Searches for the first physics body that contains a point.
- [func body(in: CGRect) -> SKPhysicsBody?](skphysicsworld/body(in:).md)
  Searches for the first physics body that intersects the specified rectangle.
- [func enumerateBodies(alongRayStart: CGPoint, end: CGPoint, using: (SKPhysicsBody, CGPoint, CGVector, UnsafeMutablePointer<ObjCBool>) -> Void)](skphysicsworld/enumeratebodies(alongraystart:end:using:).md)
  Enumerates all the physics bodies in the scene that intersect a ray.
- [func enumerateBodies(at: CGPoint, using: (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Void)](skphysicsworld/enumeratebodies(at:using:).md)
  Enumerates all the physics bodies in the scene that contain a point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsworld/enumeratebodies(in:using:))*