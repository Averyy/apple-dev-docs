# anchorAttribute(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the part of the window that stays stationary during constraint-based layout.

**Availability**:
- macOS

## Declaration

```swift
func anchorAttribute(for orientation: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Attribute
```

```objc
- (NSLayoutAttribute) anchorAttributeForOrientation:(NSLayoutConstraintOrientation) orientation;
```

#### Return Value

Returns the layout attribute.

## Parameters

- `orientation`: The attribute for orientation. [`NSLayoutConstraint.Orientation`](../nslayoutconstraint/orientation.md)specifies the possible values.

## See Also

### Constraint-Based Layouts
- [func setAnchorAttribute(NSLayoutConstraint.Attribute, for: NSLayoutConstraint.Orientation)](./setanchorattribute%28_,for%29.md)
  Sets the part of the window that stays stationary during constraint-based layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/anchorattribute(for:))*