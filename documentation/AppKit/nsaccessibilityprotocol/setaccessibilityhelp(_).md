# setAccessibilityHelp(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets the help text for the accessibility element.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func setAccessibilityHelp(_ accessibilityHelp: String?)
```

## See Also

### Configuring accessibility
- [func isAccessibilityElement() -> Bool](./isaccessibilityelement%28%29.md)
  Returns a Boolean value that determines whether the accessibility element participates in the accessibility hierarchy.
- [func setAccessibilityElement(Bool)](./setaccessibilityelement%28_%29.md)
  Sets a Boolean value that determines whether the accessibility element participates in the accessibility hierarchy.
- [func isAccessibilityEnabled() -> Bool](./isaccessibilityenabled%28%29.md)
  Returns a Boolean value that determines whether the accessibility element responds to user events.
- [func setAccessibilityEnabled(Bool)](./setaccessibilityenabled%28_%29.md)
  Sets a Boolean value that determines whether the accessibility element responds to user events.
- [func accessibilityFrame() -> NSRect](./accessibilityframe%28%29.md)
  Returns the accessibility element’s frame in screen coordinates.
- [func setAccessibilityFrame(NSRect)](./setaccessibilityframe%28_%29.md)
  Sets the accessibility element’s frame in screen coordinates.
- [func accessibilityHelp() -> String?](./accessibilityhelp%28%29.md)
  Returns the help text for the accessibility element.
- [func accessibilityLabel() -> String?](./accessibilitylabel%28%29.md)
  Returns a short description of the accessibility element.
- [func setAccessibilityLabel(String?)](./setaccessibilitylabel%28_%29.md)
  Sets a short description of the accessibility element.
- [func accessibilityTitle() -> String?](./accessibilitytitle%28%29.md)
  Returns the title of the accessibility element—for example, a button’s visible text.
- [func setAccessibilityTitle(String?)](./setaccessibilitytitle%28_%29.md)
  Sets the title of the accessibility element.
- [func accessibilityValue() -> Any?](./accessibilityvalue%28%29.md)
  Returns the accessibility element’s value.
- [func setAccessibilityValue(Any?)](./setaccessibilityvalue%28_%29.md)
  Sets the accessibility element’s value.
- [func isAccessibilitySelectorAllowed(Selector) -> Bool](./isaccessibilityselectorallowed%28_%29.md)
  Returns a Boolean value that indicates whether assistive apps can invoke the specified selector on the accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/setaccessibilityhelp(_:))*