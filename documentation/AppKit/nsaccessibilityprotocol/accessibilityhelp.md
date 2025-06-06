# accessibilityHelp()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the help text for the accessibility element.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func accessibilityHelp() -> String?
```

## See Also

- [func isAccessibilityElement() -> Bool](nsaccessibilityprotocol/isaccessibilityelement.md)
  Returns a Boolean value that determines whether the accessibility element participates in the accessibility hierarchy.
- [func setAccessibilityElement(Bool)](nsaccessibilityprotocol/setaccessibilityelement(_:).md)
  Sets a Boolean value that determines whether the accessibility element participates in the accessibility hierarchy.
- [func isAccessibilityEnabled() -> Bool](nsaccessibilityprotocol/isaccessibilityenabled.md)
  Returns a Boolean value that determines whether the accessibility element responds to user events.
- [func setAccessibilityEnabled(Bool)](nsaccessibilityprotocol/setaccessibilityenabled(_:).md)
  Sets a Boolean value that determines whether the accessibility element responds to user events.
- [func accessibilityFrame() -> NSRect](nsaccessibilityprotocol/accessibilityframe.md)
  Returns the accessibility element’s frame in screen coordinates.
- [func setAccessibilityFrame(NSRect)](nsaccessibilityprotocol/setaccessibilityframe(_:).md)
  Sets the accessibility element’s frame in screen coordinates.
- [func setAccessibilityHelp(String?)](nsaccessibilityprotocol/setaccessibilityhelp(_:).md)
  Sets the help text for the accessibility element.
- [func accessibilityLabel() -> String?](nsaccessibilityprotocol/accessibilitylabel.md)
  Returns a short description of the accessibility element.
- [func setAccessibilityLabel(String?)](nsaccessibilityprotocol/setaccessibilitylabel(_:).md)
  Sets a short description of the accessibility element.
- [func accessibilityTitle() -> String?](nsaccessibilityprotocol/accessibilitytitle.md)
  Returns the title of the accessibility element—for example, a button’s visible text.
- [func setAccessibilityTitle(String?)](nsaccessibilityprotocol/setaccessibilitytitle(_:).md)
  Sets the title of the accessibility element.
- [func accessibilityValue() -> Any?](nsaccessibilityprotocol/accessibilityvalue.md)
  Returns the accessibility element’s value.
- [func setAccessibilityValue(Any?)](nsaccessibilityprotocol/setaccessibilityvalue(_:).md)
  Sets the accessibility element’s value.
- [func isAccessibilitySelectorAllowed(Selector) -> Bool](nsaccessibilityprotocol/isaccessibilityselectorallowed(_:).md)
  Returns a Boolean value that indicates whether assistive apps can invoke the specified selector on the accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/accessibilityhelp())*