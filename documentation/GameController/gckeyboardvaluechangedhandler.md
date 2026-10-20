# GCKeyboardValueChangedHandler

**Framework**: Game Controller  
**Kind**: typealias  
**Role**: Type Alias

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

```c
typedef void (^)(GCKeyboardInput *, GCControllerButtonInput *, long, _Bool) GCKeyboardValueChangedHandler;
```

## Parameters

- `keyboard`: The keyboard controller profile for the physical keyboard.
- `key`: The element for the key that changes.
- `keyCode`: The code for the key that changes.
- `pressed`: [`true`](../Swift/true.md) if the user presses the key at the time the change occurs; otherwise, [`false`](../Swift/false.md).

## See Also

### Getting Change Information
- [var keyChangedHandler: GCKeyboardValueChangedHandler?](./gckeyboardinput/keychangedhandler.md)
  The block that the profile calls when the user presses a key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gckeyboardvaluechangedhandler)*