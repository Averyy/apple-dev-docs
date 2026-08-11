# capabilities

**Framework**: Foundation Models  
**Kind**: property  
**Required**: Yes

The capabilities of this language model.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var capabilities: LanguageModelCapabilities { get }
```

#### Discussion

If a developer attempts to use capabilities that your model does not support, the system automatically throws an error for you instead of calling a respond method, like [`respond(to:options:)`](languagemodelsession/respond(to:options:)-6a2gb.md) or [`streamResponse(to:options:)`](languagemodelsession/streamresponse(to:options:)-2nlni.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodel/capabilities)*