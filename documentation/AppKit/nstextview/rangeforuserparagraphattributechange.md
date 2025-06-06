# rangeForUserParagraphAttributeChange

**Framework**: AppKit  
**Kind**: property

The range of characters affected by an action method that changes paragraph (not character) attributes.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var rangeForUserParagraphAttributeChange: NSRange { get }
```

#### Discussion

The range of characters affected by an action method that changes paragraph (not character) attributes, such as the NSText action method [`alignLeft(_:)`](nstext/alignleft(_:).md). For rich text this range is typically calculated by extending the range of the selection to paragraph boundaries. For plain text this range is the entire contents of the receiver. If the receiver isn’t editable or doesn’t use the Font panel, the range has a location of `NSNotFound`.

## See Also

- [var usesRuler: Bool](nstextview/usesruler.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager use a ruler.
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
- [func smartDeleteRange(forProposedRange: NSRange) -> NSRange](nstextview/smartdeleterange(forproposedrange:).md)
  Returns an extended range that includes adjacent whitespace that should be deleted along with the proposed range in order to preserve proper spacing and punctuation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/rangeforuserparagraphattributechange)*