# perform(_:onTarget:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates an action that calls a method on an object.

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
class func perform(_ selector: Selector, onTarget target: Any) -> SKAction
```

```objc
+ (SKAction *) performSelector:(SEL) selector onTarget:(id) target;
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
- [class func run(() -> Void) -> SKAction](./run%28_%29.md)
  Creates an action that executes a block.
- [class func run(() -> Void, queue: dispatch_queue_t) -> SKAction](./run%28_,queue%29.md)
  Creates an action that executes a block on a specific dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/perform(_:ontarget:))*