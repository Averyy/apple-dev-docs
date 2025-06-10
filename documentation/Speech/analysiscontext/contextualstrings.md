# contextualStrings

**Framework**: Speech  
**Kind**: property

A dictionary of supplemental vocabulary words grouped by tag.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final var contextualStrings: [AnalysisContext.ContextualStringsTag : [String]] { get set }
```

#### Discussion

Use the tag to easily swap out some of the strings while leaving others in place. The framework provides a predefined [`general`](analysiscontext/contextualstringstag/general.md) tag.

## See Also

- [var userData: [AnalysisContext.UserDataTag : any Sendable]](analysiscontext/userdata.md)
  A dictionary of application-specific contextual information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/analysiscontext/contextualstrings)*