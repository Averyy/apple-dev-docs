# setSelectedRanges(_:affinity:stillSelecting:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the selection to the characters in an array of ranges in response to user action.

**Availability**:
- macOS

## Declaration

```swift
func setSelectedRanges(_ ranges: [NSValue], affinity: NSSelectionAffinity, stillSelecting stillSelectingFlag: Bool)
```

```objc
- (void) setSelectedRanges:(NSArray<NSValue *> *) ranges affinity:(NSSelectionAffinity) affinity stillSelecting:(BOOL) stillSelectingFlag;
```

## Discussion

This method also resets the selection granularity to `NSSelectByCharacter`.

## Parameters

- `ranges`: A non-nil, non-empty array of objects responding to the NSValue `rangeValue` method. The ranges in the `ranges` array must begin and end on glyph boundaries and not split base glyphs and their nonspacing marks.
- `affinity`: The selection affinity for the selection. See [`selectionAffinity`](./selectionaffinity.md) for more information about how affinities work.
- `stillSelectingFlag`: [`true`](../../Swift/true.md) to behave appropriately for a continuing selection where the user is still dragging the mouse, [`false`](../../Swift/false.md) otherwise. If [`true`](../../Swift/true.md), the receiver doesn’t send notifications or remove the marking from its marked text. If [`false`](../../Swift/false.md), the receiver posts an [`didChangeSelectionNotification`](./didchangeselectionnotification.md) to the default notification center and removes the marking from marked text if the new selection is greater than the marked region.

## See Also

### Managing the selection
- [var selectedRanges: [NSValue]](./selectedranges.md)
  An array containing the ranges of characters selected in the receiver’s layout manager.
- [func setSelectedRange(NSRange)](./setselectedrange%28_%29.md)
  Selects the specified range of characters in response to user action.
- [func setSelectedRange(NSRange, affinity: NSSelectionAffinity, stillSelecting: Bool)](./setselectedrange%28_,affinity,stillselecting%29.md)
  Sets the selection to a range of characters in response to user action.
- [var selectionAffinity: NSSelectionAffinity](./selectionaffinity.md)
  The preferred direction of selection.
- [var selectionGranularity: NSSelectionGranularity](./selectiongranularity.md)
  The selection granularity for subsequent extension of a selection.
- [var insertionPointColor: NSColor!](./insertionpointcolor.md)
  The color of the insertion point.
- [func updateInsertionPointStateAndRestartTimer(Bool)](./updateinsertionpointstateandrestarttimer%28_%29.md)
  Updates the insertion point’s location and optionally restarts the blinking cursor timer.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/setselectedranges(_:affinity:stillselecting:))*