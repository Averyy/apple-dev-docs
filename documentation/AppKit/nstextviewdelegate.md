# NSTextViewDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A set of optional methods that text view delegates can use to manage selection, set text attributes, work with the spell checker, and more.

**Availability**:
- macOS

## Declaration

```swift
protocol NSTextViewDelegate : NSTextDelegate
```

```objc
@protocol NSTextViewDelegate <NSTextDelegate>
```

## Topics

### Accessing Text System Objects
- [func undoManager(for: NSTextView) -> UndoManager?](./nstextviewdelegate/undomanager%28for%29.md)
  Returns the undo manager for the specified text view.
### Controlling Display
- [func textView(NSTextView, willDisplayToolTip: String, forCharacterAt: Int) -> String?](./nstextviewdelegate/textview%28_,willdisplaytooltip,forcharacterat%29.md)
  Returns the actual tooltip to display.
### Supporting Quick Look
- [func textView(NSTextView, urlForContentsOf: NSTextAttachment, at: Int) -> URL?](./nstextviewdelegate/textview%28_,urlforcontentsof,at%29.md)
  Returns a URL representing the document contents for a text attachment.
### Managing the Selection
- [func textView(NSTextView, willChangeSelectionFromCharacterRange: NSRange, toCharacterRange: NSRange) -> NSRange](./nstextviewdelegate/textview%28_,willchangeselectionfromcharacterrange,tocharacterrange%29.md)
  Returns the actual range to select.
- [func textView(NSTextView, willChangeSelectionFromCharacterRanges: [NSValue], toCharacterRanges: [NSValue]) -> [NSValue]](./nstextviewdelegate/textview%28_,willchangeselectionfromcharacterranges,tocharacterranges%29.md)
  Returns the actual character ranges to select.
- [func textViewDidChangeSelection(Notification)](./nstextviewdelegate/textviewdidchangeselection%28_%29.md)
  Sent when the selection changes in the text view.
- [func textView(NSTextView, candidates: [NSTextCheckingResult], forSelectedRange: NSRange) -> [NSTextCheckingResult]](./nstextviewdelegate/textview%28_,candidates,forselectedrange%29.md)
  Returns an array of text objects to include in a text selection.
- [func textView(NSTextView, candidatesForSelectedRange: NSRange) -> [Any]?](./nstextviewdelegate/textview%28_,candidatesforselectedrange%29.md)
  Returns an array of objects that represent the elements of a selection.
- [func textView(NSTextView, shouldSelectCandidateAt: Int) -> Bool](./nstextviewdelegate/textview%28_,shouldselectcandidateat%29.md)
  Returns a Boolean value that indicates whether to select the text object at the index.
- [func textView(NSTextView, shouldUpdateTouchBarItemIdentifiers: [NSTouchBarItem.Identifier]) -> [NSTouchBarItem.Identifier]](./nstextviewdelegate/textview%28_,shouldupdatetouchbaritemidentifiers%29.md)
  Returns and array of touch bar elements for the framework to update.
### Managing the Pasteboard
- [func textView(NSTextView, writablePasteboardTypesFor: any NSTextAttachmentCellProtocol, at: Int) -> [NSPasteboard.PasteboardType]](./nstextviewdelegate/textview%28_,writablepasteboardtypesfor,at%29.md)
  Returns the writable pasteboard types for a given cell.
- [func textView(NSTextView, write: any NSTextAttachmentCellProtocol, at: Int, to: NSPasteboard, type: NSPasteboard.PasteboardType) -> Bool](./nstextviewdelegate/textview%28_,write,at,to,type%29.md)
  Returns whether data of the specified type for the given cell could be written to the specified pasteboard.
### Setting Text Attributes
- [func textView(NSTextView, shouldChangeTextIn: NSRange, replacementString: String?) -> Bool](./nstextviewdelegate/textview%28_,shouldchangetextin,replacementstring%29.md)
  Sent when a text view needs to determine if text in a specified range should be changed.
- [func textView(NSTextView, shouldChangeTextInRanges: [NSValue], replacementStrings: [String]?) -> Bool](./nstextviewdelegate/textview%28_,shouldchangetextinranges,replacementstrings%29.md)
  Sent when a text view needs to determine if text in an array of specified ranges should be changed.
- [func textView(NSTextView, shouldChangeTypingAttributes: [String : Any], toAttributes: [NSAttributedString.Key : Any]) -> [NSAttributedString.Key : Any]](./nstextviewdelegate/textview%28_,shouldchangetypingattributes,toattributes%29.md)
  Sent when the typing attributes are changed.
- [func textViewDidChangeTypingAttributes(Notification)](./nstextviewdelegate/textviewdidchangetypingattributes%28_%29.md)
  Sent when a text view’s typing attributes change.
### Clicking and Pasting
- [func textView(NSTextView, clickedOn: any NSTextAttachmentCellProtocol, in: NSRect, at: Int)](./nstextviewdelegate/textview%28_,clickedon,in,at%29.md)
  Sent when the user clicks a cell.
- [func textView(NSTextView, doubleClickedOn: any NSTextAttachmentCellProtocol, in: NSRect, at: Int)](./nstextviewdelegate/textview%28_,doubleclickedon,in,at%29.md)
  Sent when the user double-clicks a cell.
- [func textView(NSTextView, clickedOnLink: Any, at: Int) -> Bool](./nstextviewdelegate/textview%28_,clickedonlink,at%29.md)
  Sent after the user clicks a link.
### Working With the Spelling Checker
- [func textView(NSTextView, shouldSetSpellingState: Int, range: NSRange) -> Int](./nstextviewdelegate/textview%28_,shouldsetspellingstate,range%29.md)
  Sent when the spelling state is changed.
- [func textView(NSTextView, willCheckTextIn: NSRange, options: [NSSpellChecker.OptionKey : Any], types: UnsafeMutablePointer<NSTextCheckingTypes>) -> [NSSpellChecker.OptionKey : Any]](./nstextviewdelegate/textview%28_,willchecktextin,options,types%29.md)
  Invoked to allow the delegate to modify the text checking process before it occurs.
- [func textView(NSTextView, didCheckTextIn: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any], results: [NSTextCheckingResult], orthography: NSOrthography, wordCount: Int) -> [NSTextCheckingResult]](./nstextviewdelegate/textview%28_,didchecktextin,types,options,results,orthography,wordcount%29.md)
  Invoked to allow the delegate to modify the text checking results after checking has occurred.
### Responding to writing tools interactions
- [func textViewWritingToolsWillBegin(NSTextView)](./nstextviewdelegate/textviewwritingtoolswillbegin%28_%29.md)
- [func textViewWritingToolsDidEnd(NSTextView)](./nstextviewdelegate/textviewwritingtoolsdidend%28_%29.md)
- [func textView(NSTextView, writingToolsIgnoredRangesInEnclosingRange: NSRange) -> [NSValue]](./nstextviewdelegate/textview%28_,writingtoolsignoredrangesinenclosingrange%29.md)
### Dragging
- [func textView(NSTextView, draggedCell: any NSTextAttachmentCellProtocol, in: NSRect, event: NSEvent, at: Int)](./nstextviewdelegate/textview%28_,draggedcell,in,event,at%29.md)
  Sent when the user attempts to drag a cell.
### Completing text
- [func textView(NSTextView, completions: [String], forPartialWordRange: NSRange, indexOfSelectedItem: UnsafeMutablePointer<Int>?) -> [String]](./nstextviewdelegate/textview%28_,completions,forpartialwordrange,indexofselecteditem%29.md)
  Returns the actual completions for a partial word.
### Displaying the sharing service picker
- [func textView(NSTextView, willShow: NSSharingServicePicker, forItems: [Any]) -> NSSharingServicePicker?](./nstextviewdelegate/textview%28_,willshow,foritems%29.md)
  Returns a sharing service picker for the current selection.
### Performing Commands
- [func textView(NSTextView, doCommandBy: Selector) -> Bool](./nstextviewdelegate/textview%28_,docommandby%29.md)
  Sent to allow the delegate to perform the command for the text view.
### Contextual Menu Management
- [func textView(NSTextView, menu: NSMenu, for: NSEvent, at: Int) -> NSMenu?](./nstextviewdelegate/textview%28_,menu,for,at%29.md)
  Allows delegate to control the context menu returned by the text view.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTextDelegate](./nstextdelegate.md)
### Conforming Types
- [NSOutlineView](./nsoutlineview.md)
- [NSTableView](./nstableview.md)

## See Also

### Text views
- [class NSTextField](./nstextfield.md)
  Text the user can select or edit to send an action message to a target when the user presses the Return key.
- [protocol NSTextFieldDelegate](./nstextfielddelegate.md)
  A protocol that a text field delegate can use to control its field editor action menu.
- [class NSTextView](./nstextview.md)
  A view that draws text and handles user interactions with that text.
- [protocol NSTextDelegate](./nstextdelegate.md)
  A set of optional methods implemented by the delegate of an [`NSText`](./nstext.md) object to edit text and change text formats.
- [class NSText](./nstext.md)
  The most general programmatic interface for objects that manage text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate)*