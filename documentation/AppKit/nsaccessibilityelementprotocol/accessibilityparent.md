# accessibilityParent()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the accessibility element’s parent in the accessibility hierarchy.

**Availability**:
- macOS ?+

## Declaration

```swift
func accessibilityParent() -> Any?
```

#### Return Value

The element’s parent in the accessibility hierarchy.

#### Discussion

This method is the getter for the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol’s [`accessibilityParent`](nsaccessibility-c.protocol/accessibilityparent.md) property.

## See Also

- [func accessibilityFrame() -> NSRect](nsaccessibilityelementprotocol/accessibilityframe.md)
  Returns the accessibility element’s frame in screen coordinates.
- [func accessibilityIdentifier() -> String](nsaccessibilityelementprotocol/accessibilityidentifier.md)
  Returns the accessibility element’s identity.
- [func isAccessibilityFocused() -> Bool](nsaccessibilityelementprotocol/isaccessibilityfocused.md)
  Returns a Boolean value that indicates whether the accessibility element has the keyboard focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityelementprotocol/accessibilityparent())*