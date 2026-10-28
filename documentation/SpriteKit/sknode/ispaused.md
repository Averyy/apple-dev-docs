# isPaused

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether actions on the node and its descendants are processed.

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
var isPaused: Bool { get set }
```

```objc
@property (nonatomic, getter=isPaused) BOOL paused;
```

## Discussion

If the value is [`true`](../../Swift/true.md), the node (and all of its descendants) are skipped when a scene processes actions.

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
- [func action(forKey: String) -> SKAction?](./action%28forkey%29.md)
  Returns an action associated with a specific key.
- [func hasActions() -> Bool](./hasactions%28%29.md)
  Returns a Boolean value that indicates whether the node is executing actions.
- [func removeAllActions()](./removeallactions%28%29.md)
  Ends and removes all actions from the node.
- [func removeAction(forKey: String)](./removeaction%28forkey%29.md)
  Removes an action associated with a specific key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/ispaused)*