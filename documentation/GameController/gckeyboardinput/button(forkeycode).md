# button(forKeyCode:)

**Framework**: Game Controller  
**Kind**: method  
**Role**: Instance Method

Returns the button element for the specified key code.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func button(forKeyCode code: GCKeyCode) -> GCControllerButtonInput?
```

```objc
- (GCControllerButtonInput *) buttonForKeyCode:(GCKeyCode) code;
```

#### Return Value

The keyboard button element that this profile defines for the specified key code.

#### Discussion

Alternatively, you can get a button element for a key using the [`subscript(_:)`](../gcphysicalinputprofile/subscript%28_%29.md) notation that you inherit from [`GCPhysicalInputProfile`](../gcphysicalinputprofile.md), as in `keyboard[GCKeyUpArrow]`.

## Parameters

- `code`: The code for the keyboard button element.

## See Also

### Accessing Buttons
- [var isAnyKeyPressed: Bool](./isanykeypressed.md)
  A Boolean value that indicates whether the user is pressing any of the keys.
- [struct GCKeyCode](../gckeycode.md)
  The key codes for keys on a keyboard.
- [Keycode Constants](../keycode-constants.md)
  Constants for the codes of keyboard keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gckeyboardinput/button(forkeycode:))*