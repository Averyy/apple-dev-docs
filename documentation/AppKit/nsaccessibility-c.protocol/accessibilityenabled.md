# accessibilityEnabled

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the accessibility element responds to user events.

**Availability**:
- macOS 10.10+

## Declaration

```objc
@property (getter=isAccessibilityEnabled) BOOL accessibilityEnabled;
```

## Discussion

Returns YES if the element is enabled; otherwise, NO. Enabled elements respond to user events.

## See Also

### Configuring accessibility
- [func isAccessibilitySelectorAllowed(Selector) -> Bool](../nsaccessibilityprotocol/isaccessibilityselectorallowed%28_%29.md)
  Returns a Boolean value that indicates whether assistive apps can invoke the specified selector on the accessibility element.
- [accessibilityElement](./accessibilityelement.md)
  A Boolean value that determines whether the accessibility element participates in the accessibility hierarchy.
- [accessibilityFrame](./accessibilityframe.md)
  The accessibility element’s frame in screen coordinates.
- [accessibilityHelp](./accessibilityhelp.md)
  The help text for the accessibility element.
- [accessibilityLabel](./accessibilitylabel.md)
  A short description of the accessibility element.
- [accessibilityTitle](./accessibilitytitle.md)
  The title of the accessibility element—for example, a button’s visible text.
- [accessibilityValue](./accessibilityvalue.md)
  The accessibility element’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-c.protocol/accessibilityenabled)*