# accessibilityParent()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the accessibility element’s parent in the accessibility hierarchy.

**Availability**:
- macOS

## Declaration

```swift
func accessibilityParent() -> Any?
```

```objc
- (id) accessibilityParent;
```

#### Return Value

The element’s parent in the accessibility hierarchy.

#### Discussion

This method is the getter for the [`NSAccessibilityProtocol`](../nsaccessibilityprotocol.md) protocol’s [`accessibilityParent`](../nsaccessibility-c.protocol/accessibilityparent.md) property.

## See Also

### Supporting Accessibility
- [func accessibilityFrame() -> NSRect](./accessibilityframe%28%29.md)
  Returns the accessibility element’s frame in screen coordinates.
- [func accessibilityIdentifier() -> String](./accessibilityidentifier%28%29.md)
  Returns the accessibility element’s identity.
- [func isAccessibilityFocused() -> Bool](./isaccessibilityfocused%28%29.md)
  Returns a Boolean value that indicates whether the accessibility element has the keyboard focus.
### Related Documentation
- [accessibilityParent](../nsaccessibility-c.protocol/accessibilityparent.md)
  The accessibility element’s parent in the accessibility hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityelementprotocol/accessibilityparent())*