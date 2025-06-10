# group(_:)

**Framework**: SceneKit  
**Kind**: method

Creates an action that runs a collection of actions in parallel.

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
class func group(_ actions: [SCNAction]) -> SCNAction
```

#### Return Value

A new group action object.

#### Discussion

When the action executes, the actions that make up the group all start immediately and run in parallel. The duration of the group action is the longest duration among the collection of actions. If an action in the group has a duration less than the group’s duration, the action completes and then idles until the group completes the remaining actions. This matters most when creating a repeating action that repeats a group.

This action is reversible; it creates a new group action that contains the reverse of each action specified in the group.

## Parameters

- `actions`: An array of   objects.

## See Also

- [class func sequence([SCNAction]) -> SCNAction](scnaction/sequence(_:).md)
  Creates an action that runs a collection of actions sequentially.
- [class func `repeat`(SCNAction, count: Int) -> SCNAction](scnaction/repeat(_:count:).md)
  Creates an action that repeats another action a specified number of times.
- [class func repeatForever(SCNAction) -> SCNAction](scnaction/repeatforever(_:).md)
  Creates an action that repeats another action forever.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/group(_:))*