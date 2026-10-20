# setAccessibilityApplicationFocusedUIElement(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets the child accessibility element with the current focus.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func setAccessibilityApplicationFocusedUIElement(_ accessibilityApplicationFocusedUIElement: Any?)
```

## See Also

### Setting the focus
- [func accessibilityApplicationFocusedUIElement() -> Any?](./accessibilityapplicationfocuseduielement%28%29.md)
  Returns the child accessibility element with the current focus.
- [func isAccessibilityFocused() -> Bool](./isaccessibilityfocused%28%29.md)
  Returns a Boolean value that determines whether the accessibility element has the keyboard focus.
- [func setAccessibilityFocused(Bool)](./setaccessibilityfocused%28_%29.md)
  Sets a Boolean value that determines whether the accessibility element has the keyboard focus.
- [func accessibilityFocusedWindow() -> Any?](./accessibilityfocusedwindow%28%29.md)
  Returns the child window with the current focus.
- [func setAccessibilityFocusedWindow(Any?)](./setaccessibilityfocusedwindow%28_%29.md)
  Sets the child window with the current focus.
- [func accessibilitySharedFocusElements() -> [Any]?](./accessibilitysharedfocuselements%28%29.md)
  Returns the array of elements that shares the keyboard focus with the accessibility element.
- [func setAccessibilitySharedFocusElements([Any]?)](./setaccessibilitysharedfocuselements%28_%29.md)
  Sets the array of elements that shares the keyboard focus with the accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/setaccessibilityapplicationfocuseduielement(_:))*