# removeAction(forKey:)

**Framework**: SpriteKit  
**Kind**: method

Removes an action associated with a specific key.

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
@MainActor
func removeAction(forKey key: String)
```

## Mentions

- [Controlling Actions Precisely by Using Names](controlling-actions-precisely-by-using-names.md)

#### Discussion

If an action is found that matches the key, it is removed from the node.

## Parameters

- `key`: A string that uniquely identifies an action.

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
- [func removeAllActions()](sknode/removeallactions.md)
  Ends and removes all actions from the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/removeaction(forkey:))*