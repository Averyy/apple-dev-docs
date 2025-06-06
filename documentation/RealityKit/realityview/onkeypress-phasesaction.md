# onKeyPress(phases:action:)

**Framework**: RealityKit  
**Kind**: method

Performs an action if the user presses any key on a hardware keyboard while the view has focus.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
nonisolated
func onKeyPress(phases: KeyPress.Phases = [.down, .repeat], action: @escaping (KeyPress) -> KeyPress.Result) -> some View
```

#### Return Value

A modified view that binds hardware keyboard input when focused.

## Parameters

- `phases`: The key-press phases to match ( ,  , and   ). The default value is  .
- `action`: The action to perform. The action receives a value   describing the matched key event. Return   to consume the   event and prevent further dispatch, or   to allow dispatch   to continue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/onkeypress(phases:action:))*