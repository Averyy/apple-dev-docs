# wait(forDuration:)

**Framework**: SpriteKit  
**Kind**: method

Creates an action that idles for a specified period of time.

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
class func wait(forDuration duration: TimeInterval) -> SKAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the action waits for the specified amount of time, then ends. This is typically used as part of a sequence of actions to insert a delay between two other actions. You might also use it in conjunction with the [`run(_:completion:)`](sknode/run(_:completion:).md) method to trigger code that needs to run at a later time.

This action is not reversible; the reverse of this action is the same action.

## Parameters

- `duration`: The amount of time to wait.

## See Also

- [class func wait(forDuration: TimeInterval, withRange: TimeInterval) -> SKAction](skaction/wait(forduration:withrange:).md)
  Creates an action that idles for a randomized period of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/wait(forduration:))*