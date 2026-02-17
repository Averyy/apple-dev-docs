# contextualStrings

**Framework**: Speech  
**Kind**: property

Words or phrases, grouped by tag, that should be recognized even if they are not in the system vocabulary.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final var contextualStrings: [AnalysisContext.ContextualStringsTag : [String]] { get set }
```

#### Discussion

With the [`DictationTranscriber`](dictationtranscriber.md) module, you can use this property to specify short custom phrases that are unique to your app. You might include phrases with the names of characters, products, or places that are specific to your app. Assigning custom phrases to this property improves the likelihood of those phrases being recognized.

Keep phrases relatively brief, limiting them to one or two words whenever possible. Lengthy phrases are less likely to be recognized. In addition, try to limit each phrase to something the user can say without pausing. Limit the total number of phrases across all tags to no more than 100.

You might also include domain-specific terminology or unusual or made-up words, but the system may not estimate their pronounciation correctly. You can provide a custom language model with correct pronounciations to [`DictationTranscriber`](dictationtranscriber.md) by initializing it with a [`customizedLanguage(modelConfiguration:)`](dictationtranscriber/contenthint/customizedlanguage(modelconfiguration:).md) content hint.

Use the tag to easily swap out some of the strings while leaving others in place. The framework provides a predefined [`general`](analysiscontext/contextualstringstag/general.md) tag.

## See Also

- [AnalysisContext.ContextualStringsTag](analysiscontext/contextualstringstag.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/analysiscontext/contextualstrings)*