# reversed()

**Framework**: SpriteKit  
**Kind**: method

Creates an action that reverses the behavior of another action.

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
func reversed() -> SKAction
```

## Mentions

- [Getting Started with Actions](getting-started-with-actions.md)

#### Return Value

A new action that reverses an action’s behavior.

#### Discussion

This method always returns an action object; however, not all actions are reversible. When reversed, some actions return an object that either does nothing or that performs the same action as the original action. For details on how an action is reversed, see the description of the class method used to create that action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/reversed())*