# backgroundColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The background color of the row.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@NSCopying
var backgroundColor: NSColor { get set }
```

```objc
@property (copy) NSColor * backgroundColor;
```

#### Discussion

The property defaults to the table view’s [`backgroundColor`](../nstableview/backgroundcolor.md), unless [`usesAlternatingRowBackgroundColors`](../nstableview/usesalternatingrowbackgroundcolors.md) is set to [`true`](../../Swift/true.md). In that case, the colors alternate, and are automatically updated as required by insertions and deletions.

The value of the background color can be customized in the `NSTableViewDelegate` method `tableView:didAddRowView:forRow:`. The property is animatable.

## See Also

### Overriding Row View Display Characteristics
- [func drawBackground(in: NSRect)](./drawbackground%28in%29.md)
  Draws the background of the row in the rectangle.
- [func drawDraggingDestinationFeedback(in: NSRect)](./drawdraggingdestinationfeedback%28in%29.md)
  Draws the row’s dragging destination feedback when the entire row is a drop target.
- [func drawSelection(in: NSRect)](./drawselection%28in%29.md)
  Draws the selected row.
- [func drawSeparator(in: NSRect)](./drawseparator%28in%29.md)
  Draws the horizontal separator between table rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablerowview/backgroundcolor)*