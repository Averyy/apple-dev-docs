# contextualStrings

**Framework**: Speech  
**Kind**: property

A dictionary of supplemental vocabulary words grouped by tag.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final var contextualStrings: [AnalysisContext.ContextualStringsTag : [String]] { get set }
```

#### Discussion

Use the tag to easily swap out some of the strings while leaving others in place. The framework provides a predefined [`general`](analysiscontext/contextualstringstag/general.md) tag.

## See Also

- [AnalysisContext.ContextualStringsTag](analysiscontext/contextualstringstag.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/analysiscontext/contextualstrings)*