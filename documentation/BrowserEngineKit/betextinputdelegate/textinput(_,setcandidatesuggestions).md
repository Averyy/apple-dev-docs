# textInput(_:setCandidateSuggestions:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides text suggestions to the system.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func textInput(_ textInput: any BETextInput, setCandidateSuggestions suggestions: [BETextSuggestion]?)
```

```objc
- (void) textInput:(id<BETextInput>) textInput setCandidateSuggestions:(NSArray<BETextSuggestion *> *) suggestions;
```

#### Discussion

For example, suggestions could include data list elements or AutoFill candidates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinputdelegate/textinput(_:setcandidatesuggestions:))*