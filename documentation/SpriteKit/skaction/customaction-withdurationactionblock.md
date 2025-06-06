# customAction(withDuration:actionBlock:)

**Framework**: SpriteKit  
**Kind**: method

Creates an action that executes a block over a duration.

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
class func customAction(withDuration duration: TimeInterval, actionBlock block: @escaping (SKNode, CGFloat) -> Void) -> SKAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the block is called repeatedly until the action’s duration expires. The elapsed time is computed and passed to the block whenever the block is called.

This action is not reversible; the reverse action executes the same block.

The following Swift code shows how you can create a custom action to update an attribute of an [`SKShader`](skshader.md) attached to a sprite node.

```swift
let customAction = SKAction.customAction(withDuration: 2.0) {
    node, elapsedTime in
    
    if let node = node as? SKSpriteNode {
        node.setValue(SKAttributeValue(float: Float(elapsedTime)),
                                       forAttribute: "a_time")
    }
}
```

## Parameters

- `duration`: The duration of the action, in seconds.
- `block`: The block to run. The block takes the following parameters:

## See Also

- [init?(named: String)](skaction/init(named:).md)
  Creates an action of the given name from an action file.
- [init?(named: String, duration: TimeInterval)](skaction/init(named:duration:).md)
  Creates an action of the given name from an action file with a new duration.
- [init?(named: String, fromURL: URL)](skaction/init(named:fromurl:).md)
  Creates an action of the given name from an action file.
- [init?(named: String, fromURL: URL, duration: TimeInterval)](skaction/init(named:fromurl:duration:).md)
  Creates an action of the given name from an action file with a new duration.
- [class func perform(Selector, onTarget: Any) -> SKAction](skaction/perform(_:ontarget:).md)
  Creates an action that calls a method on an object.
- [class func run(() -> Void) -> SKAction](skaction/run(_:).md)
  Creates an action that executes a block.
- [class func run(() -> Void, queue: dispatch_queue_t) -> SKAction](skaction/run(_:queue:).md)
  Creates an action that executes a block on a specific dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/customaction(withduration:actionblock:))*