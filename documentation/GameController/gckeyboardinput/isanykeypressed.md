# isAnyKeyPressed

**Framework**: Game Controller  
**Kind**: property

A Boolean value that indicates whether the user is pressing any of the keys.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var isAnyKeyPressed: Bool { get }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), the user is pressing a key; otherwise, the user isn’t. You can use this property to check whether the user presses any key before getting the state of specific keys.

## See Also

- [func button(forKeyCode: GCKeyCode) -> GCControllerButtonInput?](gckeyboardinput/button(forkeycode:).md)
  Returns the button element for the specified key code.
- [struct GCKeyCode](gckeycode.md)
  The key codes for keys on a keyboard.
- [Keycode Constants](keycode-constants.md)
  Constants for the codes of keyboard keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gckeyboardinput/isanykeypressed)*