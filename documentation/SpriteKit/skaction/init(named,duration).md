# init(named:duration:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Creates an action of the given name from an action file with a new duration.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(named name: String, duration: TimeInterval)
```

```objc
+ (SKAction *) actionNamed:(NSString *) name duration:(NSTimeInterval) duration;
```

#### Return Value

A new action object.

## Parameters

- `name`: The name of the action.
- `duration`: The duration of the action.

## See Also

### Creating Custom Actions
- [init?(named: String)](./init%28named%29.md)
  Creates an action of the given name from an action file.
- [init?(named: String, fromURL: URL)](./init%28named,fromurl%29.md)
  Creates an action of the given name from an action file.
- [init?(named: String, fromURL: URL, duration: TimeInterval)](./init%28named,fromurl,duration%29.md)
  Creates an action of the given name from an action file with a new duration.
- [class func customAction(withDuration: TimeInterval, actionBlock: (SKNode, CGFloat) -> Void) -> SKAction](./customaction%28withduration,actionblock%29.md)
  Creates an action that executes a block over a duration.
- [class func perform(Selector, onTarget: Any) -> SKAction](./perform%28_,ontarget%29.md)
  Creates an action that calls a method on an object.
- [class func run(() -> Void) -> SKAction](./run%28_%29.md)
  Creates an action that executes a block.
- [class func run(() -> Void, queue: dispatch_queue_t) -> SKAction](./run%28_,queue%29.md)
  Creates an action that executes a block on a specific dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/init(named:duration:))*