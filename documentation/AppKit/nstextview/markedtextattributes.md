# markedTextAttributes

**Framework**: AppKit  
**Kind**: property

The attributes used to draw marked text.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var markedTextAttributes: [NSAttributedString.Key : Any]? { get set }
```

#### Discussion

Text color, background color, and underline are the only supported attributes for marked text.

## See Also

- [var selectedRanges: [NSValue]](nstextview/selectedranges.md)
  An array containing the ranges of characters selected in the receiver’s layout manager.
- [func setSelectedRange(NSRange)](nstextview/setselectedrange(_:).md)
  Selects the specified range of characters in response to user action.
- [func setSelectedRange(NSRange, affinity: NSSelectionAffinity, stillSelecting: Bool)](nstextview/setselectedrange(_:affinity:stillselecting:).md)
  Sets the selection to a range of characters in response to user action.
- [func setSelectedRanges([NSValue], affinity: NSSelectionAffinity, stillSelecting: Bool)](nstextview/setselectedranges(_:affinity:stillselecting:).md)
  Sets the selection to the characters in an array of ranges in response to user action.
- [var selectionAffinity: NSSelectionAffinity](nstextview/selectionaffinity.md)
  The preferred direction of selection.
- [var selectionGranularity: NSSelectionGranularity](nstextview/selectiongranularity.md)
  The selection granularity for subsequent extension of a selection.
- [var insertionPointColor: NSColor!](nstextview/insertionpointcolor.md)
  The color of the insertion point.
- [func updateInsertionPointStateAndRestartTimer(Bool)](nstextview/updateinsertionpointstateandrestarttimer(_:).md)
  Updates the insertion point’s location and optionally restarts the blinking cursor timer.
- [var selectedTextAttributes: [NSAttributedString.Key : Any]](nstextview/selectedtextattributes.md)
  The attributes used to indicate the selection.
- [var linkTextAttributes: [NSAttributedString.Key : Any]?](nstextview/linktextattributes.md)
  The attributes used to draw the onscreen presentation of link text.
- [func characterIndexForInsertion(at: NSPoint) -> Int](nstextview/characterindexforinsertion(at:).md)
  Returns a character index appropriate for placing a zero-length selection for an insertion point associated with the mouse at the given point.
- [func updateCandidates()](nstextview/updatecandidates.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/markedtextattributes)*