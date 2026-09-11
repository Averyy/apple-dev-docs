# capabilities

**Framework**: Foundation Models  
**Kind**: property  
**Required**: Yes

The capabilities of this language model.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var capabilities: LanguageModelCapabilities { get }
```

#### Discussion

If a developer attempts to use capabilities that your model does not support, the system automatically throws an error for you instead of calling a respond method, like [`respond(to:options:)`](languagemodelsession/respond(to:options:)-6a2gb.md) or [`streamResponse(to:options:)`](languagemodelsession/streamresponse(to:options:)-2nlni.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodel/capabilities)*