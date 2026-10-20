# advanceToNextInputMode()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Switches to the next keyboard in the list of user-enabled keyboards.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func advanceToNextInputMode()
```

```objc
- (void) advanceToNextInputMode;
```

#### Discussion

When the user taps the Globe or a custom “next keyboard” key, the system picks the appropriate “next” keyboard from the list of user-enabled keyboards. To determine whether your custom keyboard needs to display a “next keyboard” key, check the [`needsInputModeSwitchKey`](./needsinputmodeswitchkey.md) property. If the value of the property is [`true`](../../Swift/true.md), your keyboard should include this key.

## See Also

### Controlling a custom keyboard
- [func dismissKeyboard()](./dismisskeyboard%28%29.md)
  Dismisses the custom keyboard from the screen.
- [func handleInputModeList(from: UIView, with: UIEvent)](./handleinputmodelist%28from,with%29.md)
  Supports interaction with the list of user-enabled keyboards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinputviewcontroller/advancetonextinputmode())*