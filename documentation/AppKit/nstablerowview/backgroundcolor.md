# backgroundColor

**Framework**: AppKit  
**Kind**: property

The background color of the row.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@NSCopying
@MainActor var backgroundColor: NSColor { get set }
```

#### Discussion

The property defaults to the table view’s [`backgroundColor`](nstableview/backgroundcolor.md), unless [`usesAlternatingRowBackgroundColors`](nstableview/usesalternatingrowbackgroundcolors.md) is set to [`true`](https://developer.apple.com/documentation/swift/true). In that case, the colors alternate, and are automatically updated as required by insertions and deletions.

The value of the background color can be customized in the `NSTableViewDelegate` method `tableView:didAddRowView:forRow:`. The property is animatable.

## See Also

- [func drawBackground(in: NSRect)](nstablerowview/drawbackground(in:).md)
  Draws the background of the row in the rectangle.
- [func drawDraggingDestinationFeedback(in: NSRect)](nstablerowview/drawdraggingdestinationfeedback(in:).md)
  Draws the row’s dragging destination feedback when the entire row is a drop target.
- [func drawSelection(in: NSRect)](nstablerowview/drawselection(in:).md)
  Draws the selected row.
- [func drawSeparator(in: NSRect)](nstablerowview/drawseparator(in:).md)
  Draws the horizontal separator between table rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablerowview/backgroundcolor)*