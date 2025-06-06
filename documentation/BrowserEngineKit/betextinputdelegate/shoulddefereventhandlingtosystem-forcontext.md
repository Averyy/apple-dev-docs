# shouldDeferEventHandlingToSystem(for:context:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Defers the key event to the system and returns whether the key event was handled.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS ?+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func shouldDeferEventHandlingToSystem(for textInput: any BETextInput, context keyEventContext: BEKeyEntryContext) -> Bool
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Return Value

`true` if the system handles the key event; `false` otherwise.

#### Discussion

For example, the system will handle key events for character insertions, deletions, key commands, and more.

Notify the text system that your web browser’s custom text view isn’t handling key events.

#### Overview

Call this method on your [`asyncInputDelegate`](betextinput/asyncinputdelegate.md) when your [`BETextInput`](betextinput.md) view doesn’t handle a key event, and you pass `false` to the `completionHandler` for [`handleKeyEntry(_:completionHandler:)`](betextinput/handlekeyentry(_:completionhandler:).md).

## Parameters

- `textInput`: The view for which the system needs to take over event handling.
- `keyEventContext`: Information about the key event and the document it targets.

## See Also

- [func textInput(any BETextInput, deferReplaceTextActionToSystem: Any)](betextinputdelegate/textinput(_:deferreplacetextactiontosystem:).md)
  Defers a replace text action to the ssytem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinputdelegate/shoulddefereventhandlingtosystem(for:context:))*