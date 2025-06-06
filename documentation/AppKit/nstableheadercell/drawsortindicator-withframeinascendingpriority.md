# drawSortIndicator(withFrame:in:ascending:priority:)

**Framework**: AppKit  
**Kind**: method

Draws a sorting indicator given a cell frame contained inside a view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func drawSortIndicator(withFrame cellFrame: NSRect, in controlView: NSView, ascending: Bool, priority: Int)
```

#### Discussion

Override this method to customize the sorting user interface.

## Parameters

- `cellFrame`: The cell frame.
- `controlView`: The control view.
- `ascending`: If YES the sort indicator is drawn as ascending; otherwise it is drawn as descending.
- `priority`: If   is 0, this is the primary sort indicator.

## See Also

- [Table View Programming Guide for Mac](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TableView/Introduction/Introduction.html#//apple_ref/doc/uid/10000026i)
- [func sortIndicatorRect(forBounds: NSRect) -> NSRect](nstableheadercell/sortindicatorrect(forbounds:).md)
  Returns the location to display the sorting indicator given `theRect`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableheadercell/drawsortindicator(withframe:in:ascending:priority:))*