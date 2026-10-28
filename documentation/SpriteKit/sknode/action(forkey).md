# action(forKey:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Returns an action associated with a specific key.

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
func action(forKey key: String) -> SKAction?
```

```objc
- (SKAction *) actionForKey:(NSString *) key;
```

## Mentions

- [Controlling Actions Precisely by Using Names](../controlling-actions-precisely-by-using-names.md)

## Return Value

If an action exists that matches the key, the action object is returned. Otherwise, `nil` is returned.

## Parameters

- `key`: A string that uniquely identifies an action.

## See Also

### Running Actions
- [Getting Started with Actions](../getting-started-with-actions.md)
  Create, configure, and run actions in SpriteKit.
- [func run(SKAction)](./run%28_%29.md)
  Adds an action to the list of actions executed by the node.
- [func run(SKAction, completion: () -> Void)](./run%28_,completion%29.md)
  Adds an action to the list of actions executed by the node and schedules the argument block to be run upon completion of the action.
- [func run(SKAction, withKey: String)](./run%28_,withkey%29.md)
  Adds an identifiable action to the list of actions executed by the node.
- [var speed: CGFloat](./speed.md)
  A speed modifier applied to all actions executed by a node and its descendants.
- [var isPaused: Bool](./ispaused.md)
  A Boolean value that determines whether actions on the node and its descendants are processed.
- [func hasActions() -> Bool](./hasactions%28%29.md)
  Returns a Boolean value that indicates whether the node is executing actions.
- [func removeAllActions()](./removeallactions%28%29.md)
  Ends and removes all actions from the node.
- [func removeAction(forKey: String)](./removeaction%28forkey%29.md)
  Removes an action associated with a specific key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/action(forkey:))*