# BETextInput

**Framework**: BrowserEngineKit  
**Kind**: protocol  
**Role**: Protocol

A protocol for asynchronous text views that integrate with the text system.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
protocol BETextInput : BEResponderEditActions, BETextSelectionDirectionNavigation, UIKeyInput
```

```objc
@protocol BETextInput <UIKeyInput, BETextSelectionDirectionNavigation, BEResponderEditActions>
```

## Mentions

- [Integrating custom browser text views with UIKit](./integrating-custom-browser-text-views-with-uikit.md)
- [Supporting extended text interactions](./support-extended-text-interactions.md)

#### Overview

Adopt this protocol in a text field to perform asynchronous actions and provide information to the text system. For example, you can make an XPC request to a web content extension. See [Integrating custom browser text views with UIKit](./integrating-custom-browser-text-views-with-uikit.md).

## Topics

### Managing the text input view
- [var textInputView: UIView](./betextinput/textinputview.md)
  An affiliated view that provides a coordinate system for all geometric values in this protocol.
- [var unscaledView: UIView](./betextinput/unscaledview.md)
  A view that represents the web content that’s agnostic of zoom state.
- [var selectionClipRect: CGRect](./betextinput/selectioncliprect.md)
  A rectangle that represents the bounds of editable elements.
- [var unobscuredContentRect: CGRect](./betextinput/unobscuredcontentrect.md)
  A rectangle that frames a user interface, such as text-selection handles, in an unobscured location.
### Managing selection
- [var selectedText: String?](./betextinput/selectedtext.md)
  A string that represents the selected text.
- [var selectedTextRange: UITextRange?](./betextinput/selectedtextrange.md)
  A range that represents the selected text.
- [var isSelectionAtDocumentStart: Bool](./betextinput/isselectionatdocumentstart.md)
  A Boolean value that indicates if the current selection is at the beginning of the document.
- [func selectPosition(at: CGPoint, completionHandler: () -> Void)](./betextinput/selectposition%28at,completionhandler%29.md)
  Sets the selection caret to the given point.
- [func selectPosition(at: CGPoint, for: BETextDocumentRequest, completionHandler: (BETextDocumentContext) -> Void)](./betextinput/selectposition%28at,for,completionhandler%29.md)
  Sets the selection caret to the given point.
- [func adjustSelection(by: BEDirectionalTextRange, completionHandler: () -> Void)](./betextinput/adjustselection%28by,completionhandler%29.md)
  Adjusts the selection using a range.
- [func updateCurrentSelection(to: CGPoint, from: BEGestureType, in: UIGestureRecognizer.State)](./betextinput/updatecurrentselection%28to,from,in%29.md)
  Indicates the point where the text interaction gesture changes.
### Managing selection views
- [var selectionContainerViewAboveText: UIView?](./betextinput/selectioncontainerviewabovetext.md)
  An optional view you supply to draw text selection above the text.
- [var selectionContainerViewBelowText: UIView?](./betextinput/selectioncontainerviewbelowtext.md)
  An optional view you supply to draw text selection below the text.
### Managing marked text
- [var hasMarkedText: Bool](./betextinput/hasmarkedtext.md)
  A Boolean value that indicates if marked text exists for an active input session.
- [var markedTextRange: UITextRange?](./betextinput/markedtextrange.md)
  A range that represents the position of the marked text.
- [func unmarkText()](./betextinput/unmarktext%28%29.md)
  Unmarks the currently marked text.
- [func isPointNearMarkedText(CGPoint) -> Bool](./betextinput/ispointnearmarkedtext%28_%29.md)
  Provides a Boolean value that indicates if a point is near marked text.
### Inserting and replacing text
- [func insert(BETextSuggestion)](./betextinput/insert%28_%29-5iryn.md)
  Inserts a text suggestion in response to a suggestion selection.
- [func insert(BETextAlternatives)](./betextinput/insert%28_%29-6x7hd.md)
  Inserts the given text or one of the available alternatives.
- [func replaceSelectedText(String, withText: String)](./betextinput/replaceselectedtext%28_,withtext%29.md)
  Replaces text with new text, either within the current selection or near the cursor.
- [func replaceDictatedText(String, withText: String)](./betextinput/replacedictatedtext%28_,withtext%29.md)
  Replaces the specified text for the text of a dictation.
- [func add(BETextAlternatives)](./betextinput/add%28_%29.md)
  Adds text alternatives to the text input object for the current selection.
### Deleting text
- [func delete(in: UITextStorageDirection, to: UITextGranularity)](./betextinput/delete%28in,to%29.md)
  Deletes the specified amount of text.
### Adjusting text
- [func transposeCharactersAroundSelection()](./betextinput/transposecharactersaroundselection%28%29.md)
  Transposes the characters on either side of the caret.
- [func selectWordForReplacement()](./betextinput/selectwordforreplacement%28%29.md)
  Selects a tapped word with autocorrect suggestions.
### Requesting context
- [func requestDocumentContext(BETextDocumentRequest, completionHandler: (BETextDocumentContext) -> Void)](./betextinput/requestdocumentcontext%28_,completionhandler%29.md)
  Gathers context for the system about the current document.
- [func requestTextContextForAutocorrection(completionHandler: (BETextDocumentContext) -> Void)](./betextinput/requesttextcontextforautocorrection%28completionhandler%29.md)
  A method the text system calls to get extra information for autocorrection suggestions.
- [func requestTextRects(for: String, withCompletionHandler: ([UITextSelectionRect]) -> Void)](./betextinput/requesttextrects%28for,withcompletionhandler%29.md)
  Gathers context for the presentation of a text-related user interface.
### Managing placeholders
- [func insertTextPlaceholder(size: CGSize, completionHandler: (UITextPlaceholder) -> Void)](./betextinput/inserttextplaceholder%28size,completionhandler%29.md)
  Inserts a placeholder object to reserve visual space during text input.
### Managing text traits
- [var extendedTextInputTraits: (any BEExtendedTextInputTraits)?](./betextinput/extendedtextinputtraits.md)
  An object that customizes text-input appearance and behavior beyond the standard system traits.
- [var isEditable: Bool](./betextinput/iseditable.md)
  A Boolean value that determines the ability to modify text.
### Responding to keyboard input
- [func shiftKeyStateChanged(fromState: BEKeyModifierFlags, toState: BEKeyModifierFlags)](./betextinput/shiftkeystatechanged%28fromstate,tostate%29.md)
  Indicates a transition in the state of the Shift key.
### Responding to dictation
- [func didInsertFinalDictationResult()](./betextinput/didinsertfinaldictationresult%28%29.md)
  A Boolean value that indicates when the system inserts a dictation result.
### Managing the edit menu
- [func selectTextForEditMenuWithLocation(inView: CGPoint, completionHandler: (Bool, String?, NSRange) -> Void)](./betextinput/selecttextforeditmenuwithlocation%28inview,completionhandler%29.md)
  Indicates the edit menu displays at the given location in the text input view’s coordinate space.
- [func canPerformAction(Selector, withSender: Any?) -> Bool](./betextinput/canperformaction%28_,withsender%29.md)
  Indicates whether the text view can process a given action.
### Styling text
- [func textStyling(at: UITextPosition, in: UITextStorageDirection) -> [NSAttributedString.Key : Any]?](./betextinput/textstyling%28at,in%29.md)
  Provides a dictionary that customizes the appearance of strings.
### Instance Properties
- [var asyncInputDelegate: (any BETextInputDelegate)?](./betextinput/asyncinputdelegate.md)
  A delegate object that your text view notifies of events and changes in the text’s state.
- [var attributedMarkedText: NSAttributedString?](./betextinput/attributedmarkedtext.md)
  Attributed string for the text that has been marked as part of an active input session
- [var automaticallyPresentEditMenu: Bool](./betextinput/automaticallypresenteditmenu.md)
  Controls whether the edit menu is allowed to be presented or should be suppressed.
- [var isReplaceAllowed: Bool](./betextinput/isreplaceallowed.md)
  Returns whether replacement should be allowed for an editable element.
- [var markedText: String?](./betextinput/markedtext.md)
  String for the text that has been marked as part of an active input session
- [var textFirstRect: CGRect](./betextinput/textfirstrect.md)
  Returns a rect representing the bounds of the first line of marked text, if marked text is set.
- [var textLastRect: CGRect](./betextinput/textlastrect.md)
  Returns a rect representing the bounds of the last line of marked text, if marked text is set.
### Instance Methods
- [func adjustSelectionBoundary(to: CGPoint, touchPhase: BESelectionTouchPhase, baseIsStart: Bool, flags: BESelectionFlags)](./betextinput/adjustselectionboundary%28to,touchphase,baseisstart,flags%29.md)
  Adjusts the start or end boundary of the current selection to the given point.
- [func alternativesForSelectedText() -> [BETextAlternatives]?](./betextinput/alternativesforselectedtext%28%29.md)
  Returns the text alternatives that are available to the text input object.
- [func autoscroll(to: CGPoint)](./betextinput/autoscroll%28to%29.md)
  Indicates that a text gesture initiated autoscrolling.
- [func cancelAutoscroll()](./betextinput/cancelautoscroll%28%29.md)
  Indicates that the current autoscroll gesture is complete.
- [func caretRect(for: UITextPosition) -> CGRect](./betextinput/caretrect%28for%29.md)
  Returns a rectangle in which the system can draw the text-selection caret.
- [func handleKeyEntry(BEKeyEntry, completionHandler: (BEKeyEntry, Bool) -> Void)](./betextinput/handlekeyentry%28_,completionhandler%29.md)
  Accepts key-entry events from the text system for the text view to process.
- [func keyboardWillDismiss()](./betextinput/keyboardwilldismiss%28%29.md)
  Called when the user has requested the keyboard to dismiss itself.
- [func move(byOffset: Int)](./betextinput/move%28byoffset%29.md)
  Adjusts the current selection by `offset` in character granularity units
- [func moveSelection(atBoundary: UITextGranularity, in: UITextStorageDirection, completionHandler: () -> Void)](./betextinput/moveselection%28atboundary,in,completionhandler%29.md)
  Moves the text-selection caret relative to the current position.
- [func offset(from: UITextPosition, to: UITextPosition) -> Int](./betextinput/offset%28from,to%29.md)
  Returns the distance between two positions in the text view’s text.
- [func remove(UITextPlaceholder, willInsertText: Bool, completionHandler: () -> Void)](./betextinput/remove%28_,willinserttext,completionhandler%29.md)
  Removes a placeholder object from the text input view.
- [func removeTextAlternatives()](./betextinput/removetextalternatives%28%29.md)
  Removes text alternatives from the text input object for the current selection
- [func replaceText(String, withText: String, options: BETextReplacementOptions, completionHandler: ([UITextSelectionRect]) -> Void)](./betextinput/replacetext%28_,withtext,options,completionhandler%29.md)
  Replace the specified text preceding the current selection.
- [func requestPreferredArrowDirectionForEditMenu(completionHandler: (UIEditMenuArrowDirection) -> Void)](./betextinput/requestpreferredarrowdirectionforeditmenu%28completionhandler%29.md)
  Invoked by the system to gather context, including the client’s preference for how the edit menu should be positioned relative to the selected text.
- [func selectText(in: UITextGranularity, at: CGPoint, completionHandler: () -> Void)](./betextinput/selecttext%28in,at,completionhandler%29.md)
  Selects the text within the given granularity at the given point in the text view.
- [func selectionRects(for: UITextRange) -> [UITextSelectionRect]](./betextinput/selectionrects%28for%29.md)
  Returns an array of selection rectangles corresponding to the given text range.
- [func setAttributedMarkedText(NSAttributedString?, selectedRange: NSRange)](./betextinput/setattributedmarkedtext%28_,selectedrange%29.md)
  Inserts the provided styled text and marks it to indicate that it is part of an active input session.
- [func setBaseWritingDirection(NSWritingDirection, for: UITextRange)](./betextinput/setbasewritingdirection%28_,for%29.md)
  Informs the text view of the writing direction for a given range of text.
- [func setMarkedText(String?, selectedRange: NSRange)](./betextinput/setmarkedtext%28_,selectedrange%29.md)
  Inserts the provided text and marks it to indicate that it is part of an active input session.
- [func setSelection(from: CGPoint, to: CGPoint, gesture: BEGestureType, state: UIGestureRecognizer.State)](./betextinput/setselection%28from,to,gesture,state%29.md)
  Notifies the text view that its selection needs to change to the text between the given points.
- [func systemWillDismissEditMenu(withAnimator: any UIEditMenuInteractionAnimating)](./betextinput/systemwilldismisseditmenu%28withanimator%29.md)
  Invoked by the system when it is about to dismiss an edit menu with an animator.
- [func systemWillPresentEditMenu(withAnimator: any UIEditMenuInteractionAnimating)](./betextinput/systemwillpresenteditmenu%28withanimator%29.md)
  Invoked by the system when it is about to present an edit menu with an animator.
- [func text(in: UITextRange) -> String?](./betextinput/text%28in%29.md)
  Returns the text in a browser’s text view in the given range.
- [func textInteractionGesture(BEGestureType, shouldBeginAt: CGPoint) -> Bool](./betextinput/textinteractiongesture%28_,shouldbeginat%29.md)
  Returns whether a gesture at the given point in the view needs to begin.
- [func updateSelection(extent: CGPoint, boundary: UITextGranularity, completionHandler: (Bool) -> Void)](./betextinput/updateselection%28extent,boundary,completionhandler%29.md)
  Includes the text up to the given point in the current text selection.
- [func willInsertFinalDictationResult()](./betextinput/willinsertfinaldictationresult%28%29.md)
  Indicates the system is about to insert the final dictation result.

## Relationships

### Inherits From
- [BEResponderEditActions](./berespondereditactions.md)
- [BETextSelectionDirectionNavigation](./betextselectiondirectionnavigation.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [UIKeyInput](../UIKit/uikeyinput.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UITextInputTraits](../UIKit/uitextinputtraits.md)

## See Also

### Custom text views
- [Integrating custom browser text views with UIKit](./integrating-custom-browser-text-views-with-uikit.md)
  Process keyboard interactions asynchronously in your iOS browser app’s text view.
- [Supporting extended text interactions](./support-extended-text-interactions.md)
  Share content, add replacement shortcuts, and perform other rich actions in browser text views.
- [protocol BETextInputDelegate](./betextinputdelegate.md)
  A delegate protocol that a browser text view uses to notify the text system of changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput)*