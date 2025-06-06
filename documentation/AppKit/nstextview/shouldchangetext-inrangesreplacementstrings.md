# shouldChangeText(inRanges:replacementStrings:)

**Framework**: AppKit  
**Kind**: method

Initiates a series of delegate messages (and general notifications) to determine whether modifications can be made to the characters and attributes of the receiver’s text.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func shouldChangeText(inRanges affectedRanges: [NSValue], replacementStrings: [String]?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) to allow the change, [`false`](https://developer.apple.com/documentation/swift/false) to prohibit it.

#### Discussion

This method checks with the delegate as needed using [`textShouldBeginEditing(_:)`](nstextdelegate/textshouldbeginediting(_:).md) and [`textView(_:shouldChangeTextInRanges:replacementStrings:)`](nstextviewdelegate/textview(_:shouldchangetextinranges:replacementstrings:).md).

This method must be invoked at the start of any sequence of user-initiated editing changes. If your subclass of `NSTextView` implements

that modify the text, make sure to invoke this method to determine whether the change should be made. If the change is allowed, complete the change by invoking the [`didChangeText()`](nstextview/didchangetext().md) method. If you can’t determine the affected range or replacement string before beginning changes, pass `nil` for these values.

##### Special Considerations

If you override this method, you must call `super` at the beginning of the override.

If the receiver is not editable, this method automatically returns [`false`](https://developer.apple.com/documentation/swift/false). This result prevents instances in which a text view could be changed by user actions even though it had been set to be non-editable.

## Parameters

- `affectedRanges`: An array of ranges to change.
- `replacementStrings`: An array of strings containing the characters that replace those in  , one for each range. If only text attributes are being changed,   is  .

## See Also

- [var isEditable: Bool](nstextview/iseditable.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager allow the user to edit text.
- [func updateFontPanel()](nstextview/updatefontpanel.md)
  Updates the Font panel to contain the font attributes of the selection.
- [func updateRuler()](nstextview/updateruler.md)
  Updates the ruler view in the receiver’s enclosing scroll view to reflect the selection’s paragraph and marker attributes.
- [var acceptableDragTypes: [NSPasteboard.PasteboardType]](nstextview/acceptabledragtypes.md)
  The data types that the receiver accepts as the destination view of a dragging operation.
- [func updateDragTypeRegistration()](nstextview/updatedragtyperegistration.md)
  Updates the acceptable drag types of all text views associated with the receiver’s layout manager.
- [func selectionRange(forProposedRange: NSRange, granularity: NSSelectionGranularity) -> NSRange](nstextview/selectionrange(forproposedrange:granularity:).md)
  Returns an adjusted selected range based on the selection granularity.
- [var rangeForUserCharacterAttributeChange: NSRange](nstextview/rangeforusercharacterattributechange.md)
  The range of characters affected by an action method that changes character (not paragraph) attributes.
- [var rangesForUserCharacterAttributeChange: [NSValue]?](nstextview/rangesforusercharacterattributechange.md)
  An array containing the ranges of characters affected by an action method that changes character (not paragraph) attributes.
- [var rangeForUserParagraphAttributeChange: NSRange](nstextview/rangeforuserparagraphattributechange.md)
  The range of characters affected by an action method that changes paragraph (not character) attributes.
- [var rangesForUserParagraphAttributeChange: [NSValue]?](nstextview/rangesforuserparagraphattributechange.md)
  An array containing the ranges of characters affected by a method that changes paragraph (not character) attributes.
- [var rangeForUserTextChange: NSRange](nstextview/rangeforusertextchange.md)
  The range of characters affected by a method that changes characters (as opposed to attributes).
- [var rangesForUserTextChange: [NSValue]?](nstextview/rangesforusertextchange.md)
  An array containing the ranges of characters affected by a method that changes characters (as opposed to attributes).
- [func shouldChangeText(in: NSRange, replacementString: String?) -> Bool](nstextview/shouldchangetext(in:replacementstring:).md)
  Initiates a series of delegate messages (and general notifications) to determine whether modifications can be made to the characters and attributes of the receiver’s text.
- [func didChangeText()](nstextview/didchangetext.md)
  Sends out necessary notifications when a text change completes.
- [var smartInsertDeleteEnabled: Bool](nstextview/smartinsertdeleteenabled.md)
  A Boolean value that controls whether the receiver inserts or deletes space around selected words so as to preserve proper spacing and punctuation.
- [func smartDeleteRange(forProposedRange: NSRange) -> NSRange](nstextview/smartdeleterange(forproposedrange:).md)
  Returns an extended range that includes adjacent whitespace that should be deleted along with the proposed range in order to preserve proper spacing and punctuation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/shouldchangetext(inranges:replacementstrings:))*