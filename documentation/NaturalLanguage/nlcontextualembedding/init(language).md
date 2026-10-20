# init(language:)

**Framework**: Natural Language  
**Kind**: init  
**Role**: Initializer

Creates a contextual embedding from a language.

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
init?(language: NLLanguage)
```

```objc
+ (NLContextualEmbedding *) contextualEmbeddingWithLanguage:(NLLanguage) language;
```

#### Discussion

The language the framework uses to find the most recent embedding suitable for the value you specify.

## Parameters

- `language`: The language the framework uses to find the most recent embedding suitable for the value you specify.

## See Also

### Creating a contextual embedding
- [convenience init?(modelIdentifier: String)](./init%28modelidentifier%29.md)
  Creates a contextual embedding from a model identifier.
- [init?(script: NLScript)](./init%28script%29.md)
  Creates a contextual embedding from a script.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlcontextualembedding/init(language:))*