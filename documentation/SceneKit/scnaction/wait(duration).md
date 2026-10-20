# wait(duration:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates an action that idles for a specified period of time.

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
class func wait(duration sec: TimeInterval) -> SCNAction
```

```objc
+ (SCNAction *) waitForDuration:(NSTimeInterval) sec;
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the action waits for the specified amount of time and then ends. This is typically used as part of a sequence of actions to insert a delay between two other actions. You might also use it in conjunction with the [`runAction(_:completionHandler:)`](../scnactionable/runaction%28_,completionhandler%29.md) method to trigger code that needs to run at a later time.

This action is not reversible; the reverse of this action is the same action.

## Parameters

- `sec`: The amount of time to wait.

## See Also

### Creating Actions That Add Delays to Action Sequences
- [class func wait(duration: TimeInterval, withRange: TimeInterval) -> SCNAction](./wait%28duration,withrange%29.md)
  Creates an action that idles for a randomized period of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/wait(duration:))*