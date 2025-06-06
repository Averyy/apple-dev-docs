# perform(_:onTarget:)

**Framework**: SpriteKit  
**Kind**: method

Creates an action that calls a method on an object.

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
class func perform(_ selector: Selector, onTarget target: Any) -> SKAction
```

#### Return Value

A new action object.

#### Discussion

The action object maintains a strong reference to the target object.

When the action executes, the target object’s method is called. This action occurs instantaneously.

This action is not reversible; the reverse of this action calls the selector again.

## Parameters

- `selector`: The selector of the method to call.
- `target`: The target object.

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
- [class func run(() -> Void) -> SKAction](skaction/run(_:).md)
  Creates an action that executes a block.
- [class func run(() -> Void, queue: dispatch_queue_t) -> SKAction](skaction/run(_:queue:).md)
  Creates an action that executes a block on a specific dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/perform(_:ontarget:))*