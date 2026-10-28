# smartInsert(afterStringFor:replacing:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns any whitespace that needs to be added after the string to preserve proper spacing and punctuation when the string replaces the characters in the specified range.

**Availability**:
- macOS

## Declaration

```swift
func smartInsert(afterStringFor pasteString: String, replacing charRangeToReplace: NSRange) -> String?
```

```objc
- (NSString *) smartInsertAfterStringForString:(NSString *) pasteString replacingRange:(NSRange) charRangeToReplace;
```

## Return Value

Any whitespace that needs to be added after `aString` to preserve proper spacing and punctuation when the characters in `charRange` are replaced by  `aString`. If `aString` is `nil` or if smart insertion and deletion are disabled, this method returns `nil`.

## Discussion

Don’t invoke this method directly. Instead, use [`smartInsert(for:replacing:before:after:)`](./smartinsert%28for,replacing,before,after%29.md), which calls this method as part of its implementation.

## Parameters

- `pasteString`: The string that is replacing the characters in `charRange`.
- `charRangeToReplace`: The range of characters which `aString` is replacing.

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
- [func didChangeText()](./didchangetext%28%29.md)
  Sends out necessary notifications when a text change completes.
- [var smartInsertDeleteEnabled: Bool](./smartinsertdeleteenabled.md)
  A Boolean value that controls whether the receiver inserts or deletes space around selected words so as to preserve proper spacing and punctuation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/smartinsert(afterstringfor:replacing:))*