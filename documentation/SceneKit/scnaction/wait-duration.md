# wait(duration:)

**Framework**: SceneKit  
**Kind**: method

Creates an action that idles for a specified period of time.

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
class func wait(duration sec: TimeInterval) -> SCNAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the action waits for the specified amount of time and then ends. This is typically used as part of a sequence of actions to insert a delay between two other actions. You might also use it in conjunction with the [`runAction(_:completionHandler:)`](scnactionable/runaction(_:completionhandler:).md) method to trigger code that needs to run at a later time.

This action is not reversible; the reverse of this action is the same action.

## Parameters

- `sec`: The amount of time to wait.

## See Also

- [class func wait(duration: TimeInterval, withRange: TimeInterval) -> SCNAction](scnaction/wait(duration:withrange:).md)
  Creates an action that idles for a randomized period of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/wait(duration:))*