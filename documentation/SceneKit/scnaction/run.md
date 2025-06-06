# run(_:)

**Framework**: SceneKit  
**Kind**: method

Creates an action that executes a block.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func run(_ block: @escaping (SCNNode) -> Void) -> SCNAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, SceneKit calls the block. This action takes place instantaneously.

This action is not reversible; the reverse action executes the same block.

## Parameters

- `block`: The block to run. The block takes a single parameter:

## See Also

- [class func run((SCNNode) -> Void, queue: dispatch_queue_t) -> SCNAction](scnaction/run(_:queue:).md)
  Creates an action that executes a block on a specific dispatch queue.
- [class func customAction(duration: TimeInterval, action: (SCNNode, CGFloat) -> Void) -> SCNAction](scnaction/customaction(duration:action:).md)
  Creates an action that executes a block periodically over a specified duration.
- [class func javaScriptAction(withScript: String, duration: TimeInterval) -> SCNAction](scnaction/javascriptaction(withscript:duration:).md)
  Creates an action that executes a JavaScript script periodically over a specified duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/run(_:))*