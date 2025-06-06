# coalesced

**Framework**: Game Controller  
**Kind**: property

The keyboard currently connected to the device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class var coalesced: GCKeyboard? { get }
```

#### Discussion

Get the keyboard input values from the keyboard’s [`keyboardInput`](gckeyboard/keyboardinput.md) controller profile. If the user connects more than one keyboard, the framework represents the combined keyboards with one coalesced keyboard object.

## See Also

- [static let GCKeyboardDidConnect: NSNotification.Name](../foundation/nsnotification/name/3626175-gckeyboarddidconnect.md)
  A notification that posts after a keyboard connects to the device.
- [static let GCKeyboardDidDisconnect: NSNotification.Name](../foundation/nsnotification/name/3626176-gckeyboarddiddisconnect.md)
  A notification that posts after a single keyboard, or the last of multiple keyboards, disconnects from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gckeyboard/coalesced)*