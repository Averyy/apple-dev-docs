# init(named:fromURL:duration:)

**Framework**: SpriteKit  
**Kind**: init

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
init?(named name: String, from url: URL, duration: TimeInterval)
```

#### Return Value

A new action object.

## Parameters

- `name`: The name of the action.
- `url`: The URL of the file containing the action.
- `duration`: The duration of the action, in seconds.

## See Also

- [init?(named: String)](skaction/init(named:).md)
  Creates an action of the given name from an action file.
- [init?(named: String, duration: TimeInterval)](skaction/init(named:duration:).md)
  Creates an action of the given name from an action file with a new duration.
- [init?(named: String, fromURL: URL)](skaction/init(named:fromurl:).md)
  Creates an action of the given name from an action file.
- [class func customAction(withDuration: TimeInterval, actionBlock: (SKNode, CGFloat) -> Void) -> SKAction](skaction/customaction(withduration:actionblock:).md)
  Creates an action that executes a block over a duration.
- [class func perform(Selector, onTarget: Any) -> SKAction](skaction/perform(_:ontarget:).md)
  Creates an action that calls a method on an object.
- [class func run(() -> Void) -> SKAction](skaction/run(_:).md)
  Creates an action that executes a block.
- [class func run(() -> Void, queue: dispatch_queue_t) -> SKAction](skaction/run(_:queue:).md)
  Creates an action that executes a block on a specific dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/init(named:fromurl:duration:))*