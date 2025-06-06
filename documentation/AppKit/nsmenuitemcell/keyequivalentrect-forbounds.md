# keyEquivalentRect(forBounds:)

**Framework**: AppKit  
**Kind**: method

Returns the rectangle into which the menu item’s key equivalent should be drawn.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func keyEquivalentRect(forBounds cellFrame: NSRect) -> NSRect
```

#### Return Value

The returned rectangle is based on `cellFrame` but encompasses only the area to be occupied by the key equivalent.

## Parameters

- `cellFrame`: A rectangle that defines the bounds of the receiver.

## See Also

- [func stateImageRect(forBounds: NSRect) -> NSRect](nsmenuitemcell/stateimagerect(forbounds:).md)
  Returns the rectangle into which the menu item’s state image should be drawn.
- [func titleRect(forBounds: NSRect) -> NSRect](nsmenuitemcell/titlerect(forbounds:).md)
  Returns the rectangle into which the menu item’s title should be drawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitemcell/keyequivalentrect(forbounds:))*