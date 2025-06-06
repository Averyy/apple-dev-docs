# sequence(_:)

**Framework**: SpriteKit  
**Kind**: method

Creates an action that runs a collection of actions sequentially.

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
class func sequence(_ actions: [SKAction]) -> SKAction
```

#### Return Value

A sequence action object.

#### Discussion

When the action executes, the first action in the sequence starts and runs to completion. Subsequent actions in the sequence run in a similar fashion until all of the actions in the sequence have executed. The duration of the sequence action is the sum of the durations of the actions in the sequence.

This action is reversible; it creates a new sequence action that reverses the order of the actions. Each action in the reversed sequence is itself reversed. For example, if an action sequence is `{1,2,3}`, the reversed sequence would be `{3R,2R,1R}`.

## Parameters

- `actions`: An array of   objects.

## See Also

- [class func group([SKAction]) -> SKAction](skaction/group(_:).md)
  Creates an action that runs a collection of actions in parallel.
- [class func `repeat`(SKAction, count: Int) -> SKAction](skaction/repeat(_:count:).md)
  Creates an action that repeats another action a specified number of times.
- [class func repeatForever(SKAction) -> SKAction](skaction/repeatforever(_:).md)
  Creates an action that repeats another action forever.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/sequence(_:))*