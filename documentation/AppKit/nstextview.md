# NSTextView

**Framework**: AppKit  
**Kind**: class

A view that draws text and handles user interactions with that text.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSTextView
```

## Mentions

- [Customizing Writing Tools behavior for AppKit views](customizing-writing-tools-behavior-for-system-views.md)
- [Supporting Writing Tools via the pasteboard](supporting-writing-tools-via-the-pasteboard.md)
- [Adding Writing Tools support to a custom AppKit view](adding-writing-tools-support-to-a-custom-nsview.md)
- [Adopting the system text cursor in custom text views](adopting-the-system-text-cursor-in-custom-text-views.md)

#### Overview

The [`NSTextView`](nstextview.md) class is the front-end class to the AppKit text system. The class draws the text managed by the back-end components and handles user events to select and modify its text, in addition to supporting rich text, attachments, input management, and key binding, and marked text attributes.

> **Note**:  If you need only to implement a simple editable text field, see [`NSTextField`](nstextfield.md).

[`NSTextView`](nstextview.md) is the principal means to obtain a text object that caters to almost all needs for displaying and managing text at the user interface level. While [`NSTextView`](nstextview.md) is a subclass of the [`NSText`](nstext.md) class — which declares the most general Cocoa interface to the text system — [`NSTextView`](nstextview.md) adds major features beyond the capabilities of [`NSText`](nstext.md). You can also do more powerful and more creative text manipulation (such as displaying text in a circle) using [`NSTextStorage`](nstextstorage.md), [`NSTextLayoutManager`](nstextlayoutmanager.md), [`NSTextContainer`](nstextcontainer.md), and related classes.

You’re more likely to use the [`NSTextView`](nstextview.md) class than [`NSText`](nstext.md). It’s also important to remember that [`NSTextView`](nstextview.md) conforms to a large number of protocols, the methods of which are available to instances of the [`NSTextView`](nstextview.md) class.

[`NSTextView`](nstextview.md) communicates with its delegate through methods declared both by the [`NSTextViewDelegate`](nstextviewdelegate.md) and by its superclass’s protocol, [`NSTextDelegate`](nstextdelegate.md). All delegation messages come from the first text view.

In macOS 12 and later, if you explicitly call the `layoutManager` property on a text view or text container, the framework reverts to a compatibility mode that uses [`NSLayoutManager`](nslayoutmanager.md). The text view also switches to this compatibility mode when it encounters text content that’s not yet supported, such as [`NSTextTable`](nstexttable.md).

##### About Delegate Methods

The `NSTextView` class communicates with its delegate through methods declared both by the [`NSTextViewDelegate`](nstextviewdelegate.md) and by its superclass’s protocol, [`NSTextDelegate`](nstextdelegate.md). All delegation messages come from the first text view.

##### Becoming the First Responder

When the system invokes [`becomeFirstResponder()`](nsresponder/becomefirstresponder().md) on a text view, if the previous first responder was not a text view on the same layout manager as the receiving text view, the receiving text view draws the selection and updates the insertion point if necessary.

To make a text view the first responder, call the containing window’s [`makeFirstResponder(_:)`](nswindow/makefirstresponder(_:).md) method. Never invoke a text view’s [`becomeFirstResponder()`](nsresponder/becomefirstresponder().md) method directly.

##### Resigning As First Responder

When the system invokes [`resignFirstResponder()`](nsresponder/resignfirstresponder().md) on a text view, if the object that will become the new first responder is a text view attached to the same layout manager as the receiver, the receiving text view returns [`true`](https://developer.apple.com/documentation/Swift/true) with no further action. Otherwise, it sends a [`textShouldEndEditing(_:)`](nstextdelegate/textshouldendediting(_:).md) message to its delegate (if any). If the delegate returns [`false`](https://developer.apple.com/documentation/Swift/false), the text view returns [`false`](https://developer.apple.com/documentation/Swift/false). If the delegate returns [`true`](https://developer.apple.com/documentation/Swift/true), the text view hides the selection highlighting and posts an [`didEndEditingNotification`](nstext/didendeditingnotification.md) to the default notification center and then returns [`true`](https://developer.apple.com/documentation/Swift/true).

## Topics

### Creating a text view
- [init(frame: NSRect, textContainer: NSTextContainer?)](nstextview/init(frame:textcontainer:).md)
  Initializes a text view.
- [init(frame: NSRect)](nstextview/init(frame:).md)
  Initializes a text view.
- [convenience init(usingTextLayoutManager: Bool)](nstextview/init(usingtextlayoutmanager:).md)
- [init?(coder: NSCoder)](nstextview/init(coder:).md)
  Initializes a text view with data in an unarchiver.
### Managing the text view’s content
- [var delegate: (any NSTextViewDelegate)?](nstextview/delegate.md)
  The delegate for all text views sharing the receiver’s layout manager.
- [protocol NSTextViewDelegate](nstextviewdelegate.md)
  A set of optional methods that text view delegates can use to manage selection, set text attributes, work with the spell checker, and more.
### Registering services information
- [class func registerForServices()](nstextview/registerforservices.md)
  Registers send and return types for the Services facility.
### Accessing text system objects
- [class var stronglyReferencesTextStorage: Bool](nstextview/stronglyreferencestextstorage.md)
- [class func fieldEditor() -> Self](nstextview/fieldeditor.md)
- [var textContainer: NSTextContainer?](nstextview/textcontainer.md)
  The receiver’s text container.
- [func replaceTextContainer(NSTextContainer)](nstextview/replacetextcontainer(_:).md)
  Replaces the text container for the group of text system objects containing the receiver, keeping the association between the receiver and its layout manager intact.
- [var textContainerInset: NSSize](nstextview/textcontainerinset.md)
  The empty space the receiver leaves around its associated text container.
- [var textContainerOrigin: NSPoint](nstextview/textcontainerorigin.md)
  The origin of the receiver’s text container.
- [func invalidateTextContainerOrigin()](nstextview/invalidatetextcontainerorigin.md)
  Invalidates the calculated origin of the text container.
- [var textLayoutManager: NSTextLayoutManager?](nstextview/textlayoutmanager.md)
  The manager that lays out text for the receiver’s text container.
- [var layoutManager: NSLayoutManager?](nstextview/layoutmanager.md)
  The layout manager that lays out text for the receiver’s text container.
- [var textContentStorage: NSTextContentStorage?](nstextview/textcontentstorage.md)
  The receiver’s text storage object.
- [var textStorage: NSTextStorage?](nstextview/textstorage.md)
  The receiver’s text storage object.
### Setting graphics attributes
- [var backgroundColor: NSColor](nstextview/backgroundcolor.md)
  The receiver’s background color.
- [var drawsBackground: Bool](nstextview/drawsbackground.md)
  A Boolean value that indicates whether the receiver draws its background.
- [var allowsDocumentBackgroundColorChange: Bool](nstextview/allowsdocumentbackgroundcolorchange.md)
  A Boolean value that indicates whether the receiver allows its background color to change.
- [func changeDocumentBackgroundColor(Any?)](nstextview/changedocumentbackgroundcolor(_:).md)
  An action method used to set the background color.
### Controlling text display
- [func setNeedsDisplay(NSRect, avoidAdditionalLayout: Bool)](nstextview/setneedsdisplay(_:avoidadditionallayout:).md)
  Marks the receiver as requiring display.
- [var shouldDrawInsertionPoint: Bool](nstextview/shoulddrawinsertionpoint.md)
  A Boolean value that determines whether the receiver should draw its insertion point.
- [func drawInsertionPoint(in: NSRect, color: NSColor, turnedOn: Bool)](nstextview/drawinsertionpoint(in:color:turnedon:).md)
  Draws or erases the insertion point.
- [func drawBackground(in: NSRect)](nstextview/drawbackground(in:).md)
  Draws the background of the text view.
- [func setConstrainedFrameSize(NSSize)](nstextview/setconstrainedframesize(_:).md)
  Attempts to set the frame size as if by user action.
- [func cleanUpAfterDragOperation()](nstextview/cleanupafterdragoperation.md)
  Releases the drag information still existing after the dragging session has completed.
- [func showFindIndicator(for: NSRange)](nstextview/showfindindicator(for:).md)
  Causes a temporary highlighting effect to appear around the visible portion (or portions) of the specified range.
- [class func scrollableDocumentContentTextView() -> NSScrollView](nstextview/scrollabledocumentcontenttextview.md)
- [class func scrollablePlainDocumentContentTextView() -> NSScrollView](nstextview/scrollableplaindocumentcontenttextview.md)
- [class func scrollableTextView() -> NSScrollView](nstextview/scrollabletextview.md)
### Inserting text
- [var allowedInputSourceLocales: [String]?](nstextview/allowedinputsourcelocales.md)
  An array of locale identifiers representing input sources that are allowed to be enabled when the receiver has the keyboard focus.
- [func insertText(Any)](nstextview/inserttext(_:).md)
  Inserts `aString` into the receiver’s text at the insertion point if there is one, otherwise replacing the selection.
### Setting behavioral attributes
- [var allowsUndo: Bool](nstextview/allowsundo.md)
  A Boolean value that indicates whether the receiver allows undo.
- [var isEditable: Bool](nstextview/iseditable.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager allow the user to edit text.
- [var isSelectable: Bool](nstextview/isselectable.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager allow the user to select text.
- [var isFieldEditor: Bool](nstextview/isfieldeditor.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager behave as field editors.
- [var isRichText: Bool](nstextview/isrichtext.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager allow the user to apply attributes to specific ranges of text.
- [var importsGraphics: Bool](nstextview/importsgraphics.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager allow the user to import files by dragging.
- [func setBaseWritingDirection(NSWritingDirection, range: NSRange)](nstextview/setbasewritingdirection(_:range:).md)
  Sets the base writing direction of a range of text.
- [var defaultParagraphStyle: NSParagraphStyle?](nstextview/defaultparagraphstyle.md)
  The receiver’s default paragraph style.
- [func outline(Any?)](nstextview/outline(_:).md)
  Adds the outline attribute to the selected text attributes if absent; removes the attribute if present.
- [var allowsImageEditing: Bool](nstextview/allowsimageediting.md)
  Indicates whether image attachments should permit editing of their images.
- [var isAutomaticQuoteSubstitutionEnabled: Bool](nstextview/isautomaticquotesubstitutionenabled.md)
  A Boolean value that enables and disables automatic quotation mark substitution.
- [func toggleAutomaticQuoteSubstitution(Any?)](nstextview/toggleautomaticquotesubstitution(_:).md)
  Changes the state of automatic quotation mark substitution from enabled to disabled and vice versa.
- [var isAutomaticLinkDetectionEnabled: Bool](nstextview/isautomaticlinkdetectionenabled.md)
  A Boolean value that enables or disables automatic link detection.
- [func toggleAutomaticLinkDetection(Any?)](nstextview/toggleautomaticlinkdetection(_:).md)
  Changes the state of automatic link detection from enabled to disabled and vice versa.
- [var displaysLinkToolTips: Bool](nstextview/displayslinktooltips.md)
  A Boolean value that indicates whether the text view automatically supplies the destination of a link as a tooltip for text that has a link attribute.
- [var isAutomaticTextCompletionEnabled: Bool](nstextview/isautomatictextcompletionenabled.md)
  A Boolean value that indicates whether the text view supplies autocompletion suggestions as the user types.
- [func toggleAutomaticTextCompletion(Any?)](nstextview/toggleautomatictextcompletion(_:).md)
- [var usesAdaptiveColorMappingForDarkAppearance: Bool](nstextview/usesadaptivecolormappingfordarkappearance.md)
  A Boolean value that indicates whether the framework should use adaptive color mapping for dark appearance.
- [var usesRolloverButtonForSelection: Bool](nstextview/usesrolloverbuttonforselection.md)
### Using text formatting controls
- [var usesRuler: Bool](nstextview/usesruler.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager use a ruler.
- [var isRulerVisible: Bool](nstextview/isrulervisible.md)
  A Boolean value that controls whether the scroll view enclosing text views sharing the receiver’s layout manager displays the ruler.
- [var usesInspectorBar: Bool](nstextview/usesinspectorbar.md)
  A Boolean value that indicates whether this text view uses the inspector bar.
### Managing the selection
- [var selectedRanges: [NSValue]](nstextview/selectedranges.md)
  An array containing the ranges of characters selected in the receiver’s layout manager.
- [func setSelectedRange(NSRange)](nstextview/setselectedrange(_:).md)
  Selects the specified range of characters in response to user action.
- [func setSelectedRange(NSRange, affinity: NSSelectionAffinity, stillSelecting: Bool)](nstextview/setselectedrange(_:affinity:stillselecting:).md)
  Sets the selection to a range of characters in response to user action.
- [func setSelectedRanges([NSValue], affinity: NSSelectionAffinity, stillSelecting: Bool)](nstextview/setselectedranges(_:affinity:stillselecting:).md)
  Sets the selection to the characters in an array of ranges in response to user action.
- [var selectionAffinity: NSSelectionAffinity](nstextview/selectionaffinity.md)
  The preferred direction of selection.
- [var selectionGranularity: NSSelectionGranularity](nstextview/selectiongranularity.md)
  The selection granularity for subsequent extension of a selection.
- [var insertionPointColor: NSColor!](nstextview/insertionpointcolor.md)
  The color of the insertion point.
- [func updateInsertionPointStateAndRestartTimer(Bool)](nstextview/updateinsertionpointstateandrestarttimer(_:).md)
  Updates the insertion point’s location and optionally restarts the blinking cursor timer.
- [var selectedTextAttributes: [NSAttributedString.Key : Any]](nstextview/selectedtextattributes.md)
  The attributes used to indicate the selection.
- [var markedTextAttributes: [NSAttributedString.Key : Any]?](nstextview/markedtextattributes.md)
  The attributes used to draw marked text.
- [var linkTextAttributes: [NSAttributedString.Key : Any]?](nstextview/linktextattributes.md)
  The attributes used to draw the onscreen presentation of link text.
- [func characterIndexForInsertion(at: NSPoint) -> Int](nstextview/characterindexforinsertion(at:).md)
  Returns a character index appropriate for placing a zero-length selection for an insertion point associated with the mouse at the given point.
- [func updateCandidates()](nstextview/updatecandidates.md)
### Managing the pasteboard
- [func preferredPasteboardType(from: [NSPasteboard.PasteboardType], restrictedToTypesFrom: [NSPasteboard.PasteboardType]?) -> NSPasteboard.PasteboardType?](nstextview/preferredpasteboardtype(from:restrictedtotypesfrom:).md)
  Returns whatever type on the pasteboard would be most preferred for copying data.
- [func readSelection(from: NSPasteboard) -> Bool](nstextview/readselection(from:).md)
  Reads the text view’s preferred type of data from the specified pasteboard.
- [func readSelection(from: NSPasteboard, type: NSPasteboard.PasteboardType) -> Bool](nstextview/readselection(from:type:).md)
  Reads data of the given type from the specified pasteboard.
- [var readablePasteboardTypes: [NSPasteboard.PasteboardType]](nstextview/readablepasteboardtypes.md)
  The types this text view can read immediately from the pasteboard.
- [var writablePasteboardTypes: [NSPasteboard.PasteboardType]](nstextview/writablepasteboardtypes.md)
  The pasteboard types that can be provided from the current selection.
- [func writeSelection(to: NSPasteboard, type: NSPasteboard.PasteboardType) -> Bool](nstextview/writeselection(to:type:).md)
  Writes the current selection to the specified pasteboard using the given type.
- [func writeSelection(to: NSPasteboard, types: [NSPasteboard.PasteboardType]) -> Bool](nstextview/writeselection(to:types:).md)
  Writes the current selection to the specified pasteboard under each given type.
- [func validRequestor(forSendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?](nstextview/validrequestor(forsendtype:returntype:).md)
  Returns `self` if the text view can provide and accept the specified data types, or `nil` if it can’t.
### Setting text attributes
- [func alignJustified(Any?)](nstextview/alignjustified(_:).md)
  Applies full justification to selected paragraphs (or all text, if the receiver is a plain text object).
- [func changeAttributes(Any?)](nstextview/changeattributes(_:).md)
  Changes the attributes of the current selection.
- [func changeColor(Any?)](nstextview/changecolor(_:).md)
  Sets the color of the selected text.
- [func setAlignment(NSTextAlignment, range: NSRange)](nstextview/setalignment(_:range:).md)
  Sets the alignment of the paragraphs containing characters in the specified range.
- [var typingAttributes: [NSAttributedString.Key : Any]](nstextview/typingattributes.md)
  The receiver’s typing attributes.
- [func useStandardKerning(Any?)](nstextview/usestandardkerning(_:).md)
  Set the receiver to use pair kerning data for the glyphs in its selection, or for all glyphs if the receiver is a plain text view.
- [func lowerBaseline(Any?)](nstextview/lowerbaseline(_:).md)
  Lowers the baseline offset of selected text by 1 point, or of all text if the receiver is a plain text view.
- [func raiseBaseline(Any?)](nstextview/raisebaseline(_:).md)
  Raises the baseline offset of selected text by 1 point, or of all text if the receiver is a plain text view.
- [func turnOffKerning(Any?)](nstextview/turnoffkerning(_:).md)
  Sets the receiver to use nominal glyph spacing for the glyphs in its selection, or for all glyphs if the receiver is a plain text view.
- [func loosenKerning(Any?)](nstextview/loosenkerning(_:).md)
  Increases the space between glyphs in the receiver’s selection, or in all text if the receiver is a plain text view.
- [func tightenKerning(Any?)](nstextview/tightenkerning(_:).md)
  Decreases the space between glyphs in the receiver’s selection, or for all glyphs if the receiver is a plain text view.
- [func useStandardLigatures(Any?)](nstextview/usestandardligatures(_:).md)
  Sets the receiver to use the standard ligatures available for the fonts and languages used when setting text, for the glyphs in the selection if the receiver is a rich text view, or for all glyphs if it’s a plain text view.
- [func turnOffLigatures(Any?)](nstextview/turnoffligatures(_:).md)
  Sets the receiver to use only required ligatures when setting text, for the glyphs in the selection if the receiver is a rich text view, or for all glyphs if it’s a plain text view.
- [func useAllLigatures(Any?)](nstextview/useallligatures(_:).md)
  Sets the receiver to use all ligatures available for the fonts and languages used when setting text, for the glyphs in the selection if the receiver is a rich text view, or for all glyphs if it’s a plain text view.
- [func toggleTraditionalCharacterShape(Any?)](nstextview/toggletraditionalcharactershape(_:).md)
  Toggles the `NSCharacterShapeAttributeName` attribute at the current selection.
### Clicking and pasting
- [func clicked(onLink: Any, at: Int)](nstextview/clicked(onlink:at:).md)
  Causes the text view to act as if the user clicked on some text with the given link as the value of a link attribute associated with the text.
- [func pasteAsPlainText(Any?)](nstextview/pasteasplaintext(_:).md)
  Inserts the contents of the pasteboard into the receiver’s text as plain text.
- [func pasteAsRichText(Any?)](nstextview/pasteasrichtext(_:).md)
  This action method inserts the contents of the pasteboard into the receiver’s text as rich text, maintaining its attributes.
### Supporting undo
- [func breakUndoCoalescing()](nstextview/breakundocoalescing.md)
  Informs the receiver that it should begin coalescing successive typing operations in a new undo grouping.
- [var isCoalescingUndo: Bool](nstextview/iscoalescingundo.md)
  A Boolean value that indicates whether undo coalescing is in progress.
### Customizing subclass behaviors
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
- [func smartDeleteRange(forProposedRange: NSRange) -> NSRange](nstextview/smartdeleterange(forproposedrange:).md)
  Returns an extended range that includes adjacent whitespace that should be deleted along with the proposed range in order to preserve proper spacing and punctuation.
- [func smartInsert(afterStringFor: String, replacing: NSRange) -> String?](nstextview/smartinsert(afterstringfor:replacing:).md)
  Returns any whitespace that needs to be added after the string to preserve proper spacing and punctuation when the string replaces the characters in the specified range.
- [func smartInsert(beforeStringFor: String, replacing: NSRange) -> String?](nstextview/smartinsert(beforestringfor:replacing:).md)
  Returns any whitespace that needs to be added before the string to preserve proper spacing and punctuation when the string replaces the characters in the specified range.
- [func smartInsert(for: String, replacing: NSRange, before: AutoreleasingUnsafeMutablePointer<NSString?>?, after: AutoreleasingUnsafeMutablePointer<NSString?>?)](nstextview/smartinsert(for:replacing:before:after:).md)
  Determines whether whitespace needs to be added around the string to preserve proper spacing and punctuation when it replaces the characters in the specified range.
- [func toggleSmartInsertDelete(Any?)](nstextview/togglesmartinsertdelete(_:).md)
  Changes the state of smart insert and delete from enabled to disabled and vice versa.
### Working with the spelling checker
- [var isContinuousSpellCheckingEnabled: Bool](nstextview/iscontinuousspellcheckingenabled.md)
  A Boolean value that indicates whether the receiver has continuous spell checking enabled.
- [var spellCheckerDocumentTag: Int](nstextview/spellcheckerdocumenttag.md)
  A tag identifying the text view’s text as a document for the spell checker server.
- [func toggleContinuousSpellChecking(Any?)](nstextview/togglecontinuousspellchecking(_:).md)
  Toggles whether continuous spell checking is enabled for the receiver.
- [var isGrammarCheckingEnabled: Bool](nstextview/isgrammarcheckingenabled.md)
  Enables and disables grammar checking.
- [func toggleGrammarChecking(Any?)](nstextview/togglegrammarchecking(_:).md)
  Changes the state of grammar checking from enabled to disabled and vice versa.
- [func setSpellingState(Int, range: NSRange)](nstextview/setspellingstate(_:range:).md)
  Sets the spelling state, which controls the display of the spelling and grammar indicators on the given text range.
### Working with the sharing service picker
- [func orderFrontSharingServicePicker(Any?)](nstextview/orderfrontsharingservicepicker(_:).md)
  Creates and displays a new instance of the sharing service picker.
### Supporting the ruler view
- [func rulerView(NSRulerView, didMove: NSRulerMarker)](nstextview/rulerview(_:didmove:).md)
  Modifies the paragraph style of the paragraphs containing the selection to record the new location of the marker.
- [func rulerView(NSRulerView, willMove: NSRulerMarker, toLocation: CGFloat) -> CGFloat](nstextview/rulerview(_:willmove:tolocation:).md)
  Returns a potentially modified location to which the marker should be moved.
- [func rulerView(NSRulerView, shouldMove: NSRulerMarker) -> Bool](nstextview/rulerview(_:shouldmove:).md)
  Returns whether the marker should be moved.
- [func rulerView(NSRulerView, didRemove: NSRulerMarker)](nstextview/rulerview(_:didremove:).md)
  Modifies the paragraph style of the paragraphs containing the selection—if possible—by removing the specified marker.
- [func rulerView(NSRulerView, shouldRemove: NSRulerMarker) -> Bool](nstextview/rulerview(_:shouldremove:).md)
  Returns whether the marker should be removed.
- [func rulerView(NSRulerView, didAdd: NSRulerMarker)](nstextview/rulerview(_:didadd:).md)
  Modifies the paragraph style of the paragraphs containing the selection to accommodate a new marker.
- [func rulerView(NSRulerView, shouldAdd: NSRulerMarker) -> Bool](nstextview/rulerview(_:shouldadd:).md)
  Returns whether a new marker can be added.
- [func rulerView(NSRulerView, willAdd: NSRulerMarker, atLocation: CGFloat) -> CGFloat](nstextview/rulerview(_:willadd:atlocation:).md)
  Returns a potentially modified location to which the marker should be added.
- [func rulerView(NSRulerView, handleMouseDownWith: NSEvent)](nstextview/rulerview(_:handlemousedownwith:).md)
  Adds a left tab marker to the ruler at the location clicked.
### Dragging
- [func dragImageForSelection(with: NSEvent, origin: NSPointPointer?) -> NSImage?](nstextview/dragimageforselection(with:origin:).md)
  Returns an appropriate drag image for the drag initiated by the specified event.
- [func dragOperation(for: any NSDraggingInfo, type: NSPasteboard.PasteboardType) -> NSDragOperation](nstextview/dragoperation(for:type:).md)
  Returns the type of drag operation that should be performed if the image were released now.
- [func dragSelection(with: NSEvent, offset: NSSize, slideBack: Bool) -> Bool](nstextview/dragselection(with:offset:slideback:).md)
  Begins dragging the current selected text range.
- [var acceptsGlyphInfo: Bool](nstextview/acceptsglyphinfo.md)
  A Boolean value that indicates whether the receiver accepts the glyph info attribute.
### Speaking text
- [func startSpeaking(Any?)](nstextview/startspeaking(_:).md)
  Speaks the selected text, or all text if no selection.
- [func stopSpeaking(Any?)](nstextview/stopspeaking(_:).md)
  Stops the speaking of text.
### Working with panels
- [var usesFontPanel: Bool](nstextview/usesfontpanel.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager use the Font panel and Font menu.
- [var usesFindPanel: Bool](nstextview/usesfindpanel.md)
  A Boolean value that indicates whether the receiver allows for a find panel.
- [func performFindPanelAction(Any?)](nstextview/performfindpanelaction(_:).md)
  Performs a find panel action specified by the sender’s tag.
- [func orderFrontLinkPanel(Any?)](nstextview/orderfrontlinkpanel(_:).md)
  Brings forward a panel allowing the user to manipulate links in the text view.
- [func orderFrontListPanel(Any?)](nstextview/orderfrontlistpanel(_:).md)
  Brings forward a panel allowing the user to manipulate text lists in the text view.
- [func orderFrontSpacingPanel(Any?)](nstextview/orderfrontspacingpanel(_:).md)
  Brings forward a panel allowing the user to manipulate text line heights, interline spacing, and paragraph spacing, in the text view.
- [func orderFrontTablePanel(Any?)](nstextview/orderfronttablepanel(_:).md)
  Brings forward a panel allowing the user to manipulate text tables in the text view.
- [func orderFrontSubstitutionsPanel(Any?)](nstextview/orderfrontsubstitutionspanel(_:).md)
  Brings forward a panel allowing the user to specify string substitutions in the text view.
### Performing text completion
- [func complete(Any?)](nstextview/complete(_:).md)
  Invokes completion in a text view.
- [func completions(forPartialWordRange: NSRange, indexOfSelectedItem: UnsafeMutablePointer<Int>) -> [String]?](nstextview/completions(forpartialwordrange:indexofselecteditem:).md)
  Returns an array of potential completions, in the order to be presented, representing possible word completions available from a partial word.
- [func insertCompletion(String, forPartialWordRange: NSRange, movement: Int, isFinal: Bool)](nstextview/insertcompletion(_:forpartialwordrange:movement:isfinal:).md)
  Inserts the selected completion into the text at the appropriate location.
- [var rangeForUserCompletion: NSRange](nstextview/rangeforusercompletion.md)
  The partial range from the most recent beginning of a word up to the insertion point.
### Checking and substituting text
- [func checkTextInDocument(Any?)](nstextview/checktextindocument(_:).md)
  Performs the default text checking on the entire document.
- [func checkTextInSelection(Any?)](nstextview/checktextinselection(_:).md)
  Performs the default text checking on the current selection.
- [func checkText(in: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any])](nstextview/checktext(in:types:options:).md)
  Check and replace the text in the range using the specified checking types and options.
- [func handleTextCheckingResults([NSTextCheckingResult], forRange: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any], orthography: NSOrthography, wordCount: Int)](nstextview/handletextcheckingresults(_:forrange:types:options:orthography:wordcount:).md)
  Handles the text checking results returned by the text view
- [var enabledTextCheckingTypes: NSTextCheckingTypes](nstextview/enabledtextcheckingtypes.md)
  The default text checking types.
- [var isAutomaticDashSubstitutionEnabled: Bool](nstextview/isautomaticdashsubstitutionenabled.md)
  A Boolean value that indicates whether automatic dash substitution is enabled.
- [func toggleAutomaticDashSubstitution(Any?)](nstextview/toggleautomaticdashsubstitution(_:).md)
  Toggles the state of the automatic dash substitution.
- [var isAutomaticDataDetectionEnabled: Bool](nstextview/isautomaticdatadetectionenabled.md)
  A Boolean value that indicates whether automatic data detection is enabled.
- [func toggleAutomaticDataDetection(Any?)](nstextview/toggleautomaticdatadetection(_:).md)
  Toggles the state of the automatic data detection.
- [var isAutomaticSpellingCorrectionEnabled: Bool](nstextview/isautomaticspellingcorrectionenabled.md)
  A Boolean value that indicates whether automatic spelling correction is enabled.
- [func toggleAutomaticSpellingCorrection(Any?)](nstextview/toggleautomaticspellingcorrection(_:).md)
  Toggles the state of the automatic spelling correction.
- [var isAutomaticTextReplacementEnabled: Bool](nstextview/isautomatictextreplacementenabled.md)
  A Boolean value that indicates whether automatic text replacement is enabled.
- [func toggleAutomaticTextReplacement(Any?)](nstextview/toggleautomatictextreplacement(_:).md)
  Toggles the state of the automatic text replacement.
- [func performValidatedReplacement(in: NSRange, with: NSAttributedString) -> Bool](nstextview/performvalidatedreplacement(in:with:).md)
  Replaces text in the range you specify with the attributed string you provide.
### Getting the writing tools status
- [var isWritingToolsActive: Bool](nstextview/iswritingtoolsactive.md)
### Supporting QuickLook
- [func updateQuickLookPreviewPanel()](nstextview/updatequicklookpreviewpanel.md)
  Notifies the QuickLook panel that an update may be required.
- [func toggleQuickLookPreviewPanel(Any?)](nstextview/togglequicklookpreviewpanel(_:).md)
  An action message that toggles the visibility state of the Quick Look preview panel.
- [func quickLookPreviewableItems(inRanges: [NSValue]) -> [any QLPreviewItem]](nstextview/quicklookpreviewableitems(inranges:).md)
  Returns an array of URLs for items that can be displayed by QuickLook in the specified ranges.
### Changing layout orientation
- [func changeLayoutOrientation(Any?)](nstextview/changelayoutorientation(_:).md)
  An action method that sets the layout orientation of the text.
- [func setLayoutOrientation(NSLayoutManager.TextLayoutOrientation)](nstextview/setlayoutorientation(_:).md)
  Changes the receiver’s layout orientation and invalidates the contents.
### Using the Find Bar
- [var usesFindBar: Bool](nstextview/usesfindbar.md)
  A Boolean value that indicates whether to use the find bar for this text view.
- [var isIncrementalSearchingEnabled: Bool](nstextview/isincrementalsearchingenabled.md)
  A Boolean value that indicates whether incremental searching is enabled.
### Constants
- [enum NSSelectionGranularity](nsselectiongranularity.md)
  These constants specify how much the text view extends the selection when the user drags the mouse. They’re used by [`selectionGranularity`](nstextview/selectiongranularity.md), and [`selectionRange(forProposedRange:granularity:)`](nstextview/selectionrange(forproposedrange:granularity:).md):
- [enum NSSelectionAffinity](nsselectionaffinity.md)
  These constants specify the preferred direction of selection. They’re used by [`selectionAffinity`](nstextview/selectionaffinity.md) and [`setSelectedRange(_:affinity:stillSelecting:)`](nstextview/setselectedrange(_:affinity:stillselecting:).md).
- [enum NSFindPanelAction](nsfindpanelaction.md)
  These constants define the tags for [`performFindPanelAction(_:)`](nstextview/performfindpanelaction(_:).md).
- [Input Sources Locale Identifiers](input-sources-locale-identifiers.md)
  Locale identifiers represent the input sources available.
- [Find Panel Search Metadata](find-panel-search-metadata.md)
  In addition to communicating search strings via the find pasteboard, the standard Find panel for `NSTextView` also communicates search option metadata, including case sensitivity and substring matching options. This metadata is stored in a property list as the [`findPanelSearchOptions`](nspasteboard/pasteboardtype/findpanelsearchoptions.md) value on the global find pasteboard. As such, third party applications may store additional keys in this property list to communicate additional metadata as desired to support the various search options common to many third-party applications’ Find panels.
- [enum NSFindPanelSubstringMatchType](nsfindpanelsubstringmatchtype.md)
  The type of substring matching used by the Find panel.
### Notifications
- [class let didChangeSelectionNotification: NSNotification.Name](nstextview/didchangeselectionnotification.md)
  Posted when the selected range of characters changes.
- [class let willChangeNotifyingTextViewNotification: NSNotification.Name](nstextview/willchangenotifyingtextviewnotification.md)
  Posted when a new text view is established as the text view that sends notifications.
- [class let didChangeTypingAttributesNotification: NSNotification.Name](nstextview/didchangetypingattributesnotification.md)
  Posted when there is a change in the typing attributes within a text view.
- [class let didSwitchToNSLayoutManagerNotification: NSNotification.Name](nstextview/didswitchtonslayoutmanagernotification.md)
  Posted by the framework after switching to using the compatibility mode layout manager.
- [class let willSwitchToNSLayoutManagerNotification: NSNotification.Name](nstextview/willswitchtonslayoutmanagernotification.md)
  Posted by the framework before switching to the compatibility mode layout manager.
### Interacting with the Touch Bar
- [var allowsCharacterPickerTouchBarItem: Bool](nstextview/allowscharacterpickertouchbaritem.md)
- [var candidateListTouchBarItem: NSCandidateListTouchBarItem<AnyObject>?](nstextview/candidatelisttouchbaritem.md)
- [func updateTextTouchBarItems()](nstextview/updatetexttouchbaritems.md)
- [func updateTouchBarItemIdentifiers()](nstextview/updatetouchbaritemidentifiers.md)
### Instance Properties
- [var allowedWritingToolsResultOptions: NSWritingToolsResultOptions](nstextview/allowedwritingtoolsresultoptions.md)
- [var inlinePredictionType: NSTextInputTraitType](nstextview/inlinepredictiontype.md)
- [var mathExpressionCompletionType: NSTextInputTraitType](nstextview/mathexpressioncompletiontype.md)
- [var textHighlightAttributes: [NSAttributedString.Key : Any]](nstextview/texthighlightattributes.md)
  ************************* Text Highlight  support **************************
- [var writingToolsBehavior: NSWritingToolsBehavior](nstextview/writingtoolsbehavior.md)
### Instance Methods
- [func drawTextHighlightBackground(for: NSTextRange, origin: NSPoint)](nstextview/drawtexthighlightbackground(for:origin:).md)
- [func highlight(Any?)](nstextview/highlight(_:).md)
  An action for toggling `NSTextHighlightStyleAttributeName` in the receiver’s selected range. The sender should be a menu item with a `representedObject` of type (`NSTextHighlightColorScheme`).

## Relationships

### Inherits From
- [NSText](nstext.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityNavigableStaticText](nsaccessibilitynavigablestatictext.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAccessibilityStaticText](nsaccessibilitystatictext.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCandidateListTouchBarItemDelegate](nscandidatelisttouchbaritemdelegate.md)
- [NSChangeSpelling](nschangespelling.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSColorChanging](nscolorchanging.md)
- [NSDraggingDestination](nsdraggingdestination.md)
- [NSDraggingSource](nsdraggingsource.md)
- [NSIgnoreMisspelledWords](nsignoremisspelledwords.md)
- [NSMenuItemValidation](nsmenuitemvalidation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTextContent](nstextcontent.md)
- [NSTextInput](nstextinput.md)
- [NSTextInputClient](nstextinputclient.md)
- [NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md)
- [NSTouchBarDelegate](nstouchbardelegate.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [NSUserInterfaceValidations](nsuserinterfacevalidations.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSTextField](nstextfield.md)
  Text the user can select or edit to send an action message to a target when the user presses the Return key.
- [protocol NSTextFieldDelegate](nstextfielddelegate.md)
  A protocol that a text field delegate can use to control its field editor action menu.
- [protocol NSTextViewDelegate](nstextviewdelegate.md)
  A set of optional methods that text view delegates can use to manage selection, set text attributes, work with the spell checker, and more.
- [protocol NSTextDelegate](nstextdelegate.md)
  A set of optional methods implemented by the delegate of an [`NSText`](nstext.md) object to edit text and change text formats.
- [class NSText](nstext.md)
  The most general programmatic interface for objects that manage text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview)*