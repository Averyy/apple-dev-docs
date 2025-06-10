# javaScriptAction(withScript:duration:)

**Framework**: SceneKit  
**Kind**: method

Creates an action that executes a JavaScript script periodically over a specified duration.

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
class func javaScriptAction(withScript script: String, duration seconds: TimeInterval) -> SCNAction
```

#### Return Value

A new action object.

#### Discussion

SceneKit exposes its classes, methods, and functions in the JavaScript context that runs the script—see the `SCNJavaScript.h` header file for details.

When the action executes, SceneKit runs the script repeatedly until the action’s duration expires. Each time SceneKit runs the script, it computes the elapsed time since the action began executing (as a fraction of the action’s duration between `0.0` and `1.0`) and makes it available to the script as a variable named `elapsedTime`. The script can also reference the [`SCNNode`](scnnode.md) object running the action as a variable named `node`.

This action is not reversible; the reverse action executes the same script.

## Parameters

- `script`: A string containing JavaScript source code.
- `seconds`: The duration of the action, in seconds.

## See Also

- [class func run((SCNNode) -> Void) -> SCNAction](scnaction/run(_:).md)
  Creates an action that executes a block.
- [class func run((SCNNode) -> Void, queue: dispatch_queue_t) -> SCNAction](scnaction/run(_:queue:).md)
  Creates an action that executes a block on a specific dispatch queue.
- [class func customAction(duration: TimeInterval, action: (SCNNode, CGFloat) -> Void) -> SCNAction](scnaction/customaction(duration:action:).md)
  Creates an action that executes a block periodically over a specified duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/javascriptaction(withscript:duration:))*