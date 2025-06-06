# textInput(_:deferReplaceTextActionToSystem:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Defers a replace text action to the ssytem.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS ?+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func textInput(_ textInput: any BETextInput, deferReplaceTextActionToSystem sender: Any)
```

#### Discussion

When handling the replace: action, use this method to defer the replacement to the system.

For example, a replacement could be deferred after it is selected from the autocorrect replacements list.

## See Also

- [func shouldDeferEventHandlingToSystem(for: any BETextInput, context: BEKeyEntryContext) -> Bool](betextinputdelegate/shoulddefereventhandlingtosystem(for:context:).md)
  Defers the key event to the system and returns whether the key event was handled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinputdelegate/textinput(_:deferreplacetextactiontosystem:))*