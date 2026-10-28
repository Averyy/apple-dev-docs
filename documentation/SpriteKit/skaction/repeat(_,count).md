# repeat(_:count:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates an action that repeats another action a specified number of times.

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
class func `repeat`(_ action: SKAction, count: Int) -> SKAction
```

```objc
+ (SKAction *) repeatAction:(SKAction *) action count:(NSUInteger) count;
```

## Return Value

A new action object.

## Discussion

When the action executes, the associated action runs to completion and then repeats, until the count is reached.

This action is reversible; it creates a new action that is the reverse of the specified action and then repeats it the same number of times.

## Parameters

- `action`: The action to execute.
- `count`: The number of times to execute the action.

## See Also

### Chaining Actions
- [class func group([SKAction]) -> SKAction](./group%28_%29.md)
  Creates an action that runs a collection of actions in parallel.
- [class func sequence([SKAction]) -> SKAction](./sequence%28_%29.md)
  Creates an action that runs a collection of actions sequentially.
- [class func repeatForever(SKAction) -> SKAction](./repeatforever%28_%29.md)
  Creates an action that repeats another action forever.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/repeat(_:count:))*