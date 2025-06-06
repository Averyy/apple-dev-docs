# run(_:withKey:)

**Framework**: SpriteKit  
**Kind**: method

Adds an identifiable action to the list of actions executed by the node.

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
func run(_ action: SKAction, withKey key: String)
```

## Mentions

- [Controlling Actions Precisely by Using Names](controlling-actions-precisely-by-using-names.md)

#### Discussion

This method is identical to [`run(_:)`](sknode/run(_:).md), but the action is stored so that it can be retrieved later. If an action using the same key is already running, it is removed before the new action is added.

## Parameters

- `action`: The action to perform.
- `key`: A unique key used to identify the action.

## See Also

- [Getting Started with Actions](getting-started-with-actions.md)
  Create, configure, and run actions in SpriteKit.
- [func run(SKAction)](sknode/run(_:).md)
  Adds an action to the list of actions executed by the node.
- [func run(SKAction, completion: () -> Void)](sknode/run(_:completion:).md)
  Adds an action to the list of actions executed by the node and schedules the argument block to be run upon completion of the action.
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

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/run(_:withkey:))*