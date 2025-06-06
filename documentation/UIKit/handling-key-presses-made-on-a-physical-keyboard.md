# Handling key presses made on a physical keyboard

**Framework**: UIKit

Detect when someone presses and releases keys on a physical keyboard.

#### Overview

In iOS apps and Mac apps built with Mac Catalyst, the system reports key presses that a person makes on a physical keyboard by sending press events to responder objects in the responder chain of the active app.

A responder chain is a linked series of [`UIResponder`](uiresponder.md) objects, such as [`UIViewController`](https://developer.apple.comhttps://developer.apple.com/library/archive/releasenotes/General/RN-iPhoneSDK-3/index.html#//apple_ref/doc/uid/TP40008407-CH1-SW19) and [`UIApplication`](uiapplication.md), that either handle an event or transfer responsibility for handling the event to other responders in the app. To learn more about responders and the responder chain, see [`Using responders and the responder chain to handle events`](using-responders-and-the-responder-chain-to-handle-events.md).

##### Detect a Key Press

To detect a key press that a person makes on a physical keyboard, override [`pressesBegan(_:with:)`](uiresponder/pressesbegan(_:with:).md) in a responder object of your app such as the app delegate or main view controller.

To determine what key they pressed, iterate through the set of presses, inspecting the [`key`](uipress/key.md) property of each press. Use [`charactersIgnoringModifiers`](uikey/charactersignoringmodifiers.md) to determine the text value of key, and whether the responder should handle the key press or not. If the responder doesn’t handle the key press, call [`pressesBegan(_:with:)`](uiresponder/pressesbegan(_:with:).md) on the superclass to send the press event to the next responder in the active responder chain.

For example, the following code listing handles someone pressing either the left or right arrow.

```swift
// Handle someone pressing a key on a physical keyboard.
override func pressesBegan(_ presses: Set<UIPress>, 
                           with event: UIPressesEvent?) {
    
    var didHandleEvent = false
    
    for press in presses {
        
        // Get the pressed key.
        guard let key = press.key else { continue }
        
        if key.charactersIgnoringModifiers == UIKeyCommand.inputLeftArrow {
            // Someone pressed the left arrow key.
            // Respond to the key-press event.
            didHandleEvent = true
        }
        if key.charactersIgnoringModifiers == UIKeyCommand.inputRightArrow {
            // Someone pressed the right arrow key.
            // Respond to the key-press event.
            didHandleEvent = true
        }
    }
    
    if didHandleEvent == false {
        // If someone presses a key that you're not handling,
        // pass the event to the next responder.
        super.pressesBegan(presses, with: event)
    }
}
```

##### Detect a Key Release

Override the responder’s [`pressesEnded(_:with:)`](uiresponder/pressesended(_:with:).md) method to detect when someone releases a key. To get information about the key, do the same as you did when detecting a key press; inspect the [`key`](uipress/key.md) property of each press in the `presses` set. For example, the following code listing handles someone releasing either the left or right arrow.

```swift
// Handle someone releasing a key on a physical keyboard.
override func pressesEnded(_ presses: Set<UIPress>, with event: UIPressesEvent?) {
    
    var didHandleEvent = false
    
    
    for press in presses {
        
        // Get the released key.
        guard let key = press.key else { continue }
        
        
        if key.charactersIgnoringModifiers == UIKeyCommand.inputLeftArrow {
            // Someone released the left arrow key.
            // Respond to the event.
            didHandleEvent = true
        }
        if key.charactersIgnoringModifiers == UIKeyCommand.inputRightArrow {
            // Someone released the right arrow key.
            // Respond to the event.
            didHandleEvent = true
        }
    }
    
    if didHandleEvent == false {
        // If someone releases a key that you're not handling,
        // pass the event to the next responder.
        super.pressesEnded(presses, with: event)
    }
}
```

## See Also

- [Navigating an app’s user interface using a keyboard](navigating-an-app-s-user-interface-using-a-keyboard.md)
  Navigate between user interface elements using a keyboard and focusable UI elements in iPad apps and apps built with Mac Catalyst.
- [Adding hardware keyboard support to your app](adding-hardware-keyboard-support-to-your-app.md)
  Enhance interactions with your app by handling raw keyboard events, writing custom keyboard shortcuts, and working with gesture recognizers.
- [class UIKey](uikey.md)
  An object that provides information about the state of a keyboard key.
- [enum UIKeyboardHIDUsage](uikeyboardhidusage.md)
  A set of HID usage codes that identify the keys of a USB keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/handling-key-presses-made-on-a-physical-keyboard)*