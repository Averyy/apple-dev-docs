# run(_:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates an action that executes a block.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
class func run(_ block: @escaping @Sendable (SCNNode) -> Void) -> SCNAction
```

```objc
+ (SCNAction *) runBlock:(void (^)(SCNNode *node)) block;
```

## Return Value

A new action object.

## Discussion

When the action executes, SceneKit calls the block. This action takes place instantaneously.

This action is not reversible; the reverse action executes the same block.

## Parameters

- `block`: The block to run. The block takes a single parameter:

  - **node**: The node on which the action is running.

## See Also

### Creating Custom Actions
- [class func run((SCNNode) -> Void, queue: dispatch_queue_t) -> SCNAction](./run%28_,queue%29.md)
  Creates an action that executes a block on a specific dispatch queue.
- [class func customAction(duration: TimeInterval, action: (SCNNode, CGFloat) -> Void) -> SCNAction](./customaction%28duration,action%29.md)
  Creates an action that executes a block periodically over a specified duration.
- [class func javaScriptAction(withScript: String, duration: TimeInterval) -> SCNAction](./javascriptaction%28withscript,duration%29.md)
  Creates an action that executes a JavaScript script periodically over a specified duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/run(_:))*