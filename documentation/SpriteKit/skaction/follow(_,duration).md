# follow(_:duration:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates an action that moves the node along a relative path, orienting the node to the path.

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
class func follow(_ path: CGPath, duration: TimeInterval) -> SKAction
```

```objc
+ (SKAction *) followPath:(CGPathRef) path duration:(NSTimeInterval) duration;
```

#### Return Value

A new action object.

#### Discussion

Calling this method is equivalent to calling the [`follow(_:asOffset:orientToPath:duration:)`](./follow%28_,asoffset,orienttopath,duration%29.md) method, passing in [`true`](../../Swift/true.md) to both the `offset` and `orient` parameters.

This action is reversible; the resulting action creates and then follows a reversed path with the same duration.

## Parameters

- `path`: A Core Graphics path whose coordinates are relative to the node’s current position.
- `duration`: The duration of the animation.

## See Also

### Animating a Node’s Position Along a Custom Path
- [class func follow(CGPath, speed: CGFloat) -> SKAction](./follow%28_,speed%29.md)
  Creates an action that moves the node along a relative path at a specified speed, orienting the node to the path.
- [class func follow(CGPath, asOffset: Bool, orientToPath: Bool, duration: TimeInterval) -> SKAction](./follow%28_,asoffset,orienttopath,duration%29.md)
  Creates an action that moves the node along a path.
- [class func follow(CGPath, asOffset: Bool, orientToPath: Bool, speed: CGFloat) -> SKAction](./follow%28_,asoffset,orienttopath,speed%29.md)
  Creates an action that moves the node at a specified speed along a path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/follow(_:duration:))*