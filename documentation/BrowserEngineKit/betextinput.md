# BETextInput

**Framework**: BrowserEngineKit  
**Kind**: protocol

A protocol to which text views conform to asynchronously integrate with the text system.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
protocol BETextInput : BEResponderEditActions, BETextSelectionDirectionNavigation, UIKeyInput
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)
- [Supporting extended text interactions](support-extended-text-interactions.md)

#### Overview

You adopt `BETextInput` in your text field when you need to perform asynchronous actions to provide information for the text system, for example, making an XPC request to a web content extension. For more information, see [`Integrating custom browser text views with UIKit`](integrating-custom-browser-text-views-with-uikit.md).

## Topics

### Updating the text system
- [var asyncInputDelegate: (any BETextInputDelegate)?](betextinput/asyncinputdelegate.md)
  A system-provided input delegate is assigned when the system is interested in input changes.
- [func canPerformAction(Selector, withSender: Any?) -> Bool](betextinput/canperformaction(_:withsender:).md)
  Returns whether text related actions, such those included in UIResponderStandardEditActions, can be handled
### Handling text input
- [var isEditable: Bool](betextinput/iseditable.md)
  Reflects the ability to modify text
- [func handleKeyEntry(BEKeyEntry, completionHandler: (BEKeyEntry, Bool) -> Void)](betextinput/handlekeyentry(_:completionhandler:).md)
  Accepts key-entry events from the text system for the text view to process.
- [func shiftKeyStateChanged(fromState: BEKeyModifierFlags, toState: BEKeyModifierFlags)](betextinput/shiftkeystatechanged(fromstate:tostate:).md)
  Indicates a transition in shift state
- [func text(in: UITextRange) -> String?](betextinput/text(in:).md)
  Returns the text in the specified range.
- [func offset(from: UITextPosition, to: UITextPosition) -> Int](betextinput/offset(from:to:).md)
  Returns the number of UTF-16 characters between one text position and another text position.
- [func setBaseWritingDirection(NSWritingDirection, for: UITextRange)](betextinput/setbasewritingdirection(_:for:).md)
  Sets the base writing direction for a specified range of text in a document.
- [func delete(in: UITextStorageDirection, to: UITextGranularity)](betextinput/delete(in:to:).md)
  Deletes text by the specified direction and granularity.  Current supported combinations include:
### Editing and correcting text
- [func transposeCharactersAroundSelection()](betextinput/transposecharactersaroundselection.md)
  Transposes the characters on either side of the caret in response to the key command, ctrl + T
- [func replaceText(String, withText: String, options: BETextReplacementOptions, completionHandler: ([UITextSelectionRect]) -> Void)](betextinput/replacetext(_:withtext:options:completionhandler:).md)
  Replace the specified text preceding the current selection.
- [func requestTextContextForAutocorrection(completionHandler: (BETextDocumentContext) -> Void)](betextinput/requesttextcontextforautocorrection(completionhandler:).md)
  Invoked by the system to gather context around the current selection.  Clients should generally include the setence that contains the current selection and include the previous sentence if the current selection is at a boundary.
- [func requestTextRects(for: String, withCompletionHandler: ([UITextSelectionRect]) -> Void)](betextinput/requesttextrects(for:withcompletionhandler:).md)
  Invoked by the system to gather context for the presentation of various text related UI’s. Completion handler should be invoked with the `UITextSelectionRect`s for the substring nearest to the caret that matches the given `input`
- [var automaticallyPresentEditMenu: Bool](betextinput/automaticallypresenteditmenu.md)
  Controls whether the edit menu is allowed to be presented or should be suppressed.
- [func requestPreferredArrowDirectionForEditMenu(completionHandler: (UIEditMenuArrowDirection) -> Void)](betextinput/requestpreferredarrowdirectionforeditmenu(completionhandler:).md)
  Invoked by the system to gather context, including the client’s preference for how the edit menu should be positioned relative to the selected text.
- [func systemWillPresentEditMenu(withAnimator: any UIEditMenuInteractionAnimating)](betextinput/systemwillpresenteditmenu(withanimator:).md)
  Invoked by the system when it is about to present an edit menu with an animator.
- [func systemWillDismissEditMenu(withAnimator: any UIEditMenuInteractionAnimating)](betextinput/systemwilldismisseditmenu(withanimator:).md)
  Invoked by the system when it is about to dismiss an edit menu with an animator.
### Input traits
- [var extendedTextInputTraits: (any BEExtendedTextInputTraits)?](betextinput/extendedtextinputtraits.md)
  Object from which the BEExtendedTextInputTraits will be gathered.
- [func textStyling(at: UITextPosition, in: UITextStorageDirection) -> [NSAttributedString.Key : Any]?](betextinput/textstyling(at:in:).md)
  Returns a dictionary containing NSAttributedString keys represeting appearance customizations.
### Replacing text
- [var isReplaceAllowed: Bool](betextinput/isreplaceallowed.md)
  Returns whether replacement should be allowed for an editable element.
- [func replaceSelectedText(String, withText: String)](betextinput/replaceselectedtext(_:withtext:).md)
  Replaces the specified `text` with `replacementText`
### Handling text gestures
- [func updateCurrentSelection(to: CGPoint, from: BEGestureType, in: UIGestureRecognizer.State)](betextinput/updatecurrentselection(to:from:in:).md)
  Indicates the `point` the text interaction gesture is tracking has changed
- [func setSelection(from: CGPoint, to: CGPoint, gesture: BEGestureType, state: UIGestureRecognizer.State)](betextinput/setselection(from:to:gesture:state:).md)
  Notifies the text view that its selection needs to change to the text between the given points.
- [func adjustSelectionBoundary(to: CGPoint, touchPhase: BESelectionTouchPhase, baseIsStart: Bool, flags: BESelectionFlags)](betextinput/adjustselectionboundary(to:touchphase:baseisstart:flags:).md)
  Adjusts the selection’s start or end boundary specified by `boundaryIsStart` to the `point`
- [func textInteractionGesture(BEGestureType, shouldBeginAt: CGPoint) -> Bool](betextinput/textinteractiongesture(_:shouldbeginat:).md)
  Returns whether a gesture with the given `gestureType` should begin for the given `point`
### Selecting text
- [var selectedText: String?](betextinput/selectedtext.md)
  String representing the selected text.
- [var selectedTextRange: UITextRange?](betextinput/selectedtextrange.md)
  Range representing the selected text.
- [var isSelectionAtDocumentStart: Bool](betextinput/isselectionatdocumentstart.md)
  Represents whether the current selection is at the beginning of the document
- [func caretRect(for: UITextPosition) -> CGRect](betextinput/caretrect(for:).md)
  Returns a rectangle to draw the caret at a specified insertion point.
- [func selectionRects(for: UITextRange) -> [UITextSelectionRect]](betextinput/selectionrects(for:).md)
  Returns an array of selection rects corresponding to the range of text.
- [func selectWordForReplacement()](betextinput/selectwordforreplacement.md)
  Selects a word with autocorrect replacement suggestions when it is tapped
- [func updateSelection(extent: CGPoint, boundary: UITextGranularity, completionHandler: (Bool) -> Void)](betextinput/updateselection(extent:boundary:completionhandler:).md)
  Includes the text up to the given point in the current text selection.
- [func selectText(in: UITextGranularity, at: CGPoint, completionHandler: () -> Void)](betextinput/selecttext(in:at:completionhandler:).md)
  Selects the text within the given granularity at the given point in the text view.
- [func selectPosition(at: CGPoint, completionHandler: () -> Void)](betextinput/selectposition(at:completionhandler:).md)
  Sets the selection caret to the given point
- [func selectPosition(at: CGPoint, for: BETextDocumentRequest, completionHandler: (BETextDocumentContext) -> Void)](betextinput/selectposition(at:for:completionhandler:).md)
  Sets the selection caret to the given point.  Also includes a convenience document context request.
- [func adjustSelection(by: BEDirectionalTextRange, completionHandler: () -> Void)](betextinput/adjustselection(by:completionhandler:).md)
  Adjusts the selection by the moving the selected range by the given `range`, in character granularity units.
- [func move(byOffset: Int)](betextinput/move(byoffset:).md)
  Adjusts the current selection by `offset` in character granularity units
- [func moveSelection(atBoundary: UITextGranularity, in: UITextStorageDirection, completionHandler: () -> Void)](betextinput/moveselection(atboundary:in:completionhandler:).md)
  Moves the caret to relative to the current position in the `direction` to the given `granularity`. The `direction` is “forward” or “backward” in accordance with the directionality of the language.
- [func selectTextForEditMenuWithLocation(inView: CGPoint, completionHandler: (Bool, String?, NSRange) -> Void)](betextinput/selecttextforeditmenuwithlocation(inview:completionhandler:).md)
  Indicates the edit menu is being shown at the given location in the text input view’s coordinate space.
### Marking text
- [var markedText: String?](betextinput/markedtext.md)
  String for the text that has been marked as part of an active input session
- [var attributedMarkedText: NSAttributedString?](betextinput/attributedmarkedtext.md)
  Attributed string for the text that has been marked as part of an active input session
- [var markedTextRange: UITextRange?](betextinput/markedtextrange.md)
  Range representing the position of the markedText.
- [var hasMarkedText: Bool](betextinput/hasmarkedtext.md)
  Indicates whether there any text is currently marked as part of an active input session
- [func setMarkedText(String?, selectedRange: NSRange)](betextinput/setmarkedtext(_:selectedrange:).md)
  Inserts the provided text and marks it to indicate that it is part of an active input session.
- [func setAttributedMarkedText(NSAttributedString?, selectedRange: NSRange)](betextinput/setattributedmarkedtext(_:selectedrange:).md)
  Inserts the provided styled text and marks it to indicate that it is part of an active input session.
- [func unmarkText()](betextinput/unmarktext.md)
  Unmarks the currently marked text
- [func isPointNearMarkedText(CGPoint) -> Bool](betextinput/ispointnearmarkedtext(_:).md)
  Returns whether a point should be considered “near” the marked text. Used to determine whether text interaction gestures near marked text should begin.
### Document context
- [func requestDocumentContext(BETextDocumentRequest, completionHandler: (BETextDocumentContext) -> Void)](betextinput/requestdocumentcontext(_:completionhandler:).md)
  Gathers context about the current document for the system
### Dictation
- [func willInsertFinalDictationResult()](betextinput/willinsertfinaldictationresult.md)
  Indicates the system is about to insert the final dictation result.
- [func replaceDictatedText(String, withText: String)](betextinput/replacedictatedtext(_:withtext:).md)
  Inserts/replaces text for a dictation.
- [func didInsertFinalDictationResult()](betextinput/didinsertfinaldictationresult.md)
  Indicates system has inserted the final dictation result
### Text alternatives
- [func alternativesForSelectedText() -> [BETextAlternatives]?](betextinput/alternativesforselectedtext.md)
  Returns the text alternatives that are available to the text input object.
- [func add(BETextAlternatives)](betextinput/add(_:).md)
  Adds text alternatives to the text input object for the current selection
- [func insert(BETextAlternatives)](betextinput/insert(_:)-6x7hd.md)
  Inserts the given `text` or one of it’s alternative texts available on `alternatives`
### Text placeholders
- [func insertTextPlaceholder(size: CGSize, completionHandler: (UITextPlaceholder) -> Void)](betextinput/inserttextplaceholder(size:completionhandler:).md)
  Inserts a placeholder object to reserve visual space during text input. If `size.height` is less than or equal to zero, then the placeholder is inline and line height. If `size.height` is greather than zero, then the placeholder is treated as a paragraph of height `size.height`.
- [func remove(UITextPlaceholder, willInsertText: Bool, completionHandler: () -> Void)](betextinput/remove(_:willinserttext:completionhandler:).md)
  Removes a placeholder object from the text input view.
### Text suggestions
- [func insert(BETextSuggestion)](betextinput/insert(_:)-5iryn.md)
  Inserts a `textSuggestion` in response to a user suggestion selection
### Geometry
- [var textInputView: UIView](betextinput/textinputview.md)
  An affiliated view that provides a coordinate system for all geometric values in this protocol.
- [var textFirstRect: CGRect](betextinput/textfirstrect.md)
  Returns a rect representing the bounds of the first line of marked text, if marked text is set.
- [var textLastRect: CGRect](betextinput/textlastrect.md)
  Returns a rect representing the bounds of the last line of marked text, if marked text is set.
- [var unobscuredContentRect: CGRect](betextinput/unobscuredcontentrect.md)
  Rect used to place UI (such as selection handles) in a location that isn’t obscurred by app UI.
- [var unscaledView: UIView](betextinput/unscaledview.md)
  View representing the web content that is agnostic of zoom state. Used to draw zoom agnostic system UI elements, such as the selection handles
- [var selectionClipRect: CGRect](betextinput/selectioncliprect.md)
  Rect representing the bounds of editable elements, used to ensure and UI don’t overflow outside them
- [func autoscroll(to: CGPoint)](betextinput/autoscroll(to:).md)
  Indicates autoscrolling has been triggered by a text interaction gesture.
- [func cancelAutoscroll()](betextinput/cancelautoscroll.md)
  Indicates autoscrolling is complete.
### Instance Methods
- [func keyboardWillDismiss()](betextinput/keyboardwilldismiss.md)
  Called when the user has requested the keyboard to dismiss itself.
- [func removeTextAlternatives()](betextinput/removetextalternatives.md)
  Removes text alternatives from the text input object for the current selection

## Relationships

### Inherits From
- [BEResponderEditActions](berespondereditactions.md)
- [BETextSelectionDirectionNavigation](betextselectiondirectionnavigation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIKeyInput](../UIKit/UIKeyInput.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UITextInputTraits](../UIKit/UITextInputTraits.md)

## See Also

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)
  Process keyboard interactions asynchronously in your iOS browser app’s text view.
- [Supporting extended text interactions](support-extended-text-interactions.md)
  Share content, add replacement shortcuts, and perform other rich actions in browser text views.
- [protocol BETextInputDelegate](betextinputdelegate.md)
  A delegate protocol that a browser text view uses to notify the text system of changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput)*