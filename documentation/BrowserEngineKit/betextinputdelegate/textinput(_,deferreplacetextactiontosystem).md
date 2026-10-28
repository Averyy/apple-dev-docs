# textInput(_:deferReplaceTextActionToSystem:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Defers a replace text action to the ssytem.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func textInput(_ textInput: any BETextInput, deferReplaceTextActionToSystem sender: Any)
```

```objc
- (void) textInput:(id<BETextInput>) textInput deferReplaceTextActionToSystem:(id) sender;
```

## Discussion

When handling the replace: action, use this method to defer the replacement to the system.

For example, a replacement could be deferred after it is selected from the autocorrect replacements list.

## See Also

### Deferring actions to the text system
- [func shouldDeferEventHandlingToSystem(for: any BETextInput, context: BEKeyEntryContext) -> Bool](./shoulddefereventhandlingtosystem%28for,context%29.md)
  Notify the text system that your web browser’s custom text view isn’t handling key events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinputdelegate/textinput(_:deferreplacetextactiontosystem:))*