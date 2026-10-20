# contextSize

**Framework**: Foundation Models  
**Kind**: property  
**Role**: Instance Property

The maximum context size in tokens that the model supports.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@backDeployed(before: iOS 26.4, macOS 26.4, visionOS 26.4)
final var contextSize: Int { get }
```

## Mentions

- [Managing the context window](../managing-the-context-window.md)

#### Return Value

The context size, in tokens.

#### Discussion

The context size represents the total number of tokens that can be used in a single session, including both input prompts and generated responses.

> **Throws**: An error if the context size cannot be determined. Typically this is due to the model not being available or Apple Intelligence is disabled.

## See Also

### Inspecting model capabilities
- [var supportedLanguages: Set<Locale.Language>](./supportedlanguages.md)
  Languages that the model supports.
- [func supportsLocale(Locale) -> Bool](./supportslocale%28_%29.md)
  Returns a Boolean value that indicates whether the given locale is supported by the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/contextsize)*