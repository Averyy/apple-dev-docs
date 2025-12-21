# isPaused

**Framework**: SpriteKit  
**Kind**: property

A Boolean value that determines whether actions on the node and its descendants are processed.

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
var isPaused: Bool { get set }
```

#### Discussion

If the value is [`true`](https://developer.apple.com/documentation/Swift/true), the node (and all of its descendants) are skipped when a scene processes actions.

## See Also

- [Getting Started with Actions](getting-started-with-actions.md)
  Create, configure, and run actions in SpriteKit.
- [func run(SKAction)](sknode/run(_:).md)
  Adds an action to the list of actions executed by the node.
- [func run(SKAction, completion: () -> Void)](sknode/run(_:completion:).md)
  Adds an action to the list of actions executed by the node and schedules the argument block to be run upon completion of the action.
- [func run(SKAction, withKey: String)](sknode/run(_:withkey:).md)
  Adds an identifiable action to the list of actions executed by the node.
- [var speed: CGFloat](sknode/speed.md)
  A speed modifier applied to all actions executed by a node and its descendants.
- [func action(forKey: String) -> SKAction?](sknode/action(forkey:).md)
  Returns an action associated with a specific key.
- [func hasActions() -> Bool](sknode/hasactions.md)
  Returns a Boolean value that indicates whether the node is executing actions.
- [func removeAllActions()](sknode/removeallactions.md)
  Ends and removes all actions from the node.
- [func removeAction(forKey: String)](sknode/removeaction(forkey:).md)
  Removes an action associated with a specific key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/ispaused)*