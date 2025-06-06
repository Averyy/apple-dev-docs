# kIOHIDKeyboardEventOptionsNoKeyRepeat

**Framework**: HIDDriverKit  
**Kind**: case

An option for not applying the default key repeat logic to the event.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
kIOHIDKeyboardEventOptionsNoKeyRepeat
```

#### Discussion

The default behavior for keyboard events is to repeat keys if the user holds down the key for the amount of time defined in system preferences. Use this option to disable this behavior for the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidkeyboardeventoptions/kiohidkeyboardeventoptionsnokeyrepeat)*