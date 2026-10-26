# accessibilityIdentifier()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the accessibility element’s identity.

**Availability**:
- macOS

## Declaration

```swift
optional func accessibilityIdentifier() -> String
```

```objc
- (NSString *) accessibilityIdentifier;
```

#### Return Value

Returns the unique ID for the accessibility element. It is often used in automated testing.

#### Discussion

This method is the getter for the [`NSAccessibilityProtocol`](../nsaccessibilityprotocol.md) protocol’s [`accessibilityIdentifier`](../nsaccessibility-c.protocol/accessibilityidentifier.md) property.

## See Also

### Supporting Accessibility
- [func accessibilityFrame() -> NSRect](./accessibilityframe%28%29.md)
  Returns the accessibility element’s frame in screen coordinates.
- [func accessibilityParent() -> Any?](./accessibilityparent%28%29.md)
  Returns the accessibility element’s parent in the accessibility hierarchy.
- [func isAccessibilityFocused() -> Bool](./isaccessibilityfocused%28%29.md)
  Returns a Boolean value that indicates whether the accessibility element has the keyboard focus.
### Related Documentation
- [accessibilityIdentifier](../nsaccessibility-c.protocol/accessibilityidentifier.md)
  The accessibility element’s identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityelementprotocol/accessibilityidentifier())*