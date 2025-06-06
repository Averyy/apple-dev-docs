# dismissKeyboard()

**Framework**: UIKit  
**Kind**: method

Dismisses the custom keyboard from the screen.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func dismissKeyboard()
```

## Mentions

- [Configuring a custom keyboard interface](configuring-a-custom-keyboard-interface.md)

#### Discussion

Because a custom keyboard does not have access to the current text input object, you cannot send it a [`resignFirstResponder()`](uiresponder/resignfirstresponder().md) message (as you would to dismiss the system keyboard when you are developing an app with text entry). To dismiss the custom keyboard, call [`dismissKeyboard()`](uiinputviewcontroller/dismisskeyboard().md) instead.

## See Also

- [func advanceToNextInputMode()](uiinputviewcontroller/advancetonextinputmode.md)
  Switches to the next keyboard in the list of user-enabled keyboards.
- [func handleInputModeList(from: UIView, with: UIEvent)](uiinputviewcontroller/handleinputmodelist(from:with:).md)
  Supports interaction with the list of user-enabled keyboards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinputviewcontroller/dismisskeyboard())*