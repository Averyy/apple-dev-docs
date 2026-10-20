# accessibilityFrame()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the accessibility element’s frame in screen coordinates.

**Availability**:
- macOS

## Declaration

```swift
func accessibilityFrame() -> NSRect
```

```objc
- (NSRect) accessibilityFrame;
```

#### Return Value

The element’s frame in screen coordinates.

#### Discussion

This method is the getter for the [`NSAccessibilityProtocol`](../nsaccessibilityprotocol.md) protocol’s [`accessibilityFrame`](../nsaccessibility-c.protocol/accessibilityframe.md) property. This method is called whenever accessibility clients request the [`size`](../nsaccessibility-swift.struct/attribute/size.md) or [`position`](../nsaccessibility-swift.struct/attribute/position.md) attributes.

> **Note**:  If you are working with an [`NSAccessibilityElement`](../nsaccessibilityelement-swift.class.md) subclass, use the [`accessibilityFrameInParentSpace`](../nsaccessibilityelement-swift.class/accessibilityframeinparentspace.md) property instead. The [`accessibilityFrameInParentSpace`](../nsaccessibilityelement-swift.class/accessibilityframeinparentspace.md) property ensures that accessibility element objects move when their parents move.

## See Also

### Supporting Accessibility
- [func accessibilityIdentifier() -> String](./accessibilityidentifier%28%29.md)
  Returns the accessibility element’s identity.
- [func accessibilityParent() -> Any?](./accessibilityparent%28%29.md)
  Returns the accessibility element’s parent in the accessibility hierarchy.
- [func isAccessibilityFocused() -> Bool](./isaccessibilityfocused%28%29.md)
  Returns a Boolean value that indicates whether the accessibility element has the keyboard focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityelementprotocol/accessibilityframe())*