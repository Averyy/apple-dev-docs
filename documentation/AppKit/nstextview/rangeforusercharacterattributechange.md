# rangeForUserCharacterAttributeChange

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The range of characters affected by an action method that changes character (not paragraph) attributes.

**Availability**:
- macOS

## Declaration

```swift
var rangeForUserCharacterAttributeChange: NSRange { get }
```

```objc
@property (readonly) NSRange rangeForUserCharacterAttributeChange;
```

#### Discussion

The range of characters affected by an action method that changes character (not paragraph) attributes, such as the NSText action method [`changeFont(_:)`](../nstext/changefont%28_%29.md). For rich text this range is typically the range of the selection. For plain text this range is the entire contents of the receiver. If the receiver isn’t editable or doesn’t use the Font panel, the range has a location of `NSNotFound`.

## See Also

### Related Documentation
- [var usesFontPanel: Bool](./usesfontpanel.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager use the Font panel and Font menu.
- [var isEditable: Bool](./iseditable.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager allow the user to edit text.
### Customizing subclass behaviors
- [func updateFontPanel()](./updatefontpanel%28%29.md)
  Updates the Font panel to contain the font attributes of the selection.
- [func updateRuler()](./updateruler%28%29.md)
  Updates the ruler view in the receiver’s enclosing scroll view to reflect the selection’s paragraph and marker attributes.
- [var acceptableDragTypes: [NSPasteboard.PasteboardType]](./acceptabledragtypes.md)
  The data types that the receiver accepts as the destination view of a dragging operation.
- [func updateDragTypeRegistration()](./updatedragtyperegistration%28%29.md)
  Updates the acceptable drag types of all text views associated with the receiver’s layout manager.
- [func selectionRange(forProposedRange: NSRange, granularity: NSSelectionGranularity) -> NSRange](./selectionrange%28forproposedrange,granularity%29.md)
  Returns an adjusted selected range based on the selection granularity.
- [var rangesForUserCharacterAttributeChange: [NSValue]?](./rangesforusercharacterattributechange.md)
  An array containing the ranges of characters affected by an action method that changes character (not paragraph) attributes.
- [var rangeForUserParagraphAttributeChange: NSRange](./rangeforuserparagraphattributechange.md)
  The range of characters affected by an action method that changes paragraph (not character) attributes.
- [var rangesForUserParagraphAttributeChange: [NSValue]?](./rangesforuserparagraphattributechange.md)
  An array containing the ranges of characters affected by a method that changes paragraph (not character) attributes.
- [var rangeForUserTextChange: NSRange](./rangeforusertextchange.md)
  The range of characters affected by a method that changes characters (as opposed to attributes).
- [var rangesForUserTextChange: [NSValue]?](./rangesforusertextchange.md)
  An array containing the ranges of characters affected by a method that changes characters (as opposed to attributes).
- [func shouldChangeText(in: NSRange, replacementString: String?) -> Bool](./shouldchangetext%28in,replacementstring%29.md)
  Initiates a series of delegate messages (and general notifications) to determine whether modifications can be made to the characters and attributes of the receiver’s text.
- [func shouldChangeText(inRanges: [NSValue], replacementStrings: [String]?) -> Bool](./shouldchangetext%28inranges,replacementstrings%29.md)
  Initiates a series of delegate messages (and general notifications) to determine whether modifications can be made to the characters and attributes of the receiver’s text.
- [func didChangeText()](./didchangetext%28%29.md)
  Sends out necessary notifications when a text change completes.
- [var smartInsertDeleteEnabled: Bool](./smartinsertdeleteenabled.md)
  A Boolean value that controls whether the receiver inserts or deletes space around selected words so as to preserve proper spacing and punctuation.
- [func smartDeleteRange(forProposedRange: NSRange) -> NSRange](./smartdeleterange%28forproposedrange%29.md)
  Returns an extended range that includes adjacent whitespace that should be deleted along with the proposed range in order to preserve proper spacing and punctuation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/rangeforusercharacterattributechange)*