# accessibilityIdentifier()

**Framework**: AppKit  
**Kind**: method

Returns the accessibility element’s identity.

**Availability**:
- macOS ?+

## Declaration

```swift
optional func accessibilityIdentifier() -> String
```

#### Return Value

Returns the unique ID for the accessibility element. It is often used in automated testing.

#### Discussion

This method is the getter for the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol’s [`accessibilityIdentifier`](nsaccessibility-c.protocol/accessibilityidentifier.md) property.

## See Also

- [func accessibilityFrame() -> NSRect](nsaccessibilityelementprotocol/accessibilityframe.md)
  Returns the accessibility element’s frame in screen coordinates.
- [func accessibilityParent() -> Any?](nsaccessibilityelementprotocol/accessibilityparent.md)
  Returns the accessibility element’s parent in the accessibility hierarchy.
- [func isAccessibilityFocused() -> Bool](nsaccessibilityelementprotocol/isaccessibilityfocused.md)
  Returns a Boolean value that indicates whether the accessibility element has the keyboard focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityelementprotocol/accessibilityidentifier())*