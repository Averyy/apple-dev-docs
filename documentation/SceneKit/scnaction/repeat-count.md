# repeat(_:count:)

**Framework**: SceneKit  
**Kind**: method

Creates an action that repeats another action a specified number of times.

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
class func `repeat`(_ action: SCNAction, count: Int) -> SCNAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the associated action runs to completion and then repeats, until the count is reached.

This action is reversible; it creates a new action that is the reverse of the specified action and then repeats it the same number of times.

## Parameters

- `action`: The action to be executed.
- `count`: The number of times to execute the action.

## See Also

- [class func group([SCNAction]) -> SCNAction](scnaction/group(_:).md)
  Creates an action that runs a collection of actions in parallel.
- [class func sequence([SCNAction]) -> SCNAction](scnaction/sequence(_:).md)
  Creates an action that runs a collection of actions sequentially.
- [class func repeatForever(SCNAction) -> SCNAction](scnaction/repeatforever(_:).md)
  Creates an action that repeats another action forever.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/repeat(_:count:))*