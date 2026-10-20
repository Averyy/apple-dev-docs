# follow(_:asOffset:orientToPath:duration:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates an action that moves the node along a path.

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
class func follow(_ path: CGPath, asOffset offset: Bool, orientToPath orient: Bool, duration: TimeInterval) -> SKAction
```

```objc
+ (SKAction *) followPath:(CGPathRef) path asOffset:(BOOL) offset orientToPath:(BOOL) orient duration:(NSTimeInterval) duration;
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`position`](../sknode/position.md) and [`zRotation`](../sknode/zrotation.md) properties are animated along the provided path.

This action is reversible; the resulting action creates a reversed path and then follows it, with the same duration.

## Parameters

- `path`: A path to follow.
- `offset`: If [`true`](../../Swift/true.md), the points in the path are relative offsets to the node’s starting position. If [`false`](../../Swift/false.md), the points in the node are absolute coordinate values.
- `orient`: If [`true`](../../Swift/true.md), the node’s [`zRotation`](../sknode/zrotation.md) property animates so that the node turns to follow the path. If [`false`](../../Swift/false.md), the [`zRotation`](../sknode/zrotation.md) property of the node is unchanged.
- `duration`: The duration of the animation.

## See Also

### Animating a Node’s Position Along a Custom Path
- [class func follow(CGPath, duration: TimeInterval) -> SKAction](./follow%28_,duration%29.md)
  Creates an action that moves the node along a relative path, orienting the node to the path.
- [class func follow(CGPath, speed: CGFloat) -> SKAction](./follow%28_,speed%29.md)
  Creates an action that moves the node along a relative path at a specified speed, orienting the node to the path.
- [class func follow(CGPath, asOffset: Bool, orientToPath: Bool, speed: CGFloat) -> SKAction](./follow%28_,asoffset,orienttopath,speed%29.md)
  Creates an action that moves the node at a specified speed along a path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/follow(_:asoffset:orienttopath:duration:))*