# AnalysisContext

**Framework**: Speech  
**Kind**: class

Contextual information that may be shared among analyzers.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final class AnalysisContext
```

## Topics

### Creating a context
- [init()](analysiscontext/init.md)
### Providing textual context
- [var contextualStrings: [AnalysisContext.ContextualStringsTag : [String]]](analysiscontext/contextualstrings.md)
  A dictionary of supplemental vocabulary words grouped by tag.
- [AnalysisContext.ContextualStringsTag](analysiscontext/contextualstringstag.md)
### Preserving app-specific context
- [var userData: [AnalysisContext.UserDataTag : any Sendable]](analysiscontext/userdata.md)
  A dictionary of application-specific contextual information.
- [AnalysisContext.UserDataTag](analysiscontext/userdatatag.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class SFSpeechLanguageModel](sfspeechlanguagemodel.md)
  A language model built from custom training data.
- [SFSpeechLanguageModel.Configuration](sfspeechlanguagemodel/configuration.md)
  An object describing the location of a custom language model and specialized vocabulary.
- [class SFCustomLanguageModelData](sfcustomlanguagemodeldata.md)
  An object that generates and exports custom language model training data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/analysiscontext)*