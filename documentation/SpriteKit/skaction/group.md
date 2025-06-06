# group(_:)

**Framework**: SpriteKit  
**Kind**: method

Creates an action that runs a collection of actions in parallel.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func group(_ actions: [SKAction]) -> SKAction
```

#### Return Value

A group action object.

#### Discussion

When the action executes, the actions that comprise the group all start immediately and run in parallel. The duration of the group action is the longest duration among the collection of actions. If an action in the group has a duration less than the group’s duration, the action completes, then idles until the group completes the remaining actions. This matters most when creating a repeating action that repeats a group.

This action is reversible; it creates a new group action that contains the reverse of each action specified in the group.

## Parameters

- `actions`: An array of   objects.

## See Also

- [class func sequence([SKAction]) -> SKAction](skaction/sequence(_:).md)
  Creates an action that runs a collection of actions sequentially.
- [class func `repeat`(SKAction, count: Int) -> SKAction](skaction/repeat(_:count:).md)
  Creates an action that repeats another action a specified number of times.
- [class func repeatForever(SKAction) -> SKAction](skaction/repeatforever(_:).md)
  Creates an action that repeats another action forever.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/group(_:))*