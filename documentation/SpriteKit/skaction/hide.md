# hide()

**Framework**: SpriteKit  
**Kind**: method

Creates an action that hides a node.

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
class func hide() -> SKAction
```

#### Return Value

A new action object.

#### Discussion

This action has an instantaneous duration. When the action executes, the node’s [`isHidden`](sknode/ishidden.md) property is set to [`true`](https://developer.apple.com/documentation/swift/true).

This action is reversible; the reversed action shows the node.

## See Also

- [class func unhide() -> SKAction](skaction/unhide.md)
  Creates an action that makes a node visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/hide())*