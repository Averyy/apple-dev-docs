# group(_:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates an action that runs a collection of actions in parallel.

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
class func group(_ actions: [SCNAction]) -> SCNAction
```

```objc
+ (SCNAction *) group:(NSArray<SCNAction *> *) actions;
```

#### Return Value

A new group action object.

#### Discussion

When the action executes, the actions that make up the group all start immediately and run in parallel. The duration of the group action is the longest duration among the collection of actions. If an action in the group has a duration less than the group’s duration, the action completes and then idles until the group completes the remaining actions. This matters most when creating a repeating action that repeats a group.

This action is reversible; it creates a new group action that contains the reverse of each action specified in the group.

## Parameters

- `actions`: An array of [`SCNAction`](../scnaction.md) objects.

## See Also

### Creating Actions That Combine or Repeat Other Actions
- [class func sequence([SCNAction]) -> SCNAction](./sequence%28_%29.md)
  Creates an action that runs a collection of actions sequentially.
- [class func `repeat`(SCNAction, count: Int) -> SCNAction](./repeat%28_,count%29.md)
  Creates an action that repeats another action a specified number of times.
- [class func repeatForever(SCNAction) -> SCNAction](./repeatforever%28_%29.md)
  Creates an action that repeats another action forever.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/group(_:))*