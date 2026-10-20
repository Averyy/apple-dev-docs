# run(_:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates an action that executes a block.

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
class func run(_ block: @escaping () -> Void) -> SKAction
```

```objc
+ (SKAction *) runBlock:(dispatch_block_t) block;
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the block is called. This action takes place instantaneously.

This action is not reversible; the reverse action executes the same block.

## Parameters

- `block`: The block to run.

## See Also

### Creating Custom Actions
- [init?(named: String)](./init%28named%29.md)
  Creates an action of the given name from an action file.
- [init?(named: String, duration: TimeInterval)](./init%28named,duration%29.md)
  Creates an action of the given name from an action file with a new duration.
- [init?(named: String, fromURL: URL)](./init%28named,fromurl%29.md)
  Creates an action of the given name from an action file.
- [init?(named: String, fromURL: URL, duration: TimeInterval)](./init%28named,fromurl,duration%29.md)
  Creates an action of the given name from an action file with a new duration.
- [class func customAction(withDuration: TimeInterval, actionBlock: (SKNode, CGFloat) -> Void) -> SKAction](./customaction%28withduration,actionblock%29.md)
  Creates an action that executes a block over a duration.
- [class func perform(Selector, onTarget: Any) -> SKAction](./perform%28_,ontarget%29.md)
  Creates an action that calls a method on an object.
- [class func run(() -> Void, queue: dispatch_queue_t) -> SKAction](./run%28_,queue%29.md)
  Creates an action that executes a block on a specific dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/run(_:))*