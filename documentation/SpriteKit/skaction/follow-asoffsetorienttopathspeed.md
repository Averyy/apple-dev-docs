# follow(_:asOffset:orientToPath:speed:)

**Framework**: SpriteKit  
**Kind**: method

Creates an action that moves the node at a specified speed along a path.

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
class func follow(_ path: CGPath, asOffset offset: Bool, orientToPath orient: Bool, speed: CGFloat) -> SKAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`position`](sknode/position.md) and [`zRotation`](sknode/zrotation.md) properties are animated along the provided path. The duration of the action is determined by the length of the path and the speed of the node.

This action is reversible; the resulting action creates a reversed path and then follows it, with the same speed.

## Parameters

- `path`: A path to follow.
- `offset`: If  , the points in the path are relative offsets to the node’s starting position. If  , the points in the node are absolute coordinate values.
- `orient`: If  , the node’s   property animates so that the node turns to follow the path. If  , the   property of the node is unchanged.
- `speed`: The speed at which the node should move, in points per second.

## See Also

- [class func follow(CGPath, duration: TimeInterval) -> SKAction](skaction/follow(_:duration:).md)
  Creates an action that moves the node along a relative path, orienting the node to the path.
- [class func follow(CGPath, speed: CGFloat) -> SKAction](skaction/follow(_:speed:).md)
  Creates an action that moves the node along a relative path at a specified speed, orienting the node to the path.
- [class func follow(CGPath, asOffset: Bool, orientToPath: Bool, duration: TimeInterval) -> SKAction](skaction/follow(_:asoffset:orienttopath:duration:).md)
  Creates an action that moves the node along a path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/follow(_:asoffset:orienttopath:speed:))*