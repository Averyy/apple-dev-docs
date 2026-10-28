# accessibilitySharedFocusElements

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of elements that shares the keyboard focus with the accessibility element.

**Availability**:
- macOS 10.10+

## Declaration

```objc
@property (copy, nullable) NSArray * accessibilitySharedFocusElements;
```

## Discussion

Use this property to manage elements that share the keyboard focus—for example, a search field with completion menu below it.

## See Also

### Setting the focus
- [accessibilityApplicationFocusedUIElement](./accessibilityapplicationfocuseduielement.md)
  The child accessibility element with the current focus.
- [accessibilityFocused](./accessibilityfocused.md)
  A Boolean value that determines whether the accessibility element has the keyboard focus.
- [accessibilityFocusedWindow](./accessibilityfocusedwindow.md)
  The child window with the current focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-c.protocol/accessibilitysharedfocuselements)*