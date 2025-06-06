# onKeyPress(_:action:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Performs an action if the user presses a key on a hardware keyboard while the view has focus.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
nonisolated
func onKeyPress(_ key: KeyEquivalent, action: @escaping () -> KeyPress.Result) -> some View
```

#### Return Value

A modified view that binds hardware keyboard input when focused.

#### Discussion

SwiftUI performs the action for key-down and key-repeat events.

## Parameters

- `key`: The key to match against incoming hardware keyboard events.
- `action`: The action to perform. Return   to consume the   event and prevent further dispatch, or   to allow dispatch   to continue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedcontentview/onkeypress(_:action:))*