# BETextInputDelegate

**Framework**: BrowserEngineKit  
**Kind**: protocol

A delegate protocol that a browser text view uses to notify the text system of changes.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS ?+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
protocol BETextInputDelegate
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Overview

You don’t conform to `BETextInputDelegate` in your classes, or implement its methods. The operating system creates objects that conform to this protocol and sets them as the [`asyncInputDelegate`](betextinput/asyncinputdelegate.md) on your browser’s custom text views.

## Topics

### Text selection
- [func selectionWillChange(for: any BETextInput)](betextinputdelegate/selectionwillchange(for:).md)
  Tells the system when the selection is about to change in the document.
- [func selectionDidChange(for: any BETextInput)](betextinputdelegate/selectiondidchange(for:).md)
  Tells the system when the selection has changed in the document.
### Deferring actions to the text system
- [func shouldDeferEventHandlingToSystem(for: any BETextInput, context: BEKeyEntryContext) -> Bool](betextinputdelegate/shoulddefereventhandlingtosystem(for:context:).md)
  Defers the key event to the system and returns whether the key event was handled.
- [func textInput(any BETextInput, deferReplaceTextActionToSystem: Any)](betextinputdelegate/textinput(_:deferreplacetextactiontosystem:).md)
  Defers a replace text action to the ssytem.
### Providing completion suggestions
- [func textInput(any BETextInput, setCandidateSuggestions: [BETextSuggestion]?)](betextinputdelegate/textinput(_:setcandidatesuggestions:).md)
  Provides text suggestions to the system.
### Removing stored context information
- [func invalidateTextEntryContext(for: any BETextInput)](betextinputdelegate/invalidatetextentrycontext(for:).md)
  Tells the system the text entry context has changed and that text entry UI’s need to be refreshed.

## See Also

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)
  Process keyboard interactions asynchronously in your iOS browser app’s text view.
- [Supporting extended text interactions](support-extended-text-interactions.md)
  Share content, add replacement shortcuts, and perform other rich actions in browser text views.
- [protocol BETextInput](betextinput.md)
  A protocol to which text views conform to asynchronously integrate with the text system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinputdelegate)*