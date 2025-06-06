# handleInputModeList(from:with:)

**Framework**: UIKit  
**Kind**: method

Supports interaction with the list of user-enabled keyboards.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func handleInputModeList(from view: UIView, with event: UIEvent)
```

#### Discussion

Use this method to launch the input mode list from your input view when the user long-presses or swipes up from the view; advance to the next input mode in the list when the user taps the view.

## See Also

- [func advanceToNextInputMode()](uiinputviewcontroller/advancetonextinputmode.md)
  Switches to the next keyboard in the list of user-enabled keyboards.
- [func dismissKeyboard()](uiinputviewcontroller/dismisskeyboard.md)
  Dismisses the custom keyboard from the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinputviewcontroller/handleinputmodelist(from:with:))*