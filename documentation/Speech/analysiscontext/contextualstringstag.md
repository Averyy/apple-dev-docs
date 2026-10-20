# AnalysisContext.ContextualStringsTag

**Framework**: Speech  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct ContextualStringsTag
```

## Topics

### Creating a tag
- [init(AnalysisContext.ContextualStringsTag.RawValue)](./contextualstringstag/init%28_%29.md)
### Predefined tags
- [static let general: AnalysisContext.ContextualStringsTag](./contextualstringstag/general.md)
  A predefined tag for applications that have no need to distinguish between sets of contextual strings.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Providing textual context
- [var contextualStrings: [AnalysisContext.ContextualStringsTag : [String]]](./contextualstrings.md)
  Words or phrases, grouped by tag, that should be recognized even if they are not in the system vocabulary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/analysiscontext/contextualstringstag)*