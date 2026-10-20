# invalidateTextEntryContext(for:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the system the text entry context has changed and that text entry UI’s need to be refreshed.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func invalidateTextEntryContext(for textInput: any BETextInput)
```

```objc
- (void) invalidateTextEntryContextForTextInput:(id<BETextInput>) textInput;
```

#### Discussion

This is a costly operation and should only used with intention.  For example, when switching focus between different elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinputdelegate/invalidatetextentrycontext(for:))*