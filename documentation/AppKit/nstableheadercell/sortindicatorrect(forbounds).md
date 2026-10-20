# sortIndicatorRect(forBounds:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the location to display the sorting indicator given `theRect`.

**Availability**:
- macOS

## Declaration

```swift
func sortIndicatorRect(forBounds rect: NSRect) -> NSRect
```

```objc
- (NSRect) sortIndicatorRectForBounds:(NSRect) rect;
```

#### Return Value

The rectangle within `theRect` that should contain the sorting indicator.

## Parameters

- `rect`: A cell rectangle.

## See Also

### Drawing Sorting Indicators
- [func drawSortIndicator(withFrame: NSRect, in: NSView, ascending: Bool, priority: Int)](./drawsortindicator%28withframe,in,ascending,priority%29.md)
  Draws a sorting indicator given a cell frame contained inside a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableheadercell/sortindicatorrect(forbounds:))*