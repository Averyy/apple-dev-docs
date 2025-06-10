# customAction(duration:action:)

**Framework**: SceneKit  
**Kind**: method

Creates an action that executes a block periodically over a specified duration.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class func customAction(duration seconds: TimeInterval, action block: @escaping (SCNNode, CGFloat) -> Void) -> SCNAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, SceneKit calls the block repeatedly until the action’s duration expires. For each call, SceneKit computes the elapsed time and passes it to the block.

This action is not reversible; the reverse action executes the same block.

## Parameters

- `seconds`: The duration of the action, in seconds.
- `block`: The block to run. The block takes the following parameters:

## See Also

- [class func run((SCNNode) -> Void) -> SCNAction](scnaction/run(_:).md)
  Creates an action that executes a block.
- [class func run((SCNNode) -> Void, queue: dispatch_queue_t) -> SCNAction](scnaction/run(_:queue:).md)
  Creates an action that executes a block on a specific dispatch queue.
- [class func javaScriptAction(withScript: String, duration: TimeInterval) -> SCNAction](scnaction/javascriptaction(withscript:duration:).md)
  Creates an action that executes a JavaScript script periodically over a specified duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/customaction(duration:action:))*