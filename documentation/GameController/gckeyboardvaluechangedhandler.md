# GCKeyboardValueChangedHandler

**Framework**: Game Controller  
**Kind**: typealias

The signature for the block that the keyboard input profile calls when a key value changes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
typealias GCKeyboardValueChangedHandler = (GCKeyboardInput, GCControllerButtonInput, GCKeyCode, Bool) -> Void
```

## Parameters

- `keyboard`: The keyboard controller profile for the physical keyboard.
- `key`: The element for the key that changes.
- `keyCode`: The code for the key that changes.
- `pressed`:   if the user presses the key at the time the change occurs; otherwise,  .

## See Also

- [var keyChangedHandler: GCKeyboardValueChangedHandler?](gckeyboardinput/keychangedhandler.md)
  The block that the profile calls when the user presses a key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gckeyboardvaluechangedhandler)*