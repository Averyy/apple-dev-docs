# Text interaction

**Framework**: BrowserEngineKit

Integrate your web browser engine asynchronously with the text system.

## Topics

### Custom text views
- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)
  Process keyboard interactions asynchronously in your iOS browser app’s text view.
- [Supporting extended text interactions](support-extended-text-interactions.md)
  Share content, add replacement shortcuts, and perform other rich actions in browser text views.
- [protocol BETextInput](betextinput.md)
  A protocol for asynchronous text views that integrate with the text system.
- [protocol BETextInputDelegate](betextinputdelegate.md)
  A delegate protocol that a browser text view uses to notify the text system of changes.
### Interaction responses
- [class BETextInteraction](betextinteraction.md)
  An interaction you add to a text view to support extended text gestures.
- [protocol BETextInteractionDelegate](betextinteractiondelegate.md)
  A set of methods that informs you about selection changes in text views.
- [protocol BEResponderEditActions](berespondereditactions.md)
  A set of methods that defines extended interactions in browser text views.
- [enum BEGestureType](begesturetype.md)
  The types of touch gestures that operate on input text.
- [protocol BEResponderEditActions](berespondereditactions.md)
  A set of methods that defines extended interactions in browser text views.
### Text selection
- [protocol BETextSelectionDirectionNavigation](betextselectiondirectionnavigation.md)
  A protocol that defines methods for cursor and selection adjustments.
- [struct BESelectionFlags](beselectionflags.md)
  Flags that indicate different states or characteristics of a text selection.
- [enum BESelectionTouchPhase](beselectiontouchphase.md)
  The different phases of touch interaction during text selection operations.
### Keyboard input
- [class BEKeyEntry](bekeyentry.md)
  A class that represents a keyboard event in the text system.
- [class BEKeyEntryContext](bekeyentrycontext.md)
  A class that describes a key event and the text document with which the event is associated.
- [enum BEKeyModifierFlags](bekeymodifierflags.md)
  An enumeration that records the state of the shift-modifier keys.
### Replacements and AutoFill
- [class BEAutoFillTextSuggestion](beautofilltextsuggestion.md)
  A suggestion object that provides AutoFill text content for web form fields based on a person’s usage patterns.
- [class BETextAlternatives](betextalternatives.md)
  An object that provides alternative text suggestions for a person’s text selection.
- [class BETextDocumentContext](betextdocumentcontext.md)
  Information about the text surrounding a selection in a document.
- [class BETextDocumentRequest](betextdocumentrequest.md)
  A description of the contextual information that a text document request retrieves.
- [BETextDocumentRequest.Options](betextdocumentrequest/options-swift.struct.md)
  Options that describe the contextual information for a text document request.
- [class BETextSuggestion](betextsuggestion.md)
  A text suggestion to insert into a document.
- [struct BETextReplacementOptions](betextreplacementoptions.md)
  Options that determine the way your app processes text in webpages.
### Information about text
- [protocol BEExtendedTextInputTraits](beextendedtextinputtraits.md)
  An object that customizes text-input appearance and behavior beyond the standard system traits.
- [struct BEDirectionalTextRange](bedirectionaltextrange.md)
  Modifications to text length based on its offset.

## See Also

- [View and input coordination](view-coordination.md)
  Display content in the browser’s UI that an extension renders.
- [class BEWebAppManifest](bewebappmanifest.md)
  An object that represents a web app manifest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/text-interaction)*