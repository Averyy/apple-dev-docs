# setAnchorAttribute(_:for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the part of the window that stays stationary during constraint-based layout.

**Availability**:
- macOS

## Declaration

```swift
func setAnchorAttribute(_ attr: NSLayoutConstraint.Attribute, for orientation: NSLayoutConstraint.Orientation)
```

```objc
- (void) setAnchorAttribute:(NSLayoutAttribute) attr forOrientation:(NSLayoutConstraintOrientation) orientation;
```

## Parameters

- `attr`: The layout attribute. [`NSLayoutConstraint.Attribute`](../../UIKit/nslayoutconstraint/attribute.md) specifies the possible values.
- `orientation`: The window drag orientation. [`NSLayoutConstraint.Orientation`](../nslayoutconstraint/orientation.md) specifies the possible values.

## See Also

### Constraint-Based Layouts
- [func anchorAttribute(for: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Attribute](./anchorattribute%28for%29.md)
  Returns the part of the window that stays stationary during constraint-based layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/setanchorattribute(_:for:))*