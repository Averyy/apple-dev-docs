# NSTextViewDelegate

**Framework**: AppKit  
**Kind**: protocol

A set of optional methods that text view delegates can use to manage selection, set text attributes, work with the spell checker, and more.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSTextViewDelegate : NSTextDelegate
```

## Topics

### Accessing Text System Objects
- [func undoManager(for: NSTextView) -> UndoManager?](nstextviewdelegate/undomanager(for:).md)
  Returns the undo manager for the specified text view.
### Controlling Display
- [func textView(NSTextView, willDisplayToolTip: String, forCharacterAt: Int) -> String?](nstextviewdelegate/textview(_:willdisplaytooltip:forcharacterat:).md)
  Returns the actual tooltip to display.
### Supporting Quick Look
- [func textView(NSTextView, urlForContentsOf: NSTextAttachment, at: Int) -> URL?](nstextviewdelegate/textview(_:urlforcontentsof:at:).md)
  Returns a URL representing the document contents for a text attachment.
### Managing the Selection
- [func textView(NSTextView, willChangeSelectionFromCharacterRange: NSRange, toCharacterRange: NSRange) -> NSRange](nstextviewdelegate/textview(_:willchangeselectionfromcharacterrange:tocharacterrange:).md)
  Returns the actual range to select.
- [func textView(NSTextView, willChangeSelectionFromCharacterRanges: [NSValue], toCharacterRanges: [NSValue]) -> [NSValue]](nstextviewdelegate/textview(_:willchangeselectionfromcharacterranges:tocharacterranges:).md)
  Returns the actual character ranges to select.
- [func textViewDidChangeSelection(Notification)](nstextviewdelegate/textviewdidchangeselection(_:).md)
  Sent when the selection changes in the text view.
- [func textView(NSTextView, candidates: [NSTextCheckingResult], forSelectedRange: NSRange) -> [NSTextCheckingResult]](nstextviewdelegate/textview(_:candidates:forselectedrange:).md)
  Returns an array of text objects to include in a text selection.
- [func textView(NSTextView, candidatesForSelectedRange: NSRange) -> [Any]?](nstextviewdelegate/textview(_:candidatesforselectedrange:).md)
  Returns an array of objects that represent the elements of a selection.
- [func textView(NSTextView, shouldSelectCandidateAt: Int) -> Bool](nstextviewdelegate/textview(_:shouldselectcandidateat:).md)
  Returns a Boolean value that indicates whether to select the text object at the index.
- [func textView(NSTextView, shouldUpdateTouchBarItemIdentifiers: [NSTouchBarItem.Identifier]) -> [NSTouchBarItem.Identifier]](nstextviewdelegate/textview(_:shouldupdatetouchbaritemidentifiers:).md)
  Returns and array of touch bar elements for the framework to update.
### Managing the Pasteboard
- [func textView(NSTextView, writablePasteboardTypesFor: any NSTextAttachmentCellProtocol, at: Int) -> [NSPasteboard.PasteboardType]](nstextviewdelegate/textview(_:writablepasteboardtypesfor:at:).md)
  Returns the writable pasteboard types for a given cell.
- [func textView(NSTextView, write: any NSTextAttachmentCellProtocol, at: Int, to: NSPasteboard, type: NSPasteboard.PasteboardType) -> Bool](nstextviewdelegate/textview(_:write:at:to:type:).md)
  Returns whether data of the specified type for the given cell could be written to the specified pasteboard.
### Setting Text Attributes
- [func textView(NSTextView, shouldChangeTextIn: NSRange, replacementString: String?) -> Bool](nstextviewdelegate/textview(_:shouldchangetextin:replacementstring:).md)
  Sent when a text view needs to determine if text in a specified range should be changed.
- [func textView(NSTextView, shouldChangeTextInRanges: [NSValue], replacementStrings: [String]?) -> Bool](nstextviewdelegate/textview(_:shouldchangetextinranges:replacementstrings:).md)
  Sent when a text view needs to determine if text in an array of specified ranges should be changed.
- [func textView(NSTextView, shouldChangeTypingAttributes: [String : Any], toAttributes: [NSAttributedString.Key : Any]) -> [NSAttributedString.Key : Any]](nstextviewdelegate/textview(_:shouldchangetypingattributes:toattributes:).md)
  Sent when the typing attributes are changed.
- [func textViewDidChangeTypingAttributes(Notification)](nstextviewdelegate/textviewdidchangetypingattributes(_:).md)
  Sent when a text view’s typing attributes change.
### Clicking and Pasting
- [func textView(NSTextView, clickedOn: any NSTextAttachmentCellProtocol, in: NSRect, at: Int)](nstextviewdelegate/textview(_:clickedon:in:at:).md)
  Sent when the user clicks a cell.
- [func textView(NSTextView, doubleClickedOn: any NSTextAttachmentCellProtocol, in: NSRect, at: Int)](nstextviewdelegate/textview(_:doubleclickedon:in:at:).md)
  Sent when the user double-clicks a cell.
- [func textView(NSTextView, clickedOnLink: Any, at: Int) -> Bool](nstextviewdelegate/textview(_:clickedonlink:at:).md)
  Sent after the user clicks a link.
### Working With the Spelling Checker
- [func textView(NSTextView, shouldSetSpellingState: Int, range: NSRange) -> Int](nstextviewdelegate/textview(_:shouldsetspellingstate:range:).md)
  Sent when the spelling state is changed.
- [func textView(NSTextView, willCheckTextIn: NSRange, options: [NSSpellChecker.OptionKey : Any], types: UnsafeMutablePointer<NSTextCheckingTypes>) -> [NSSpellChecker.OptionKey : Any]](nstextviewdelegate/textview(_:willchecktextin:options:types:).md)
  Invoked to allow the delegate to modify the text checking process before it occurs.
- [func textView(NSTextView, didCheckTextIn: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any], results: [NSTextCheckingResult], orthography: NSOrthography, wordCount: Int) -> [NSTextCheckingResult]](nstextviewdelegate/textview(_:didchecktextin:types:options:results:orthography:wordcount:).md)
  Invoked to allow the delegate to modify the text checking results after checking has occurred.
### Responding to writing tools interactions
- [func textViewWritingToolsWillBegin(NSTextView)](nstextviewdelegate/textviewwritingtoolswillbegin(_:).md)
- [func textViewWritingToolsDidEnd(NSTextView)](nstextviewdelegate/textviewwritingtoolsdidend(_:).md)
- [func textView(NSTextView, writingToolsIgnoredRangesInEnclosingRange: NSRange) -> [NSValue]](nstextviewdelegate/textview(_:writingtoolsignoredrangesinenclosingrange:).md)
### Dragging
- [func textView(NSTextView, draggedCell: any NSTextAttachmentCellProtocol, in: NSRect, event: NSEvent, at: Int)](nstextviewdelegate/textview(_:draggedcell:in:event:at:).md)
  Sent when the user attempts to drag a cell.
### Completing text
- [func textView(NSTextView, completions: [String], forPartialWordRange: NSRange, indexOfSelectedItem: UnsafeMutablePointer<Int>?) -> [String]](nstextviewdelegate/textview(_:completions:forpartialwordrange:indexofselecteditem:).md)
  Returns the actual completions for a partial word.
### Displaying the sharing service picker
- [func textView(NSTextView, willShow: NSSharingServicePicker, forItems: [Any]) -> NSSharingServicePicker?](nstextviewdelegate/textview(_:willshow:foritems:).md)
  Returns a sharing service picker for the current selection.
### Performing Commands
- [func textView(NSTextView, doCommandBy: Selector) -> Bool](nstextviewdelegate/textview(_:docommandby:).md)
  Sent to allow the delegate to perform the command for the text view.
### Contextual Menu Management
- [func textView(NSTextView, menu: NSMenu, for: NSEvent, at: Int) -> NSMenu?](nstextviewdelegate/textview(_:menu:for:at:).md)
  Allows delegate to control the context menu returned by the text view.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTextDelegate](nstextdelegate.md)
### Conforming Types
- [NSOutlineView](nsoutlineview.md)
- [NSTableView](nstableview.md)

## See Also

- [class NSTextField](nstextfield.md)
  Text the user can select or edit to send an action message to a target when the user presses the Return key.
- [protocol NSTextFieldDelegate](nstextfielddelegate.md)
  A protocol that a text field delegate can use to control its field editor action menu.
- [class NSTextView](nstextview.md)
  A view that draws text and handles user interactions with that text.
- [protocol NSTextDelegate](nstextdelegate.md)
  A set of optional methods implemented by the delegate of an [`NSText`](nstext.md) object to edit text and change text formats.
- [class NSText](nstext.md)
  The most general programmatic interface for objects that manage text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate)*