# run(_:completion:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Adds an action to the list of actions executed by the node and schedules the argument block to be run upon completion of the action.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

*iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS*

```swift
func run(_ action: SKAction, completion block: @escaping () -> Void)
```

*iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS*

```swift
func run(_ action: SKAction) async
```

*watchOS*

```swift
func run(_ action: SKAction, completion block: @escaping @Sendable () -> Void)
```

```objc
- (void) runAction:(SKAction *) action completion:(void (^)()) block;
```

## Mentions

- [Getting Started with Actions](../getting-started-with-actions.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func run(_ action: SKAction) async
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `action`: The action to perform.
- `block`: A completion block called when the action completes.

## See Also

### Running Actions
- [Getting Started with Actions](../getting-started-with-actions.md)
  Create, configure, and run actions in SpriteKit.
- [func run(SKAction)](./run%28_%29.md)
  Adds an action to the list of actions executed by the node.
- [func run(SKAction, withKey: String)](./run%28_,withkey%29.md)
  Adds an identifiable action to the list of actions executed by the node.
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

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/run(_:completion:))*