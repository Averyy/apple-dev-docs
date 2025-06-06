# removeAllActions()

**Framework**: SpriteKit  
**Kind**: method

Ends and removes all actions from the node.

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
func removeAllActions()
```

## Mentions

- [Configuring Action Timing](configuring-action-timing.md)

#### Discussion

When an action is removed from the node, any remaining animation the action would perform is skipped; however, previous changes are not reverted. It is possible that an action may make a final change to the scene when removed; if so, it is documented for the specific action in [`SKAction`](skaction.md).

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
- [var isPaused: Bool](sknode/ispaused.md)
  A Boolean value that determines whether actions on the node and its descendants are processed.
- [func action(forKey: String) -> SKAction?](sknode/action(forkey:).md)
  Returns an action associated with a specific key.
- [func hasActions() -> Bool](sknode/hasactions.md)
  Returns a Boolean value that indicates whether the node is executing actions.
- [func removeAction(forKey: String)](sknode/removeaction(forkey:).md)
  Removes an action associated with a specific key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/removeallactions())*