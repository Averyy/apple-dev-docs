# NSStandardKeyBindingResponding

**Framework**: AppKit  
**Kind**: protocol

Methods that responder subclasses implement to support key binding commands, such as inserting tabs and newlines, or moving the insertion point.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
protocol NSStandardKeyBindingResponding : NSObjectProtocol
```

#### Overview

[`NSResponder`](nsresponder.md) doesn’t implement any of these methods. [`NSTextView`](nstextview.md) implements a subset of them related to text editing. Your responder subclasses can implement any methods that make sense. You can create your own methods as well, but use these if the concepts map to functionality in your app. If your responder subclass is a view that’s key and uses key binding, and the user types a key sequence bound to a command not implemented in your class, nothing happens by default.

## Topics

### Responding to Key Commands
- [func doCommand(by: Selector)](nsstandardkeybindingresponding/docommand(by:).md)
  Performs the given selector if possible.
### Inserting Content
- [func insertBacktab(Any?)](nsstandardkeybindingresponding/insertbacktab(_:).md)
  Inserts a backtab character.
- [func insertContainerBreak(Any?)](nsstandardkeybindingresponding/insertcontainerbreak(_:).md)
  Inserts a container break, such as a new page break.
- [func insertDoubleQuoteIgnoringSubstitution(Any?)](nsstandardkeybindingresponding/insertdoublequoteignoringsubstitution(_:).md)
  Inserts a double quotation mark without substituting a curly quotation mark.
- [func insertLineBreak(Any?)](nsstandardkeybindingresponding/insertlinebreak(_:).md)
  Inserts a line break character.
- [func insertNewline(Any?)](nsstandardkeybindingresponding/insertnewline(_:).md)
  Inserts a newline character.
- [func insertNewlineIgnoringFieldEditor(Any?)](nsstandardkeybindingresponding/insertnewlineignoringfieldeditor(_:).md)
  Inserts a newline character without invoking the field editor’s normal handling to end editing.
- [func insertParagraphSeparator(Any?)](nsstandardkeybindingresponding/insertparagraphseparator(_:).md)
  Inserts a paragraph separator.
- [func insertSingleQuoteIgnoringSubstitution(Any?)](nsstandardkeybindingresponding/insertsinglequoteignoringsubstitution(_:).md)
- [func insertTab(Any?)](nsstandardkeybindingresponding/inserttab(_:).md)
  Inserts a tab character.
- [func insertTabIgnoringFieldEditor(Any?)](nsstandardkeybindingresponding/inserttabignoringfieldeditor(_:).md)
- [func insertText(Any)](nsstandardkeybindingresponding/inserttext(_:).md)
  Inserts the text you specify.
### Deleting Content
- [func deleteBackward(Any?)](nsstandardkeybindingresponding/deletebackward(_:).md)
  Deletes content moving backward from the current insertion point.
- [func deleteBackwardByDecomposingPreviousCharacter(Any?)](nsstandardkeybindingresponding/deletebackwardbydecomposingpreviouscharacter(_:).md)
- [func deleteForward(Any?)](nsstandardkeybindingresponding/deleteforward(_:).md)
- [func deleteToBeginningOfLine(Any?)](nsstandardkeybindingresponding/deletetobeginningofline(_:).md)
  Deletes content from the insertion point to the beginning of the current line.
- [func deleteToBeginningOfParagraph(Any?)](nsstandardkeybindingresponding/deletetobeginningofparagraph(_:).md)
  Deletes content from the insertion point to the beginning of the current paragraph.
- [func deleteToEndOfLine(Any?)](nsstandardkeybindingresponding/deletetoendofline(_:).md)
  Deletes content from the insertion point to the end of the current line.
- [func deleteToEndOfParagraph(Any?)](nsstandardkeybindingresponding/deletetoendofparagraph(_:).md)
  Deletes content from the insertion point to the end of the current paragraph.
- [func deleteWordBackward(Any?)](nsstandardkeybindingresponding/deletewordbackward(_:).md)
  Deletes the word preceding the current insertion point.
- [func deleteWordForward(Any?)](nsstandardkeybindingresponding/deletewordforward(_:).md)
- [func yank(Any?)](nsstandardkeybindingresponding/yank(_:).md)
  Deletes the current selection, placing it in a temporary buffer, such as the Clipboard.
### Moving the Insertion Pointer
- [func moveBackward(Any?)](nsstandardkeybindingresponding/movebackward(_:).md)
  Moves the insertion pointer backward in the current content.
- [func moveDown(Any?)](nsstandardkeybindingresponding/movedown(_:).md)
  Moves the insertion pointer down in the current content.
- [func moveForward(Any?)](nsstandardkeybindingresponding/moveforward(_:).md)
  Moves the insertion pointer forward in the current content.
- [func moveLeft(Any?)](nsstandardkeybindingresponding/moveleft(_:).md)
  Moves the insertion pointer left in the current content.
- [func moveRight(Any?)](nsstandardkeybindingresponding/moveright(_:).md)
  Moves the insertion pointer right in the current content.
- [func moveUp(Any?)](nsstandardkeybindingresponding/moveup(_:).md)
  Moves the insertion pointer up in the current content.
### Modifying the Selection
- [func moveBackwardAndModifySelection(Any?)](nsstandardkeybindingresponding/movebackwardandmodifyselection(_:).md)
  Extends the selection to include the content before the current selection.
- [func moveDownAndModifySelection(Any?)](nsstandardkeybindingresponding/movedownandmodifyselection(_:).md)
  Extends the selection to include the content below the current selection.
- [func moveForwardAndModifySelection(Any?)](nsstandardkeybindingresponding/moveforwardandmodifyselection(_:).md)
  Extends the selection to include the content after the current selection.
- [func moveLeftAndModifySelection(Any?)](nsstandardkeybindingresponding/moveleftandmodifyselection(_:).md)
  Extends the selection to include the content to the left of the current selection.
- [func moveRightAndModifySelection(Any?)](nsstandardkeybindingresponding/moverightandmodifyselection(_:).md)
  Extends the selection to include the content to the right of the current selection.
- [func moveUpAndModifySelection(Any?)](nsstandardkeybindingresponding/moveupandmodifyselection(_:).md)
  Extends the selection to include the content above the current selection.
### Scrolling Content
- [func scrollPageDown(Any?)](nsstandardkeybindingresponding/scrollpagedown(_:).md)
  Scrolls the content down by a page.
- [func scrollPageUp(Any?)](nsstandardkeybindingresponding/scrollpageup(_:).md)
  Scrolls the content up by a page.
- [func scrollLineDown(Any?)](nsstandardkeybindingresponding/scrolllinedown(_:).md)
  Scrolls the content down by a line.
- [func scrollLineUp(Any?)](nsstandardkeybindingresponding/scrolllineup(_:).md)
  Scrolls the content up by a line.
- [func scrollToBeginningOfDocument(Any?)](nsstandardkeybindingresponding/scrolltobeginningofdocument(_:).md)
  Scrolls the content to the beginning of the document.
- [func scrollToEndOfDocument(Any?)](nsstandardkeybindingresponding/scrolltoendofdocument(_:).md)
  Scrolls the content to the end of the document.
- [func pageDown(Any?)](nsstandardkeybindingresponding/pagedown(_:).md)
  Moves the visible content region down by a page.
- [func pageUp(Any?)](nsstandardkeybindingresponding/pageup(_:).md)
  Moves the visible content region up by a page.
- [func pageDownAndModifySelection(Any?)](nsstandardkeybindingresponding/pagedownandmodifyselection(_:).md)
  Moves the visible content region down by a page, and extends the current selection.
- [func pageUpAndModifySelection(Any?)](nsstandardkeybindingresponding/pageupandmodifyselection(_:).md)
  Moves the visible content region up by a page, and extends the current selection.
- [func centerSelectionInVisibleArea(Any?)](nsstandardkeybindingresponding/centerselectioninvisiblearea(_:).md)
  Moves the visible content region so the current selection is visually centered.
### Transposing Elements
- [func transpose(Any?)](nsstandardkeybindingresponding/transpose(_:).md)
  Transposes the content around the current selection.
- [func transposeWords(Any?)](nsstandardkeybindingresponding/transposewords(_:).md)
  Transposes the words around the current selection.
### Indenting Content
- [func indent(Any?)](nsstandardkeybindingresponding/indent(_:).md)
  Indents the content at the current selection.
### Canceling Operations
- [func cancelOperation(Any?)](nsstandardkeybindingresponding/canceloperation(_:).md)
  Cancels the current operation.
### Supporting QuickLook
- [func quickLookPreviewItems(Any?)](nsstandardkeybindingresponding/quicklookpreviewitems(_:).md)
  Invokes QuickLook to preview the current selection.
### Supporting Writing Directions
- [func makeBaseWritingDirectionLeftToRight(Any?)](nsstandardkeybindingresponding/makebasewritingdirectionlefttoright(_:).md)
- [func makeBaseWritingDirectionNatural(Any?)](nsstandardkeybindingresponding/makebasewritingdirectionnatural(_:).md)
- [func makeBaseWritingDirectionRightToLeft(Any?)](nsstandardkeybindingresponding/makebasewritingdirectionrighttoleft(_:).md)
- [func makeTextWritingDirectionLeftToRight(Any?)](nsstandardkeybindingresponding/maketextwritingdirectionlefttoright(_:).md)
- [func makeTextWritingDirectionNatural(Any?)](nsstandardkeybindingresponding/maketextwritingdirectionnatural(_:).md)
- [func makeTextWritingDirectionRightToLeft(Any?)](nsstandardkeybindingresponding/maketextwritingdirectionrighttoleft(_:).md)
### Changing Capitalization
- [func capitalizeWord(Any?)](nsstandardkeybindingresponding/capitalizeword(_:).md)
- [func changeCaseOfLetter(Any?)](nsstandardkeybindingresponding/changecaseofletter(_:).md)
- [func lowercaseWord(Any?)](nsstandardkeybindingresponding/lowercaseword(_:).md)
- [func uppercaseWord(Any?)](nsstandardkeybindingresponding/uppercaseword(_:).md)
### Moving the Selection in Documents
- [func moveToBeginningOfDocument(Any?)](nsstandardkeybindingresponding/movetobeginningofdocument(_:).md)
- [func moveToBeginningOfDocumentAndModifySelection(Any?)](nsstandardkeybindingresponding/movetobeginningofdocumentandmodifyselection(_:).md)
- [func moveToEndOfDocument(Any?)](nsstandardkeybindingresponding/movetoendofdocument(_:).md)
- [func moveToEndOfDocumentAndModifySelection(Any?)](nsstandardkeybindingresponding/movetoendofdocumentandmodifyselection(_:).md)
### Moving the Selection in Paragraphs
- [func moveParagraphBackwardAndModifySelection(Any?)](nsstandardkeybindingresponding/moveparagraphbackwardandmodifyselection(_:).md)
- [func moveParagraphForwardAndModifySelection(Any?)](nsstandardkeybindingresponding/moveparagraphforwardandmodifyselection(_:).md)
- [func moveToBeginningOfParagraph(Any?)](nsstandardkeybindingresponding/movetobeginningofparagraph(_:).md)
- [func moveToBeginningOfParagraphAndModifySelection(Any?)](nsstandardkeybindingresponding/movetobeginningofparagraphandmodifyselection(_:).md)
- [func moveToEndOfParagraph(Any?)](nsstandardkeybindingresponding/movetoendofparagraph(_:).md)
- [func moveToEndOfParagraphAndModifySelection(Any?)](nsstandardkeybindingresponding/movetoendofparagraphandmodifyselection(_:).md)
### Moving the Selection in Lines of Text
- [func moveToBeginningOfLine(Any?)](nsstandardkeybindingresponding/movetobeginningofline(_:).md)
- [func moveToBeginningOfLineAndModifySelection(Any?)](nsstandardkeybindingresponding/movetobeginningoflineandmodifyselection(_:).md)
- [func moveToEndOfLine(Any?)](nsstandardkeybindingresponding/movetoendofline(_:).md)
- [func moveToEndOfLineAndModifySelection(Any?)](nsstandardkeybindingresponding/movetoendoflineandmodifyselection(_:).md)
- [func moveToLeftEndOfLine(Any?)](nsstandardkeybindingresponding/movetoleftendofline(_:).md)
- [func moveToLeftEndOfLineAndModifySelection(Any?)](nsstandardkeybindingresponding/movetoleftendoflineandmodifyselection(_:).md)
- [func moveToRightEndOfLine(Any?)](nsstandardkeybindingresponding/movetorightendofline(_:).md)
- [func moveToRightEndOfLineAndModifySelection(Any?)](nsstandardkeybindingresponding/movetorightendoflineandmodifyselection(_:).md)
### Changing the Selection
- [func selectAll(Any?)](nsstandardkeybindingresponding/selectall(_:).md)
- [func selectLine(Any?)](nsstandardkeybindingresponding/selectline(_:).md)
- [func selectParagraph(Any?)](nsstandardkeybindingresponding/selectparagraph(_:).md)
- [func selectWord(Any?)](nsstandardkeybindingresponding/selectword(_:).md)
### Supporting Marked Selections
- [func setMark(Any?)](nsstandardkeybindingresponding/setmark(_:).md)
- [func selectToMark(Any?)](nsstandardkeybindingresponding/selecttomark(_:).md)
- [func deleteToMark(Any?)](nsstandardkeybindingresponding/deletetomark(_:).md)
- [func swapWithMark(Any?)](nsstandardkeybindingresponding/swapwithmark(_:).md)
### Supporting Autocomplete
- [func complete(Any?)](nsstandardkeybindingresponding/complete(_:).md)
### Moving the Selection by Word Boundaries
- [func moveWordBackward(Any?)](nsstandardkeybindingresponding/movewordbackward(_:).md)
- [func moveWordBackwardAndModifySelection(Any?)](nsstandardkeybindingresponding/movewordbackwardandmodifyselection(_:).md)
- [func moveWordForward(Any?)](nsstandardkeybindingresponding/movewordforward(_:).md)
- [func moveWordForwardAndModifySelection(Any?)](nsstandardkeybindingresponding/movewordforwardandmodifyselection(_:).md)
- [func moveWordLeft(Any?)](nsstandardkeybindingresponding/movewordleft(_:).md)
- [func moveWordLeftAndModifySelection(Any?)](nsstandardkeybindingresponding/movewordleftandmodifyselection(_:).md)
- [func moveWordRight(Any?)](nsstandardkeybindingresponding/movewordright(_:).md)
- [func moveWordRightAndModifySelection(Any?)](nsstandardkeybindingresponding/movewordrightandmodifyselection(_:).md)
### Instance Methods
- [func showContextMenuForSelection(Any?)](nsstandardkeybindingresponding/showcontextmenuforselection(_:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSApplication](nsapplication.md)
- [NSBackgroundExtensionView](nsbackgroundextensionview.md)
- [NSBox](nsbox.md)
- [NSBrowser](nsbrowser.md)
- [NSButton](nsbutton.md)
- [NSClipView](nsclipview.md)
- [NSCollectionView](nscollectionview.md)
- [NSCollectionViewItem](nscollectionviewitem.md)
- [NSColorPanel](nscolorpanel.md)
- [NSColorWell](nscolorwell.md)
- [NSComboBox](nscombobox.md)
- [NSComboButton](nscombobutton.md)
- [NSControl](nscontrol.md)
- [NSDatePicker](nsdatepicker.md)
- [NSDrawer](nsdrawer.md)
- [NSFontPanel](nsfontpanel.md)
- [NSForm](nsform.md)
- [NSGlassEffectContainerView](nsglasseffectcontainerview.md)
- [NSGlassEffectView](nsglasseffectview.md)
- [NSGridView](nsgridview.md)
- [NSImageView](nsimageview.md)
- [NSLevelIndicator](nslevelindicator.md)
- [NSMatrix](nsmatrix.md)
- [NSOpenGLView](nsopenglview.md)
- [NSOpenPanel](nsopenpanel.md)
- [NSOutlineView](nsoutlineview.md)
- [NSPageController](nspagecontroller.md)
- [NSPanel](nspanel.md)
- [NSPathControl](nspathcontrol.md)
- [NSPopUpButton](nspopupbutton.md)
- [NSPopover](nspopover.md)
- [NSPredicateEditor](nspredicateeditor.md)
- [NSProgressIndicator](nsprogressindicator.md)
- [NSResponder](nsresponder.md)
- [NSRuleEditor](nsruleeditor.md)
- [NSRulerView](nsrulerview.md)
- [NSSavePanel](nssavepanel.md)
- [NSScrollView](nsscrollview.md)
- [NSScroller](nsscroller.md)
- [NSScrubber](nsscrubber.md)
- [NSScrubberArrangedView](nsscrubberarrangedview.md)
- [NSScrubberImageItemView](nsscrubberimageitemview.md)
- [NSScrubberItemView](nsscrubberitemview.md)
- [NSScrubberSelectionView](nsscrubberselectionview.md)
- [NSScrubberTextItemView](nsscrubbertextitemview.md)
- [NSSearchField](nssearchfield.md)
- [NSSecureTextField](nssecuretextfield.md)
- [NSSegmentedControl](nssegmentedcontrol.md)
- [NSSlider](nsslider.md)
- [NSSplitView](nssplitview.md)
- [NSSplitViewController](nssplitviewcontroller.md)
- [NSSplitViewItemAccessoryViewController](nssplitviewitemaccessoryviewcontroller.md)
- [NSStackView](nsstackview.md)
- [NSStatusBarButton](nsstatusbarbutton.md)
- [NSStepper](nsstepper.md)
- [NSSwitch](nsswitch.md)
- [NSTabView](nstabview.md)
- [NSTabViewController](nstabviewcontroller.md)
- [NSTableCellView](nstablecellview.md)
- [NSTableHeaderView](nstableheaderview.md)
- [NSTableRowView](nstablerowview.md)
- [NSTableView](nstableview.md)
- [NSText](nstext.md)
- [NSTextField](nstextfield.md)
- [NSTextInsertionIndicator](nstextinsertionindicator.md)
- [NSTextView](nstextview.md)
- [NSTitlebarAccessoryViewController](nstitlebaraccessoryviewcontroller.md)
- [NSTokenField](nstokenfield.md)
- [NSView](nsview.md)
- [NSViewController](nsviewcontroller.md)
- [NSVisualEffectView](nsvisualeffectview.md)
- [NSWindow](nswindow.md)
- [NSWindowController](nswindowcontroller.md)

## See Also

- [func supplementalTarget(forAction: Selector, sender: Any?) -> Any?](nsresponder/supplementaltarget(foraction:sender:).md)
  Finds a target for an action method.
- [Action Messages](action-messages.md)
  Implement action messages in your first responders to handle common tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstandardkeybindingresponding)*