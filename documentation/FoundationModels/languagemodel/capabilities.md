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

If a developer attempts to use capabilities that your model does not support, then the system will automatically throw an error for you instead of calling `respond(to:)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodel/capabilities)*