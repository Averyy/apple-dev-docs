# NSStandardKeyBindingResponding

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

Methods that responder subclasses implement to support key binding commands, such as inserting tabs and newlines, or moving the insertion point.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
protocol NSStandardKeyBindingResponding : NSObjectProtocol
```

```objc
@protocol NSStandardKeyBindingResponding <NSObject>
```

## Overview

[`NSResponder`](./nsresponder.md) doesn’t implement any of these methods. [`NSTextView`](./nstextview.md) implements a subset of them related to text editing. Your responder subclasses can implement any methods that make sense. You can create your own methods as well, but use these if the concepts map to functionality in your app. If your responder subclass is a view that’s key and uses key binding, and the user types a key sequence bound to a command not implemented in your class, nothing happens by default.

## Topics

### Responding to Key Commands
- [func doCommand(by: Selector)](./nsstandardkeybindingresponding/docommand%28by%29.md)
  Performs the given selector if possible.
### Inserting Content
- [func insertBacktab(Any?)](./nsstandardkeybindingresponding/insertbacktab%28_%29.md)
  Inserts a backtab character.
- [func insertContainerBreak(Any?)](./nsstandardkeybindingresponding/insertcontainerbreak%28_%29.md)
  Inserts a container break, such as a new page break.
- [func insertDoubleQuoteIgnoringSubstitution(Any?)](./nsstandardkeybindingresponding/insertdoublequoteignoringsubstitution%28_%29.md)
  Inserts a double quotation mark without substituting a curly quotation mark.
- [func insertLineBreak(Any?)](./nsstandardkeybindingresponding/insertlinebreak%28_%29.md)
  Inserts a line break character.
- [func insertNewline(Any?)](./nsstandardkeybindingresponding/insertnewline%28_%29.md)
  Inserts a newline character.
- [func insertNewlineIgnoringFieldEditor(Any?)](./nsstandardkeybindingresponding/insertnewlineignoringfieldeditor%28_%29.md)
  Inserts a newline character without invoking the field editor’s normal handling to end editing.
- [func insertParagraphSeparator(Any?)](./nsstandardkeybindingresponding/insertparagraphseparator%28_%29.md)
  Inserts a paragraph separator.
- [func insertSingleQuoteIgnoringSubstitution(Any?)](./nsstandardkeybindingresponding/insertsinglequoteignoringsubstitution%28_%29.md)
- [func insertTab(Any?)](./nsstandardkeybindingresponding/inserttab%28_%29.md)
  Inserts a tab character.
- [func insertTabIgnoringFieldEditor(Any?)](./nsstandardkeybindingresponding/inserttabignoringfieldeditor%28_%29.md)
- [func insertText(Any)](./nsstandardkeybindingresponding/inserttext%28_%29.md)
  Inserts the text you specify.
### Deleting Content
- [func deleteBackward(Any?)](./nsstandardkeybindingresponding/deletebackward%28_%29.md)
  Deletes content moving backward from the current insertion point.
- [func deleteBackwardByDecomposingPreviousCharacter(Any?)](./nsstandardkeybindingresponding/deletebackwardbydecomposingpreviouscharacter%28_%29.md)
- [func deleteForward(Any?)](./nsstandardkeybindingresponding/deleteforward%28_%29.md)
- [func deleteToBeginningOfLine(Any?)](./nsstandardkeybindingresponding/deletetobeginningofline%28_%29.md)
  Deletes content from the insertion point to the beginning of the current line.
- [func deleteToBeginningOfParagraph(Any?)](./nsstandardkeybindingresponding/deletetobeginningofparagraph%28_%29.md)
  Deletes content from the insertion point to the beginning of the current paragraph.
- [func deleteToEndOfLine(Any?)](./nsstandardkeybindingresponding/deletetoendofline%28_%29.md)
  Deletes content from the insertion point to the end of the current line.
- [func deleteToEndOfParagraph(Any?)](./nsstandardkeybindingresponding/deletetoendofparagraph%28_%29.md)
  Deletes content from the insertion point to the end of the current paragraph.
- [func deleteWordBackward(Any?)](./nsstandardkeybindingresponding/deletewordbackward%28_%29.md)
  Deletes the word preceding the current insertion point.
- [func deleteWordForward(Any?)](./nsstandardkeybindingresponding/deletewordforward%28_%29.md)
- [func yank(Any?)](./nsstandardkeybindingresponding/yank%28_%29.md)
  Deletes the current selection, placing it in a temporary buffer, such as the Clipboard.
### Moving the Insertion Pointer
- [func moveBackward(Any?)](./nsstandardkeybindingresponding/movebackward%28_%29.md)
  Moves the insertion pointer backward in the current content.
- [func moveDown(Any?)](./nsstandardkeybindingresponding/movedown%28_%29.md)
  Moves the insertion pointer down in the current content.
- [func moveForward(Any?)](./nsstandardkeybindingresponding/moveforward%28_%29.md)
  Moves the insertion pointer forward in the current content.
- [func moveLeft(Any?)](./nsstandardkeybindingresponding/moveleft%28_%29.md)
  Moves the insertion pointer left in the current content.
- [func moveRight(Any?)](./nsstandardkeybindingresponding/moveright%28_%29.md)
  Moves the insertion pointer right in the current content.
- [func moveUp(Any?)](./nsstandardkeybindingresponding/moveup%28_%29.md)
  Moves the insertion pointer up in the current content.
### Modifying the Selection
- [func moveBackwardAndModifySelection(Any?)](./nsstandardkeybindingresponding/movebackwardandmodifyselection%28_%29.md)
  Extends the selection to include the content before the current selection.
- [func moveDownAndModifySelection(Any?)](./nsstandardkeybindingresponding/movedownandmodifyselection%28_%29.md)
  Extends the selection to include the content below the current selection.
- [func moveForwardAndModifySelection(Any?)](./nsstandardkeybindingresponding/moveforwardandmodifyselection%28_%29.md)
  Extends the selection to include the content after the current selection.
- [func moveLeftAndModifySelection(Any?)](./nsstandardkeybindingresponding/moveleftandmodifyselection%28_%29.md)
  Extends the selection to include the content to the left of the current selection.
- [func moveRightAndModifySelection(Any?)](./nsstandardkeybindingresponding/moverightandmodifyselection%28_%29.md)
  Extends the selection to include the content to the right of the current selection.
- [func moveUpAndModifySelection(Any?)](./nsstandardkeybindingresponding/moveupandmodifyselection%28_%29.md)
  Extends the selection to include the content above the current selection.
### Scrolling Content
- [func scrollPageDown(Any?)](./nsstandardkeybindingresponding/scrollpagedown%28_%29.md)
  Scrolls the content down by a page.
- [func scrollPageUp(Any?)](./nsstandardkeybindingresponding/scrollpageup%28_%29.md)
  Scrolls the content up by a page.
- [func scrollLineDown(Any?)](./nsstandardkeybindingresponding/scrolllinedown%28_%29.md)
  Scrolls the content down by a line.
- [func scrollLineUp(Any?)](./nsstandardkeybindingresponding/scrolllineup%28_%29.md)
  Scrolls the content up by a line.
- [func scrollToBeginningOfDocument(Any?)](./nsstandardkeybindingresponding/scrolltobeginningofdocument%28_%29.md)
  Scrolls the content to the beginning of the document.
- [func scrollToEndOfDocument(Any?)](./nsstandardkeybindingresponding/scrolltoendofdocument%28_%29.md)
  Scrolls the content to the end of the document.
- [func pageDown(Any?)](./nsstandardkeybindingresponding/pagedown%28_%29.md)
  Moves the visible content region down by a page.
- [func pageUp(Any?)](./nsstandardkeybindingresponding/pageup%28_%29.md)
  Moves the visible content region up by a page.
- [func pageDownAndModifySelection(Any?)](./nsstandardkeybindingresponding/pagedownandmodifyselection%28_%29.md)
  Moves the visible content region down by a page, and extends the current selection.
- [func pageUpAndModifySelection(Any?)](./nsstandardkeybindingresponding/pageupandmodifyselection%28_%29.md)
  Moves the visible content region up by a page, and extends the current selection.
- [func centerSelectionInVisibleArea(Any?)](./nsstandardkeybindingresponding/centerselectioninvisiblearea%28_%29.md)
  Moves the visible content region so the current selection is visually centered.
### Transposing Elements
- [func transpose(Any?)](./nsstandardkeybindingresponding/transpose%28_%29.md)
  Transposes the content around the current selection.
- [func transposeWords(Any?)](./nsstandardkeybindingresponding/transposewords%28_%29.md)
  Transposes the words around the current selection.
### Indenting Content
- [func indent(Any?)](./nsstandardkeybindingresponding/indent%28_%29.md)
  Indents the content at the current selection.
### Canceling Operations
- [func cancelOperation(Any?)](./nsstandardkeybindingresponding/canceloperation%28_%29.md)
  Cancels the current operation.
### Supporting QuickLook
- [func quickLookPreviewItems(Any?)](./nsstandardkeybindingresponding/quicklookpreviewitems%28_%29.md)
  Invokes QuickLook to preview the current selection.
### Supporting Writing Directions
- [func makeBaseWritingDirectionLeftToRight(Any?)](./nsstandardkeybindingresponding/makebasewritingdirectionlefttoright%28_%29.md)
- [func makeBaseWritingDirectionNatural(Any?)](./nsstandardkeybindingresponding/makebasewritingdirectionnatural%28_%29.md)
- [func makeBaseWritingDirectionRightToLeft(Any?)](./nsstandardkeybindingresponding/makebasewritingdirectionrighttoleft%28_%29.md)
- [func makeTextWritingDirectionLeftToRight(Any?)](./nsstandardkeybindingresponding/maketextwritingdirectionlefttoright%28_%29.md)
- [func makeTextWritingDirectionNatural(Any?)](./nsstandardkeybindingresponding/maketextwritingdirectionnatural%28_%29.md)
- [func makeTextWritingDirectionRightToLeft(Any?)](./nsstandardkeybindingresponding/maketextwritingdirectionrighttoleft%28_%29.md)
### Changing Capitalization
- [func capitalizeWord(Any?)](./nsstandardkeybindingresponding/capitalizeword%28_%29.md)
- [func changeCaseOfLetter(Any?)](./nsstandardkeybindingresponding/changecaseofletter%28_%29.md)
- [func lowercaseWord(Any?)](./nsstandardkeybindingresponding/lowercaseword%28_%29.md)
- [func uppercaseWord(Any?)](./nsstandardkeybindingresponding/uppercaseword%28_%29.md)
### Moving the Selection in Documents
- [func moveToBeginningOfDocument(Any?)](./nsstandardkeybindingresponding/movetobeginningofdocument%28_%29.md)
- [func moveToBeginningOfDocumentAndModifySelection(Any?)](./nsstandardkeybindingresponding/movetobeginningofdocumentandmodifyselection%28_%29.md)
- [func moveToEndOfDocument(Any?)](./nsstandardkeybindingresponding/movetoendofdocument%28_%29.md)
- [func moveToEndOfDocumentAndModifySelection(Any?)](./nsstandardkeybindingresponding/movetoendofdocumentandmodifyselection%28_%29.md)
### Moving the Selection in Paragraphs
- [func moveParagraphBackwardAndModifySelection(Any?)](./nsstandardkeybindingresponding/moveparagraphbackwardandmodifyselection%28_%29.md)
- [func moveParagraphForwardAndModifySelection(Any?)](./nsstandardkeybindingresponding/moveparagraphforwardandmodifyselection%28_%29.md)
- [func moveToBeginningOfParagraph(Any?)](./nsstandardkeybindingresponding/movetobeginningofparagraph%28_%29.md)
- [func moveToBeginningOfParagraphAndModifySelection(Any?)](./nsstandardkeybindingresponding/movetobeginningofparagraphandmodifyselection%28_%29.md)
- [func moveToEndOfParagraph(Any?)](./nsstandardkeybindingresponding/movetoendofparagraph%28_%29.md)
- [func moveToEndOfParagraphAndModifySelection(Any?)](./nsstandardkeybindingresponding/movetoendofparagraphandmodifyselection%28_%29.md)
### Moving the Selection in Lines of Text
- [func moveToBeginningOfLine(Any?)](./nsstandardkeybindingresponding/movetobeginningofline%28_%29.md)
- [func moveToBeginningOfLineAndModifySelection(Any?)](./nsstandardkeybindingresponding/movetobeginningoflineandmodifyselection%28_%29.md)
- [func moveToEndOfLine(Any?)](./nsstandardkeybindingresponding/movetoendofline%28_%29.md)
- [func moveToEndOfLineAndModifySelection(Any?)](./nsstandardkeybindingresponding/movetoendoflineandmodifyselection%28_%29.md)
- [func moveToLeftEndOfLine(Any?)](./nsstandardkeybindingresponding/movetoleftendofline%28_%29.md)
- [func moveToLeftEndOfLineAndModifySelection(Any?)](./nsstandardkeybindingresponding/movetoleftendoflineandmodifyselection%28_%29.md)
- [func moveToRightEndOfLine(Any?)](./nsstandardkeybindingresponding/movetorightendofline%28_%29.md)
- [func moveToRightEndOfLineAndModifySelection(Any?)](./nsstandardkeybindingresponding/movetorightendoflineandmodifyselection%28_%29.md)
### Changing the Selection
- [func selectAll(Any?)](./nsstandardkeybindingresponding/selectall%28_%29.md)
- [func selectLine(Any?)](./nsstandardkeybindingresponding/selectline%28_%29.md)
- [func selectParagraph(Any?)](./nsstandardkeybindingresponding/selectparagraph%28_%29.md)
- [func selectWord(Any?)](./nsstandardkeybindingresponding/selectword%28_%29.md)
### Supporting Marked Selections
- [func setMark(Any?)](./nsstandardkeybindingresponding/setmark%28_%29.md)
- [func selectToMark(Any?)](./nsstandardkeybindingresponding/selecttomark%28_%29.md)
- [func deleteToMark(Any?)](./nsstandardkeybindingresponding/deletetomark%28_%29.md)
- [func swapWithMark(Any?)](./nsstandardkeybindingresponding/swapwithmark%28_%29.md)
### Supporting Autocomplete
- [func complete(Any?)](./nsstandardkeybindingresponding/complete%28_%29.md)
### Moving the Selection by Word Boundaries
- [func moveWordBackward(Any?)](./nsstandardkeybindingresponding/movewordbackward%28_%29.md)
- [func moveWordBackwardAndModifySelection(Any?)](./nsstandardkeybindingresponding/movewordbackwardandmodifyselection%28_%29.md)
- [func moveWordForward(Any?)](./nsstandardkeybindingresponding/movewordforward%28_%29.md)
- [func moveWordForwardAndModifySelection(Any?)](./nsstandardkeybindingresponding/movewordforwardandmodifyselection%28_%29.md)
- [func moveWordLeft(Any?)](./nsstandardkeybindingresponding/movewordleft%28_%29.md)
- [func moveWordLeftAndModifySelection(Any?)](./nsstandardkeybindingresponding/movewordleftandmodifyselection%28_%29.md)
- [func moveWordRight(Any?)](./nsstandardkeybindingresponding/movewordright%28_%29.md)
- [func moveWordRightAndModifySelection(Any?)](./nsstandardkeybindingresponding/movewordrightandmodifyselection%28_%29.md)
### Instance Methods
- [func showContextMenuForSelection(Any?)](./nsstandardkeybindingresponding/showcontextmenuforselection%28_%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [NSApplication](./nsapplication.md)
- [NSBackgroundExtensionView](./nsbackgroundextensionview.md)
- [NSBox](./nsbox.md)
- [NSBrowser](./nsbrowser.md)
- [NSButton](./nsbutton.md)
- [NSClipView](./nsclipview.md)
- [NSCollectionView](./nscollectionview.md)
- [NSCollectionViewItem](./nscollectionviewitem.md)
- [NSColorPanel](./nscolorpanel.md)
- [NSColorWell](./nscolorwell.md)
- [NSComboBox](./nscombobox.md)
- [NSComboButton](./nscombobutton.md)
- [NSControl](./nscontrol.md)
- [NSDatePicker](./nsdatepicker.md)
- [NSDrawer](./nsdrawer.md)
- [NSFontPanel](./nsfontpanel.md)
- [NSForm](./nsform.md)
- [NSGlassEffectContainerView](./nsglasseffectcontainerview.md)
- [NSGlassEffectView](./nsglasseffectview.md)
- [NSGridView](./nsgridview.md)
- [NSImageView](./nsimageview.md)
- [NSLevelIndicator](./nslevelindicator.md)
- [NSMatrix](./nsmatrix.md)
- [NSOpenGLView](./nsopenglview.md)
- [NSOpenPanel](./nsopenpanel.md)
- [NSOutlineView](./nsoutlineview.md)
- [NSPageController](./nspagecontroller.md)
- [NSPanel](./nspanel.md)
- [NSPathControl](./nspathcontrol.md)
- [NSPopUpButton](./nspopupbutton.md)
- [NSPopover](./nspopover.md)
- [NSPredicateEditor](./nspredicateeditor.md)
- [NSProgressIndicator](./nsprogressindicator.md)
- [NSResponder](./nsresponder.md)
- [NSRuleEditor](./nsruleeditor.md)
- [NSRulerView](./nsrulerview.md)
- [NSSavePanel](./nssavepanel.md)
- [NSScrollView](./nsscrollview.md)
- [NSScroller](./nsscroller.md)
- [NSScrubber](./nsscrubber.md)
- [NSScrubberArrangedView](./nsscrubberarrangedview.md)
- [NSScrubberImageItemView](./nsscrubberimageitemview.md)
- [NSScrubberItemView](./nsscrubberitemview.md)
- [NSScrubberSelectionView](./nsscrubberselectionview.md)
- [NSScrubberTextItemView](./nsscrubbertextitemview.md)
- [NSSearchField](./nssearchfield.md)
- [NSSecureTextField](./nssecuretextfield.md)
- [NSSegmentedControl](./nssegmentedcontrol.md)
- [NSSlider](./nsslider.md)
- [NSSplitView](./nssplitview.md)
- [NSSplitViewController](./nssplitviewcontroller.md)
- [NSSplitViewItemAccessoryViewController](./nssplitviewitemaccessoryviewcontroller.md)
- [NSStackView](./nsstackview.md)
- [NSStatusBarButton](./nsstatusbarbutton.md)
- [NSStepper](./nsstepper.md)
- [NSSwitch](./nsswitch.md)
- [NSTabView](./nstabview.md)
- [NSTabViewController](./nstabviewcontroller.md)
- [NSTableCellView](./nstablecellview.md)
- [NSTableHeaderView](./nstableheaderview.md)
- [NSTableRowView](./nstablerowview.md)
- [NSTableView](./nstableview.md)
- [NSText](./nstext.md)
- [NSTextField](./nstextfield.md)
- [NSTextInsertionIndicator](./nstextinsertionindicator.md)
- [NSTextView](./nstextview.md)
- [NSTitlebarAccessoryViewController](./nstitlebaraccessoryviewcontroller.md)
- [NSTokenField](./nstokenfield.md)
- [NSView](./nsview.md)
- [NSViewController](./nsviewcontroller.md)
- [NSVisualEffectView](./nsvisualeffectview.md)
- [NSWindow](./nswindow.md)
- [NSWindowController](./nswindowcontroller.md)

## See Also

### Responding to Action Messages
- [func supplementalTarget(forAction: Selector, sender: Any?) -> Any?](./nsresponder/supplementaltarget%28foraction,sender%29.md)
  Finds a target for an action method.
- [Action Messages](./action-messages.md)
  Implement action messages in your first responders to handle common tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstandardkeybindingresponding)*