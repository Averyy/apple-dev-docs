# setAnchorAttribute(_:for:)

**Framework**: AppKit  
**Kind**: method

Sets the part of the window that stays stationary during constraint-based layout.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setAnchorAttribute(_ attr: NSLayoutConstraint.Attribute, for orientation: NSLayoutConstraint.Orientation)
```

## Parameters

- `attr`: The layout attribute.   specifies the possible values.
- `orientation`: The window drag orientation.   specifies the possible values.

## See Also

- [func anchorAttribute(for: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Attribute](nswindow/anchorattribute(for:).md)
  Returns the part of the window that stays stationary during constraint-based layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/setanchorattribute(_:for:))*