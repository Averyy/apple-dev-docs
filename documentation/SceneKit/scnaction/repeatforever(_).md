# repeatForever(_:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates an action that repeats another action forever.

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
class func repeatForever(_ action: SCNAction) -> SCNAction
```

```objc
+ (SCNAction *) repeatActionForever:(SCNAction *) action;
```

## Return Value

A new action object.

## Discussion

When the action executes, the associated action runs to completion and then repeats.

This action is reversible; it creates a new action that is the reverse of the specified action and then repeats it forever.

> **Note**:  The action to be repeated must have a non-instantaneous duration.

## Parameters

- `action`: The action to execute.

## See Also

### Creating Actions That Combine or Repeat Other Actions
- [class func group([SCNAction]) -> SCNAction](./group%28_%29.md)
  Creates an action that runs a collection of actions in parallel.
- [class func sequence([SCNAction]) -> SCNAction](./sequence%28_%29.md)
  Creates an action that runs a collection of actions sequentially.
- [class func `repeat`(SCNAction, count: Int) -> SCNAction](./repeat%28_,count%29.md)
  Creates an action that repeats another action a specified number of times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/repeatforever(_:))*