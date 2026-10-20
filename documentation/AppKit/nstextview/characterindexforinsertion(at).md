# characterIndexForInsertion(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a character index appropriate for placing a zero-length selection for an insertion point associated with the mouse at the given point.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func characterIndexForInsertion(at point: NSPoint) -> Int
```

```objc
- (NSUInteger) characterIndexForInsertionAtPoint:(NSPoint) point;
```

#### Return Value

The character index for the insertion point.

#### Discussion

This method should be used for insertion points associated with mouse clicks, drag events, and so forth. For other purposes, it is better to use `NSLayoutManager` methods.

The `NSTextInput` method [`characterIndexForPoint:`](../nstextinput/characterindexforpoint_.md) is not suitable for this role; it is intended only for uses related to text input methods.

## Parameters

- `point`: The point for which to return an index, in view coordinates.

## See Also

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
- [func updateInsertionPointStateAndRestartTimer(Bool)](./updateinsertionpointstateandrestarttimer%28_%29.md)
  Updates the insertion point’s location and optionally restarts the blinking cursor timer.
- [var selectedTextAttributes: [NSAttributedString.Key : Any]](./selectedtextattributes.md)
  The attributes used to indicate the selection.
- [var markedTextAttributes: [NSAttributedString.Key : Any]?](./markedtextattributes.md)
  The attributes used to draw marked text.
- [var linkTextAttributes: [NSAttributedString.Key : Any]?](./linktextattributes.md)
  The attributes used to draw the onscreen presentation of link text.
- [func updateCandidates()](./updatecandidates%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/characterindexforinsertion(at:))*