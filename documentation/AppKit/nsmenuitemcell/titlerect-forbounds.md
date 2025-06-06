# titleRect(forBounds:)

**Framework**: AppKit  
**Kind**: method

Returns the rectangle into which the menu item’s title should be drawn.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func titleRect(forBounds cellFrame: NSRect) -> NSRect
```

#### Return Value

The returned rectangle is based on `cellFrame` but encompasses only the area to be occupied by the text of the title.

## Parameters

- `cellFrame`: A rectangle that defines the bounds of the receiver.

## See Also

- [func keyEquivalentRect(forBounds: NSRect) -> NSRect](nsmenuitemcell/keyequivalentrect(forbounds:).md)
  Returns the rectangle into which the menu item’s key equivalent should be drawn.
- [func stateImageRect(forBounds: NSRect) -> NSRect](nsmenuitemcell/stateimagerect(forbounds:).md)
  Returns the rectangle into which the menu item’s state image should be drawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitemcell/titlerect(forbounds:))*