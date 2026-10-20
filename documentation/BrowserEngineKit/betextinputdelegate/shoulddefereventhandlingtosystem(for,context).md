# shouldDeferEventHandlingToSystem(for:context:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Notify the text system that your web browser’s custom text view isn’t handling key events.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func shouldDeferEventHandlingToSystem(for textInput: any BETextInput, context keyEventContext: BEKeyEntryContext) -> Bool
```

```objc
- (BOOL) shouldDeferEventHandlingToSystemForTextInput:(id<BETextInput>) textInput context:(BEKeyEntryContext *) keyEventContext;
```

## Mentions

- [Integrating custom browser text views with UIKit](../integrating-custom-browser-text-views-with-uikit.md)

#### Return Value

`true` if the system handles the key event; `false` otherwise.

#### Discussion

Call this method on your [`asyncInputDelegate`](../betextinput/asyncinputdelegate.md) when your [`BETextInput`](../betextinput.md) view doesn’t handle a key event, and you pass `false` to the `completionHandler` for [`handleKeyEntry(_:completionHandler:)`](../betextinput/handlekeyentry%28_,completionhandler%29.md).

## Parameters

- `textInput`: The view for which the system needs to take over event handling.
- `keyEventContext`: Information about the key event and the document it targets.

## See Also

### Deferring actions to the text system
- [func textInput(any BETextInput, deferReplaceTextActionToSystem: Any)](./textinput%28_,deferreplacetextactiontosystem%29.md)
  Defers a replace text action to the ssytem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinputdelegate/shoulddefereventhandlingtosystem(for:context:))*