# isAccessibilityFocused()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the accessibility element has the keyboard focus.

**Availability**:
- macOS

## Declaration

```swift
optional func isAccessibilityFocused() -> Bool
```

```objc
- (BOOL) isAccessibilityFocused;
```

## Return Value

[`true`](../../Swift/true.md) if this element has the keyboard focus; otherwise, [`false`](../../Swift/false.md).

## Discussion

This method is the getter for the [`NSAccessibilityProtocol`](../nsaccessibilityprotocol.md) protocol’s [`accessibilityFocused`](../nsaccessibility-c.protocol/accessibilityfocused.md) property.

## See Also

### Supporting Accessibility
- [func accessibilityFrame() -> NSRect](./accessibilityframe%28%29.md)
  Returns the accessibility element’s frame in screen coordinates.
- [func accessibilityIdentifier() -> String](./accessibilityidentifier%28%29.md)
  Returns the accessibility element’s identity.
- [func accessibilityParent() -> Any?](./accessibilityparent%28%29.md)
  Returns the accessibility element’s parent in the accessibility hierarchy.
### Related Documentation
- [accessibilityFocused](../nsaccessibility-c.protocol/accessibilityfocused.md)
  A Boolean value that determines whether the accessibility element has the keyboard focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityelementprotocol/isaccessibilityfocused())*