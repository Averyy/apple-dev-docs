# wait(forDuration:withRange:)

**Framework**: SpriteKit  
**Kind**: method

Creates an action that idles for a randomized period of time.

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
class func wait(forDuration duration: TimeInterval, withRange durationRange: TimeInterval) -> SKAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the action waits for the specified amount of time, then ends. This is typically used as part of a sequence of actions to insert a delay between two other actions. However, you might also use it in conjunction with the [`run(_:completion:)`](sknode/run(_:completion:).md) method to trigger code that needs to run at a later time.

Each time the action is executed, the action computes a new random value for the duration. The duration may vary in either direction by up to half of the value of the `durationRange` parameter.

This action is not reversible; the reverse of this action is the same action.

## Parameters

- `duration`: The average amount of time to wait.
- `durationRange`: The range of possible values for the duration.

## See Also

- [class func wait(forDuration: TimeInterval) -> SKAction](skaction/wait(forduration:).md)
  Creates an action that idles for a specified period of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/wait(forduration:withrange:))*