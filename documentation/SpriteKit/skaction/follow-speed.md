# follow(_:speed:)

**Framework**: SpriteKit  
**Kind**: method

Creates an action that moves the node along a relative path at a specified speed, orienting the node to the path.

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
class func follow(_ path: CGPath, speed: CGFloat) -> SKAction
```

#### Return Value

A new action object.

#### Discussion

Calling this method is equivalent to calling the [`follow(_:asOffset:orientToPath:speed:)`](skaction/follow(_:asoffset:orienttopath:speed:).md) method, passing in [`true`](https://developer.apple.com/documentation/Swift/true) to both the `offset` and `orient` parameters.

This action is reversible; the resulting action creates and then follows a reversed path with the same speed.

## Parameters

- `path`: A Core Graphics path whose coordinates are relative to the node’s current position.
- `speed`: The speed at which the node should move, in points per second.

## See Also

- [class func follow(CGPath, duration: TimeInterval) -> SKAction](skaction/follow(_:duration:).md)
  Creates an action that moves the node along a relative path, orienting the node to the path.
- [class func follow(CGPath, asOffset: Bool, orientToPath: Bool, duration: TimeInterval) -> SKAction](skaction/follow(_:asoffset:orienttopath:duration:).md)
  Creates an action that moves the node along a path.
- [class func follow(CGPath, asOffset: Bool, orientToPath: Bool, speed: CGFloat) -> SKAction](skaction/follow(_:asoffset:orienttopath:speed:).md)
  Creates an action that moves the node at a specified speed along a path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/follow(_:speed:))*