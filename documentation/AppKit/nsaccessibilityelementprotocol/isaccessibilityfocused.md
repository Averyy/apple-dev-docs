# isAccessibilityFocused()

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether the accessibility element has the keyboard focus.

**Availability**:
- macOS ?+

## Declaration

```swift
optional func isAccessibilityFocused() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if this element has the keyboard focus; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method is the getter for the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol’s [`accessibilityFocused`](nsaccessibility-c.protocol/accessibilityfocused.md) property.

## See Also

- [func accessibilityFrame() -> NSRect](nsaccessibilityelementprotocol/accessibilityframe.md)
  Returns the accessibility element’s frame in screen coordinates.
- [func accessibilityIdentifier() -> String](nsaccessibilityelementprotocol/accessibilityidentifier.md)
  Returns the accessibility element’s identity.
- [func accessibilityParent() -> Any?](nsaccessibilityelementprotocol/accessibilityparent.md)
  Returns the accessibility element’s parent in the accessibility hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityelementprotocol/isaccessibilityfocused())*