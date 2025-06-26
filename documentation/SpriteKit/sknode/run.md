# run(_:)

**Framework**: SpriteKit  
**Kind**: method

Adds an action to the list of actions executed by the node.

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
func run(_ action: SKAction)
```

## Mentions

- [Getting Started with Actions](getting-started-with-actions.md)

#### Discussion

The new action is processed the next time the scene’s animation loop is processed.

## Parameters

- `action`: The action to perform.

## See Also

- [Getting Started with Actions](getting-started-with-actions.md)
  Create, configure, and run actions in SpriteKit.
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
- [func removeAllActions()](sknode/removeallactions.md)
  Ends and removes all actions from the node.
- [func removeAction(forKey: String)](sknode/removeaction(forkey:).md)
  Removes an action associated with a specific key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/run(_:))*