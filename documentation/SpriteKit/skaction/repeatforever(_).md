# repeatForever(_:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates an action that repeats another action forever.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class func repeatForever(_ action: SKAction) -> SKAction
```

```objc
+ (SKAction *) repeatActionForever:(SKAction *) action;
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

### Chaining Actions
- [class func group([SKAction]) -> SKAction](./group%28_%29.md)
  Creates an action that runs a collection of actions in parallel.
- [class func sequence([SKAction]) -> SKAction](./sequence%28_%29.md)
  Creates an action that runs a collection of actions sequentially.
- [class func `repeat`(SKAction, count: Int) -> SKAction](./repeat%28_,count%29.md)
  Creates an action that repeats another action a specified number of times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/repeatforever(_:))*