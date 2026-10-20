# drawSortIndicator(withFrame:in:ascending:priority:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws a sorting indicator given a cell frame contained inside a view.

**Availability**:
- macOS

## Declaration

```swift
func drawSortIndicator(withFrame cellFrame: NSRect, in controlView: NSView, ascending: Bool, priority: Int)
```

```objc
- (void) drawSortIndicatorWithFrame:(NSRect) cellFrame inView:(NSView *) controlView ascending:(BOOL) ascending priority:(NSInteger) priority;
```

#### Discussion

Override this method to customize the sorting user interface.

## Parameters

- `cellFrame`: The cell frame.
- `controlView`: The control view.
- `ascending`: If YES the sort indicator is drawn as ascending; otherwise it is drawn as descending.
- `priority`: If `priority` is 0, this is the primary sort indicator.

## See Also

### Related Documentation
- [class NSTableHeaderCell](../nstableheadercell.md)
  An object that a table header view uses to draw the content of the column headers.
### Drawing Sorting Indicators
- [func sortIndicatorRect(forBounds: NSRect) -> NSRect](./sortindicatorrect%28forbounds%29.md)
  Returns the location to display the sorting indicator given `theRect`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableheadercell/drawsortindicator(withframe:in:ascending:priority:))*