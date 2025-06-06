# stateImageRect(forBounds:)

**Framework**: AppKit  
**Kind**: method

Returns the rectangle into which the menu item’s state image should be drawn.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func stateImageRect(forBounds cellFrame: NSRect) -> NSRect
```

#### Return Value

The returned rectangle is based on `cellFrame` but encompasses only the area to be occupied by the menu item’s state image.

## Parameters

- `cellFrame`: A rectangle that defines the bounds of the receiver.

## See Also

- [func keyEquivalentRect(forBounds: NSRect) -> NSRect](nsmenuitemcell/keyequivalentrect(forbounds:).md)
  Returns the rectangle into which the menu item’s key equivalent should be drawn.
- [func titleRect(forBounds: NSRect) -> NSRect](nsmenuitemcell/titlerect(forbounds:).md)
  Returns the rectangle into which the menu item’s title should be drawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitemcell/stateimagerect(forbounds:))*