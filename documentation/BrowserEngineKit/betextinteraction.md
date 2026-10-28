# BETextInteraction

**Framework**: BrowserEngineKit  
**Kind**: class  
**Role**: Class

An interaction you add to a text view to support extended text gestures.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
@MainActor
class BETextInteraction
```

```objc
@interface BETextInteraction : NSObject
```

## Mentions

- [Integrating custom browser text views with UIKit](./integrating-custom-browser-text-views-with-uikit.md)
- [Supporting extended text interactions](./support-extended-text-interactions.md)

## Overview

Add a `BETextInteraction` object to your browser text view’s [`textInputView`](./betextinput/textinputview.md). When your browser text view receives text-interaction actions, call the methods on this object to invoke the standard system behavior.

## Topics

### Text selection
- [var delegate: (any BETextInteractionDelegate)?](./betextinteraction/delegate.md)
  A delegate object that the interaction notifies when the system changes the text selection.
- [protocol BETextInteractionDelegate](./betextinteractiondelegate.md)
  A set of methods that informs you about selection changes in text views.
- [var textSelectionDisplayInteraction: UITextSelectionDisplayInteraction](./betextinteraction/textselectiondisplayinteraction.md)
  An interaction that manages the system’s text-selection UI.
- [func selectionBoundaryAdjusted(to: CGPoint, touchPhase: BESelectionTouchPhase, flags: BESelectionFlags)](./betextinteraction/selectionboundaryadjusted%28to,touchphase,flags%29.md)
  Notifies the system after the text view adjusts its selection.
- [func selectionChangedWithGesture(at: CGPoint, gesture: BEGestureType, state: UIGestureRecognizer.State, flags: BESelectionFlags)](./betextinteraction/selectionchangedwithgesture%28at,gesture,state,flags%29.md)
  Notifies the system that the text view changed its selection.
### Menus
- [func presentEditMenuForSelection()](./betextinteraction/presenteditmenuforselection%28%29.md)
  Presents an edit menu for the current text selection.
- [func dismissEditMenuForSelection()](./betextinteraction/dismisseditmenuforselection%28%29.md)
  Dismisses the edit menu for the current text selection.
- [var contextMenuInteraction: UIContextMenuInteraction](./betextinteraction/contextmenuinteraction.md)
  An interaction you use to work with the text view’s context menu.
- [var contextMenuInteractionDelegate: (any UIContextMenuInteractionDelegate)?](./betextinteraction/contextmenuinteractiondelegate.md)
  The delegate for the context menu interaction associated with this text interaction.
### Text replacements
- [func addShortcut(forText: String, from: CGRect)](./betextinteraction/addshortcut%28fortext,from%29.md)
  Presents UI for a person to add a text-replacement shortcut to the keyboard dictionary.
- [func showReplacements(forText: String)](./betextinteraction/showreplacements%28fortext%29.md)
  Displays inline text replacements for the current selection.
### Sharing and defining text
- [func share(text: String, from: CGRect)](./betextinteraction/share%28text,from%29.md)
  Presents standard UI for someone to share text from a browser text view.
- [func showDictionary(forTextInContext: String, definingTextInRange: NSRange, from: CGRect)](./betextinteraction/showdictionary%28fortextincontext,definingtextinrange,from%29.md)
  Presents a dictionary definition for the supplied text.
### Translation and transliteration
- [func translate(text: String, from: CGRect)](./betextinteraction/translate%28text,from%29.md)
  Presents a translation of the text.
- [func transliterateChinese(forText: String)](./betextinteraction/transliteratechinese%28fortext%29.md)
  Converts text between traditional and simplified Chinese.
### UI updates
- [func editabilityChanged()](./betextinteraction/editabilitychanged%28%29.md)
  Tells the system that the document’s editability status has changed.
- [func refreshKeyboardUI()](./betextinteraction/refreshkeyboardui%28%29.md)
  Tells the system to refresh the keyboard UI.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [UIInteraction](../UIKit/uiinteraction.md)

## See Also

### Interaction responses
- [protocol BETextInteractionDelegate](./betextinteractiondelegate.md)
  A set of methods that informs you about selection changes in text views.
- [protocol BEResponderEditActions](./berespondereditactions.md)
  A set of methods that defines extended interactions in browser text views.
- [enum BEGestureType](./begesturetype.md)
  The types of touch gestures that operate on input text.
- [protocol BEResponderEditActions](./berespondereditactions.md)
  A set of methods that defines extended interactions in browser text views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinteraction)*