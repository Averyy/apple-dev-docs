# deactivate()

**Framework**: AppKit  
**Kind**: method

Deactivates the color well.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func deactivate()
```

#### Discussion

This method detaches the color well from the system color panel. Future selections in the color panel don’t update the color well’s current color.

## See Also

- [func activate(Bool)](nscolorwell/activate(_:).md)
  Activates the color well, displays the color panel, and synchronizes the two UI elements.
- [var isActive: Bool](nscolorwell/isactive.md)
  A Boolean value that indicates whether the color well is currently active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorwell/deactivate())*