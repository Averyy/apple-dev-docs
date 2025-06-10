# AnalysisContext

**Framework**: Speech  
**Kind**: class

Contextual information that may be shared among analyzers.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final class AnalysisContext
```

## Topics

### Structures
- [AnalysisContext.ContextualStringsTag](analysiscontext/contextualstringstag.md)
- [AnalysisContext.UserDataTag](analysiscontext/userdatatag.md)
### Initializers
- [init()](analysiscontext/init.md)
### Instance Properties
- [var contextualStrings: [AnalysisContext.ContextualStringsTag : [String]]](analysiscontext/contextualstrings.md)
  A dictionary of supplemental vocabulary words grouped by tag.
- [var userData: [AnalysisContext.UserDataTag : any Sendable]](analysiscontext/userdata.md)
  A dictionary of application-specific contextual information.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class SFCustomLanguageModelData](sfcustomlanguagemodeldata.md)
  An object that generates and exports custom language model training data.
- [class SFSpeechLanguageModel](sfspeechlanguagemodel.md)
  A language model built from custom training data.
- [SFSpeechLanguageModel.Configuration](sfspeechlanguagemodel/configuration.md)
  An object describing the location of a custom language model and specialized vocabulary.
- [protocol DataInsertable](datainsertable.md)
  A protocol supporting the custom language model training data result builder.
- [protocol TemplateInsertable](templateinsertable.md)
  A protocol supporting the custom language model training data result builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/analysiscontext)*