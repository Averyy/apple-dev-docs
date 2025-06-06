# accessibilitySharedFocusElements()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the array of elements that shares the keyboard focus with the accessibility element.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func accessibilitySharedFocusElements() -> [Any]?
```

## See Also

- [func accessibilityApplicationFocusedUIElement() -> Any?](nsaccessibilityprotocol/accessibilityapplicationfocuseduielement.md)
  Returns the child accessibility element with the current focus.
- [func setAccessibilityApplicationFocusedUIElement(Any?)](nsaccessibilityprotocol/setaccessibilityapplicationfocuseduielement(_:).md)
  Sets the child accessibility element with the current focus.
- [func isAccessibilityFocused() -> Bool](nsaccessibilityprotocol/isaccessibilityfocused.md)
  Returns a Boolean value that determines whether the accessibility element has the keyboard focus.
- [func setAccessibilityFocused(Bool)](nsaccessibilityprotocol/setaccessibilityfocused(_:).md)
  Sets a Boolean value that determines whether the accessibility element has the keyboard focus.
- [func accessibilityFocusedWindow() -> Any?](nsaccessibilityprotocol/accessibilityfocusedwindow.md)
  Returns the child window with the current focus.
- [func setAccessibilityFocusedWindow(Any?)](nsaccessibilityprotocol/setaccessibilityfocusedwindow(_:).md)
  Sets the child window with the current focus.
- [func setAccessibilitySharedFocusElements([Any]?)](nsaccessibilityprotocol/setaccessibilitysharedfocuselements(_:).md)
  Sets the array of elements that shares the keyboard focus with the accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/accessibilitysharedfocuselements())*