# shouldChangeText(in:replacementString:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Initiates a series of delegate messages (and general notifications) to determine whether modifications can be made to the characters and attributes of the receiver’s text.

**Availability**:
- macOS

## Declaration

```swift
func shouldChangeText(in affectedCharRange: NSRange, replacementString: String?) -> Bool
```

```objc
- (BOOL) shouldChangeTextInRange:(NSRange) affectedCharRange replacementString:(NSString *) replacementString;
```

#### Return Value

[`true`](../../Swift/true.md) to allow the change, [`false`](../../Swift/false.md) to prohibit it.

#### Discussion

This method checks with the delegate as needed using [`textShouldBeginEditing(_:)`](../nstextdelegate/textshouldbeginediting%28_%29.md) and [`textView(_:shouldChangeTextIn:replacementString:)`](../nstextviewdelegate/textview%28_,shouldchangetextin,replacementstring%29.md).

This method must be invoked at the start of any sequence of user-initiated editing changes. If your subclass of `NSTextView` implements methods that modify the text, make sure to invoke this method to determine whether the change should be made. If the change is allowed, complete the change by invoking the [`didChangeText()`](./didchangetext%28%29.md) method.

##### Special Considerations

If you override this method, you must call `super` at the beginning of the override.

If the receiver is not editable, this method automatically returns [`false`](../../Swift/false.md). This result prevents instances in which a text view could be changed by user actions even though it had been set to be non-editable.

In macOS 10.4 and later, if there are multiple selections, this method acts on the first selected subrange.

## Parameters

- `affectedCharRange`: The range of characters affected by the proposed change.
- `replacementString`: The characters that will replace those in `affectedCharRange`. If only text attributes are being changed, `replacementString` is `nil`.

## See Also

### Related Documentation
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
- [func shouldChangeText(inRanges: [NSValue], replacementStrings: [String]?) -> Bool](./shouldchangetext%28inranges,replacementstrings%29.md)
  Initiates a series of delegate messages (and general notifications) to determine whether modifications can be made to the characters and attributes of the receiver’s text.
- [func didChangeText()](./didchangetext%28%29.md)
  Sends out necessary notifications when a text change completes.
- [var smartInsertDeleteEnabled: Bool](./smartinsertdeleteenabled.md)
  A Boolean value that controls whether the receiver inserts or deletes space around selected words so as to preserve proper spacing and punctuation.
- [func smartDeleteRange(forProposedRange: NSRange) -> NSRange](./smartdeleterange%28forproposedrange%29.md)
  Returns an extended range that includes adjacent whitespace that should be deleted along with the proposed range in order to preserve proper spacing and punctuation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/shouldchangetext(in:replacementstring:))*