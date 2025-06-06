# sortIndicatorRect(forBounds:)

**Framework**: AppKit  
**Kind**: method

Returns the location to display the sorting indicator given `theRect`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func sortIndicatorRect(forBounds rect: NSRect) -> NSRect
```

#### Return Value

The rectangle within `theRect` that should contain the sorting indicator.

## Parameters

- `rect`: A cell rectangle.

## See Also

- [func drawSortIndicator(withFrame: NSRect, in: NSView, ascending: Bool, priority: Int)](nstableheadercell/drawsortindicator(withframe:in:ascending:priority:).md)
  Draws a sorting indicator given a cell frame contained inside a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableheadercell/sortindicatorrect(forbounds:))*