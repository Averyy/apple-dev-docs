# takeColorFrom(_:)

**Framework**: AppKit  
**Kind**: method

Changes the currently selected color to the color of the specified object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func takeColorFrom(_ sender: Any?)
```

#### Discussion

This method attempts to access a property or accessor method named `color`. If the object doesn’t implement a `color` accessor, this method does nothing.

## Parameters

- `sender`: The object from which to take the new color.

## See Also

- [var color: NSColor](nscolorwell/color.md)
  The currently selected color for the color well.
- [var supportsAlpha: Bool](nscolorwell/supportsalpha.md)
  A Boolean value that determines whether the color picker supports alpha values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorwell/takecolorfrom(_:))*