# setSelectedRange(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Selects the specified range of characters in response to user action.

**Availability**:
- macOS

## Declaration

```swift
func setSelectedRange(_ charRange: NSRange)
```

```objc
- (void) setSelectedRange:(NSRange) charRange;
```

#### Discussion

Calling this method resets the [`selectionGranularity`](./selectiongranularity.md) property to [`NSSelectionGranularity.selectByCharacter`](../nsselectiongranularity/selectbycharacter.md) and the [`selectionAffinity`](./selectionaffinity.md) property to [`NSSelectionAffinity.upstream`](../nsselectionaffinity/upstream.md).

## Parameters

- `charRange`: The range of characters to select. The range must begin and end on glyph boundaries and not split base glyphs and their nonspacing marks.

## See Also

### Managing the selection
- [var selectedRanges: [NSValue]](./selectedranges.md)
  An array containing the ranges of characters selected in the receiver’s layout manager.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/setselectedrange(_:))*