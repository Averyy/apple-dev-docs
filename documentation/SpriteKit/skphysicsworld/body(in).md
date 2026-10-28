# body(in:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Searches for the first physics body that intersects the specified rectangle.

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
func body(in rect: CGRect) -> SKPhysicsBody?
```

```objc
- (SKPhysicsBody *) bodyInRect:(CGRect) rect;
```

## Mentions

- [Searching the World for Physics Bodies](../searching-the-world-for-physics-bodies.md)

## Return Value

The first physics body discovered that intersects the rectangle. If no body intersects the rectangle, this method returns `nil`.

## Parameters

- `rect`: A rectangle in scene coordinates.

## See Also

### Searching the Scene for Physics Bodies
- [Searching the World for Physics Bodies](../searching-the-world-for-physics-bodies.md)
  Cast a ray to find the physics bodies in the scene that intersect it.
- [func body(alongRayStart: CGPoint, end: CGPoint) -> SKPhysicsBody?](./body%28alongraystart,end%29.md)
  Searches for the first physics body that intersects a ray.
- [func body(at: CGPoint) -> SKPhysicsBody?](./body%28at%29.md)
  Searches for the first physics body that contains a point.
- [func enumerateBodies(alongRayStart: CGPoint, end: CGPoint, using: (SKPhysicsBody, CGPoint, CGVector, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratebodies%28alongraystart,end,using%29.md)
  Enumerates all the physics bodies in the scene that intersect a ray.
- [func enumerateBodies(at: CGPoint, using: (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratebodies%28at,using%29.md)
  Enumerates all the physics bodies in the scene that contain a point.
- [func enumerateBodies(in: CGRect, using: (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratebodies%28in,using%29.md)
  Enumerates all the physics bodies in the scene that intersect the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsworld/body(in:))*