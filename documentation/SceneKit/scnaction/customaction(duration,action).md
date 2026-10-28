# customAction(duration:action:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates an action that executes a block periodically over a specified duration.

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
class func customAction(duration seconds: TimeInterval, action block: @escaping @Sendable (SCNNode, CGFloat) -> Void) -> SCNAction
```

```objc
+ (SCNAction *) customActionWithDuration:(NSTimeInterval) seconds actionBlock:(void (^)(SCNNode *node, CGFloat elapsedTime)) block;
```

## Return Value

A new action object.

## Discussion

When the action executes, SceneKit calls the block repeatedly until the action’s duration expires. For each call, SceneKit computes the elapsed time and passes it to the block.

This action is not reversible; the reverse action executes the same block.

## Parameters

- `seconds`: The duration of the action, in seconds.
- `block`: The block to run. The block takes the following parameters:

  - ***node***: The node on which the action is running.
  - ***elapsedTime***: The amount of time that has passed since the action began executing.

## See Also

### Creating Custom Actions
- [class func run((SCNNode) -> Void) -> SCNAction](./run%28_%29.md)
  Creates an action that executes a block.
- [class func run((SCNNode) -> Void, queue: dispatch_queue_t) -> SCNAction](./run%28_,queue%29.md)
  Creates an action that executes a block on a specific dispatch queue.
- [class func javaScriptAction(withScript: String, duration: TimeInterval) -> SCNAction](./javascriptaction%28withscript,duration%29.md)
  Creates an action that executes a JavaScript script periodically over a specified duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/customaction(duration:action:))*