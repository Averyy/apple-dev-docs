# enumerateBodies(in:using:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Enumerates all the physics bodies in the scene that intersect the specified rectangle.

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
func enumerateBodies(in rect: CGRect, using block: @escaping (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Void)
```

```objc
- (void) enumerateBodiesInRect:(CGRect) rect usingBlock:(void (^)(SKPhysicsBody *body, BOOL *stop)) block;
```

## Parameters

- `rect`: A rectangle in scene coordinates.
- `block`: A block to be called for each physics body that contains the point. The block takes the following parameters:

  - **body**: The physics body that intersected the rectangle.
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
- [func enumerateBodies(alongRayStart: CGPoint, end: CGPoint, using: (SKPhysicsBody, CGPoint, CGVector, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratebodies%28alongraystart,end,using%29.md)
  Enumerates all the physics bodies in the scene that intersect a ray.
- [func enumerateBodies(at: CGPoint, using: (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratebodies%28at,using%29.md)
  Enumerates all the physics bodies in the scene that contain a point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsworld/enumeratebodies(in:using:))*