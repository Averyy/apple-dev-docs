# shiftKeyStateChanged(fromState:toState:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Indicates a transition in the state of the Shift key.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func shiftKeyStateChanged(fromState oldState: BEKeyModifierFlags, toState newState: BEKeyModifierFlags)
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Discussion

The system invokes this method when a person presses or releases the Shift key, or toggles the Caps Lock key.

## Parameters

- `oldState`: The previous state of the Shift key.
- `newState`: The new state of the Shift key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/shiftkeystatechanged(fromstate:tostate:))*