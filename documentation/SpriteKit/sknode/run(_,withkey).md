# run(_:withKey:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Adds an identifiable action to the list of actions executed by the node.

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
func run(_ action: SKAction, withKey key: String)
```

```objc
- (void) runAction:(SKAction *) action withKey:(NSString *) key;
```

## Mentions

- [Controlling Actions Precisely by Using Names](../controlling-actions-precisely-by-using-names.md)

#### Discussion

This method is identical to [`run(_:)`](./run%28_%29.md), but the action is stored so that it can be retrieved later. If an action using the same key is already running, it is removed before the new action is added.

## Parameters

- `action`: The action to perform.
- `key`: A unique key used to identify the action.

## See Also

### Running Actions
- [Getting Started with Actions](../getting-started-with-actions.md)
  Create, configure, and run actions in SpriteKit.
- [func run(SKAction)](./run%28_%29.md)
  Adds an action to the list of actions executed by the node.
- [func run(SKAction, completion: () -> Void)](./run%28_,completion%29.md)
  Adds an action to the list of actions executed by the node and schedules the argument block to be run upon completion of the action.
- [var speed: CGFloat](./speed.md)
  A speed modifier applied to all actions executed by a node and its descendants.
- [var isPaused: Bool](./ispaused.md)
  A Boolean value that determines whether actions on the node and its descendants are processed.
- [func action(forKey: String) -> SKAction?](./action%28forkey%29.md)
  Returns an action associated with a specific key.
- [func hasActions() -> Bool](./hasactions%28%29.md)
  Returns a Boolean value that indicates whether the node is executing actions.
- [func removeAllActions()](./removeallactions%28%29.md)
  Ends and removes all actions from the node.
- [func removeAction(forKey: String)](./removeaction%28forkey%29.md)
  Removes an action associated with a specific key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/run(_:withkey:))*