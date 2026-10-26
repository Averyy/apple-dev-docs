# isAccessibilitySelectorAllowed(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a Boolean value that indicates whether assistive apps can invoke the specified selector on the accessibility element.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func isAccessibilitySelectorAllowed(_ selector: Selector) -> Bool
```

```objc
- (BOOL) isAccessibilitySelectorAllowed:(SEL) selector;
```

#### Return Value

[`true`](../../Swift/true.md), if accessibility clients can call the selector; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `selector`: The selector to check.

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
- [func setAccessibilityHelp(String?)](./setaccessibilityhelp%28_%29.md)
  Sets the help text for the accessibility element.
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
- [accessibilityElement](../nsaccessibility-c.protocol/accessibilityelement.md)
  A Boolean value that determines whether the accessibility element participates in the accessibility hierarchy.
- [accessibilityEnabled](../nsaccessibility-c.protocol/accessibilityenabled.md)
  A Boolean value that determines whether the accessibility element responds to user events.
- [accessibilityFrame](../nsaccessibility-c.protocol/accessibilityframe.md)
  The accessibility element’s frame in screen coordinates.
- [accessibilityHelp](../nsaccessibility-c.protocol/accessibilityhelp.md)
  The help text for the accessibility element.
- [accessibilityLabel](../nsaccessibility-c.protocol/accessibilitylabel.md)
  A short description of the accessibility element.
- [accessibilityTitle](../nsaccessibility-c.protocol/accessibilitytitle.md)
  The title of the accessibility element—for example, a button’s visible text.
- [accessibilityValue](../nsaccessibility-c.protocol/accessibilityvalue.md)
  The accessibility element’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/isaccessibilityselectorallowed(_:))*