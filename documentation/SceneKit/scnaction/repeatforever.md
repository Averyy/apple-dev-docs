# repeatForever(_:)

**Framework**: Scenekit  
**Kind**: method

Creates an action that repeats another action forever.

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
class func repeatForever(_ action: SCNAction) -> SCNAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the associated action runs to completion and then repeats.

This action is reversible; it creates a new action that is the reverse of the specified action and then repeats it forever.

> **Note**:  The action to be repeated must have a non-instantaneous duration.

## Parameters

- `action`: The action to execute.

## See Also

- [class func group([SCNAction]) -> SCNAction](scnaction/group(_:).md)
  Creates an action that runs a collection of actions in parallel.
- [class func sequence([SCNAction]) -> SCNAction](scnaction/sequence(_:).md)
  Creates an action that runs a collection of actions sequentially.
- [class func `repeat`(SCNAction, count: Int) -> SCNAction](scnaction/repeat(_:count:).md)
  Creates an action that repeats another action a specified number of times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/repeatforever(_:))*