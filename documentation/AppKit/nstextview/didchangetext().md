# didChangeText()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sends out necessary notifications when a text change completes.

**Availability**:
- macOS

## Declaration

```swift
func didChangeText()
```

```objc
- (void) didChangeText;
```

## Discussion

Invoked automatically at the end of a series of changes, this method posts an [`didChangeNotification`](../nstext/didchangenotification.md) to the default notification center, which also results in the delegate receiving an `NSText` delegate [`textDidChange(_:)`](../nstextdelegate/textdidchange%28_%29.md) message.

Subclasses implementing methods that change their text should invoke this method at the end of those methods. See [Subclassing NSTextView](https://developer.apple.com/library/archive/documentation/TextFonts/Conceptual/CocoaTextArchitecture/TextEditing/TextEditing.html#//apple_ref/doc/uid/TP40009459-CH3-SW16) for more information.

## See Also

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
- [var rangeForUserCharacterAttributeChange: NSRange](./rangeforusercharacterattributechange.md)
  The range of characters affected by an action method that changes character (not paragraph) attributes.
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
- [var smartInsertDeleteEnabled: Bool](./smartinsertdeleteenabled.md)
  A Boolean value that controls whether the receiver inserts or deletes space around selected words so as to preserve proper spacing and punctuation.
- [func smartDeleteRange(forProposedRange: NSRange) -> NSRange](./smartdeleterange%28forproposedrange%29.md)
  Returns an extended range that includes adjacent whitespace that should be deleted along with the proposed range in order to preserve proper spacing and punctuation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/didchangetext())*