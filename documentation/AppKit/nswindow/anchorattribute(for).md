# anchorAttribute(for:)

**Framework**: AppKit  
**Kind**: method

Returns the part of the window that stays stationary during constraint-based layout.

**Availability**:
- macOS ?+

## Declaration

```swift
func anchorAttribute(for orientation: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Attribute
```

#### Return Value

Returns the layout attribute.

## Parameters

- `orientation`: The attribute for orientation. [`NSLayoutConstraint.Orientation`](nslayoutconstraint/orientation.md)specifies the possible values.

## See Also

- [func setAnchorAttribute(NSLayoutConstraint.Attribute, for: NSLayoutConstraint.Orientation)](nswindow/setanchorattribute(_:for:).md)
  Sets the part of the window that stays stationary during constraint-based layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/anchorattribute(for:))*