# enumerateBodies(alongRayStart:end:using:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Enumerates all the physics bodies in the scene that intersect a ray.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func enumerateBodies(alongRayStart start: CGPoint, end: CGPoint, using block: @escaping (SKPhysicsBody, CGPoint, CGVector, UnsafeMutablePointer<ObjCBool>) -> Void)
```

```objc
- (void) enumerateBodiesAlongRayStart:(CGPoint) start end:(CGPoint) end usingBlock:(void (^)(SKPhysicsBody *body, CGPoint point, CGVector normal, BOOL *stop)) block;
```

## Mentions

- [Searching the World for Physics Bodies](../searching-the-world-for-physics-bodies.md)

## Parameters

- `start`: The starting point for the ray in scene coordinates.
- `end`: The ending point for the ray in scene coordinates.
- `block`: A block to be called for each physics body that the ray touches. The block takes the following parameters:

  - **body**: The physics body that the ray intersected.
  - **point**: The point in scene coordinates where the ray contacted the physics body.
  - **normal**: The normal vector for the physics body at the point of contact.
  - **stop**: A pointer to a Boolean variable. Your block can set this to [`true`](../../Swift/true.md) to terminate the enumeration.

## See Also

### Searching the Scene for Physics Bodies
- [Searching the World for Physics Bodies](../searching-the-world-for-physics-bodies.md)
  Cast a ray to find the physics bodies in the scene that intersect it.
- [func body(alongRayStart: CGPoint, end: CGPoint) -> SKPhysicsBody?](./body%28alongraystart,end%29.md)
  Searches for the first physics body that intersects a ray.
- [func body(at: CGPoint) -> SKPhysicsBody?](./body%28at%29.md)
  Searches for the first physics body that contains a point.
- [func body(in: CGRect) -> SKPhysicsBody?](./body%28in%29.md)
  Searches for the first physics body that intersects the specified rectangle.
- [func enumerateBodies(at: CGPoint, using: (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratebodies%28at,using%29.md)
  Enumerates all the physics bodies in the scene that contain a point.
- [func enumerateBodies(in: CGRect, using: (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratebodies%28in,using%29.md)
  Enumerates all the physics bodies in the scene that intersect the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsworld/enumeratebodies(alongraystart:end:using:))*