# smartInsert(beforeStringFor:replacing:)

**Framework**: AppKit  
**Kind**: method

Returns any whitespace that needs to be added before the string to preserve proper spacing and punctuation when the string replaces the characters in the specified range.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func smartInsert(beforeStringFor pasteString: String, replacing charRangeToReplace: NSRange) -> String?
```

#### Return Value

Any whitespace that needs to be added before `aString` to preserve proper spacing and punctuation when the characters in `charRange` are replaced by  `aString`. If `aString` is `nil` or if smart insertion and deletion are disabled, this method returns `nil`.

#### Discussion

Don’t invoke this method directly. Instead, use [`smartInsert(for:replacing:before:after:)`](nstextview/smartinsert(for:replacing:before:after:).md), which calls this method as part of its implementation.

## Parameters

- `pasteString`: The string that is replacing the characters in  .
- `charRangeToReplace`: The range of characters which   is replacing.

## See Also

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
- [func shouldChangeText(inRanges: [NSValue], replacementStrings: [String]?) -> Bool](nstextview/shouldchangetext(inranges:replacementstrings:).md)
  Initiates a series of delegate messages (and general notifications) to determine whether modifications can be made to the characters and attributes of the receiver’s text.
- [func didChangeText()](nstextview/didchangetext.md)
  Sends out necessary notifications when a text change completes.
- [var smartInsertDeleteEnabled: Bool](nstextview/smartinsertdeleteenabled.md)
  A Boolean value that controls whether the receiver inserts or deletes space around selected words so as to preserve proper spacing and punctuation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/smartinsert(beforestringfor:replacing:))*