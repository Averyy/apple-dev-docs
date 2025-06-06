# onKeyPress(keys:phases:action:)

**Framework**: FamilyControls  
**Kind**: method

Performs an action if the user presses one or more keys on a hardware keyboard while the view has focus.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
nonisolated
func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases = [.down, .repeat], action: @escaping (KeyPress) -> KeyPress.Result) -> some View
```

#### Return Value

A modified view that binds keyboard input when focused.

## Parameters

- `keys`: A set of keys to match against incoming hardware   keyboard events.
- `phases`: The key-press phases to match ( ,  , and   ). The default value is  .
- `action`: The action to perform. The action receives a value   describing the matched key event. Return   to consume the   event and prevent further dispatch, or   to allow dispatch   to continue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/onkeypress(keys:phases:action:))*