# AnalysisContext.ContextualStringsTag

**Framework**: Speech  
**Kind**: struct

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
- [init(AnalysisContext.ContextualStringsTag.RawValue)](analysiscontext/contextualstringstag/init(_:).md)
### Predefined tags
- [static let general: AnalysisContext.ContextualStringsTag](analysiscontext/contextualstringstag/general.md)
  A predefined tag for applications that have no need to distinguish between sets of contextual strings.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var contextualStrings: [AnalysisContext.ContextualStringsTag : [String]]](analysiscontext/contextualstrings.md)
  Words or phrases, grouped by tag, that should be recognized even if they are not in the system vocabulary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/analysiscontext/contextualstringstag)*