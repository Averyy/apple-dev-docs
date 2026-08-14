# unhide()

**Framework**: SpriteKit  
**Kind**: method

Creates an action that makes a node visible.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class func unhide() -> SKAction
```

#### Return Value

A new action object.

#### Discussion

This action has an instantaneous duration. When the action executes, the node’s [`isHidden`](sknode/ishidden.md) property is set to [`false`](https://developer.apple.com/documentation/swift/false).

This action is reversible; the reversed action hides the node.

## See Also

- [class func hide() -> SKAction](skaction/hide.md)
  Creates an action that hides a node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/unhide())*