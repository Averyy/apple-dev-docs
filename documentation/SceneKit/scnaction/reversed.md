# reversed()

**Framework**: SceneKit  
**Kind**: method

Creates an action that reverses the behavior of another action.

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
func reversed() -> SCNAction
```

#### Return Value

A new action that reverses the action’s behavior.

#### Discussion

This method always returns an action object; however, not all actions are reversible. When reversed, some actions return an object that either does nothing or performs the same action as the original action. For details on how an action is reversed, see the description of the class method used to create that action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/reversed())*