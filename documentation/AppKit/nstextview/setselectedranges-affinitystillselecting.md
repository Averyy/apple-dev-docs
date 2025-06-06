# setSelectedRanges(_:affinity:stillSelecting:)

**Framework**: AppKit  
**Kind**: method

Sets the selection to the characters in an array of ranges in response to user action.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setSelectedRanges(_ ranges: [NSValue], affinity: NSSelectionAffinity, stillSelecting stillSelectingFlag: Bool)
```

#### Discussion

This method also resets the selection granularity to `NSSelectByCharacter`.

## Parameters

- `ranges`: A non-nil, non-empty array of objects responding to the NSValue   method. The ranges in the   array must begin and end on glyph boundaries and not split base glyphs and their nonspacing marks.
- `affinity`: The selection affinity for the selection. See   for more information about how affinities work.
- `stillSelectingFlag`:   to behave appropriately for a continuing selection where the user is still dragging the mouse,   otherwise. If  , the receiver doesn’t send notifications or remove the marking from its marked text. If  , the receiver posts an   to the default notification center and removes the marking from marked text if the new selection is greater than the marked region.

## See Also

- [var selectedRanges: [NSValue]](nstextview/selectedranges.md)
  An array containing the ranges of characters selected in the receiver’s layout manager.
- [func setSelectedRange(NSRange)](nstextview/setselectedrange(_:).md)
  Selects the specified range of characters in response to user action.
- [func setSelectedRange(NSRange, affinity: NSSelectionAffinity, stillSelecting: Bool)](nstextview/setselectedrange(_:affinity:stillselecting:).md)
  Sets the selection to a range of characters in response to user action.
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
- [var markedTextAttributes: [NSAttributedString.Key : Any]?](nstextview/markedtextattributes.md)
  The attributes used to draw marked text.
- [var linkTextAttributes: [NSAttributedString.Key : Any]?](nstextview/linktextattributes.md)
  The attributes used to draw the onscreen presentation of link text.
- [func characterIndexForInsertion(at: NSPoint) -> Int](nstextview/characterindexforinsertion(at:).md)
  Returns a character index appropriate for placing a zero-length selection for an insertion point associated with the mouse at the given point.
- [func updateCandidates()](nstextview/updatecandidates.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/setselectedranges(_:affinity:stillselecting:))*