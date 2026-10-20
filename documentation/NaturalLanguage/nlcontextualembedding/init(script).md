# init(script:)

**Framework**: Natural Language  
**Kind**: init  
**Role**: Initializer

Creates a contextual embedding from a script.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init?(script: NLScript)
```

```objc
+ (NLContextualEmbedding *) contextualEmbeddingWithScript:(NLScript) script;
```

## Parameters

- `script`: The writing system the framework uses to find the most suitable system embedding for the value you specify; for example, Chinese or Latin.

## See Also

### Creating a contextual embedding
- [convenience init?(modelIdentifier: String)](./init%28modelidentifier%29.md)
  Creates a contextual embedding from a model identifier.
- [init?(language: NLLanguage)](./init%28language%29.md)
  Creates a contextual embedding from a language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlcontextualembedding/init(script:))*