# updateInsertionPointStateAndRestartTimer(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Updates the insertion point’s location and optionally restarts the blinking cursor timer.

**Availability**:
- macOS

## Declaration

```swift
func updateInsertionPointStateAndRestartTimer(_ restartFlag: Bool)
```

```objc
- (void) updateInsertionPointStateAndRestartTimer:(BOOL) restartFlag;
```

## Discussion

This method is invoked automatically whenever the insertion point needs to be moved; you should never need to invoke it directly, but you can override it to modify insertion point behavior.

## Parameters

- `restartFlag`: [`true`](../../Swift/true.md) to restart the blinking cursor timer, [`false`](../../Swift/false.md) otherwise.

## See Also

### Related Documentation
- [var shouldDrawInsertionPoint: Bool](./shoulddrawinsertionpoint.md)
  A Boolean value that determines whether the receiver should draw its insertion point.
- [func drawInsertionPoint(in: NSRect, color: NSColor, turnedOn: Bool)](./drawinsertionpoint%28in,color,turnedon%29.md)
  Draws or erases the insertion point.
### Managing the selection
- [var selectedRanges: [NSValue]](./selectedranges.md)
  An array containing the ranges of characters selected in the receiver’s layout manager.
- [func setSelectedRange(NSRange)](./setselectedrange%28_%29.md)
  Selects the specified range of characters in response to user action.
- [func setSelectedRange(NSRange, affinity: NSSelectionAffinity, stillSelecting: Bool)](./setselectedrange%28_,affinity,stillselecting%29.md)
  Sets the selection to a range of characters in response to user action.
- [func setSelectedRanges([NSValue], affinity: NSSelectionAffinity, stillSelecting: Bool)](./setselectedranges%28_,affinity,stillselecting%29.md)
  Sets the selection to the characters in an array of ranges in response to user action.
- [var selectionAffinity: NSSelectionAffinity](./selectionaffinity.md)
  The preferred direction of selection.
- [var selectionGranularity: NSSelectionGranularity](./selectiongranularity.md)
  The selection granularity for subsequent extension of a selection.
- [var insertionPointColor: NSColor!](./insertionpointcolor.md)
  The color of the insertion point.
- [var selectedTextAttributes: [NSAttributedString.Key : Any]](./selectedtextattributes.md)
  The attributes used to indicate the selection.
- [var markedTextAttributes: [NSAttributedString.Key : Any]?](./markedtextattributes.md)
  The attributes used to draw marked text.
- [var linkTextAttributes: [NSAttributedString.Key : Any]?](./linktextattributes.md)
  The attributes used to draw the onscreen presentation of link text.
- [func characterIndexForInsertion(at: NSPoint) -> Int](./characterindexforinsertion%28at%29.md)
  Returns a character index appropriate for placing a zero-length selection for an insertion point associated with the mouse at the given point.
- [func updateCandidates()](./updatecandidates%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/updateinsertionpointstateandrestarttimer(_:))*