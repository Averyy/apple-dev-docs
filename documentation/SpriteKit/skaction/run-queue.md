# run(_:queue:)

**Framework**: SpriteKit  
**Kind**: method

Creates an action that executes a block on a specific dispatch queue.

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
class func run(_ block: @escaping () -> Void, queue: dispatch_queue_t) -> SKAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the block is called. This action takes place instantaneously.

This action is not reversible; the reverse action executes the same block.

## Parameters

- `block`: The block to run.
- `queue`: The queue to perform the action on.

## See Also

- [init?(named: String)](skaction/init(named:).md)
  Creates an action of the given name from an action file.
- [init?(named: String, duration: TimeInterval)](skaction/init(named:duration:).md)
  Creates an action of the given name from an action file with a new duration.
- [init?(named: String, fromURL: URL)](skaction/init(named:fromurl:).md)
  Creates an action of the given name from an action file.
- [init?(named: String, fromURL: URL, duration: TimeInterval)](skaction/init(named:fromurl:duration:).md)
  Creates an action of the given name from an action file with a new duration.
- [class func customAction(withDuration: TimeInterval, actionBlock: (SKNode, CGFloat) -> Void) -> SKAction](skaction/customaction(withduration:actionblock:).md)
  Creates an action that executes a block over a duration.
- [class func perform(Selector, onTarget: Any) -> SKAction](skaction/perform(_:ontarget:).md)
  Creates an action that calls a method on an object.
- [class func run(() -> Void) -> SKAction](skaction/run(_:).md)
  Creates an action that executes a block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/run(_:queue:))*