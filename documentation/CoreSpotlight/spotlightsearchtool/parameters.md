# parameters

**Framework**: Core Spotlight  
**Kind**: property

Dynamic schema: use the native tool’s schema based on capabilities.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var parameters: GenerationSchema { get }
```

#### Discussion

For `.rag(profile)` we dispatch to the domain-specific schema so the model only sees fields relevant to that domain.  Returning the generic `RAGSearchArguments` for every domain inflates the prompt past on-device’s context window and ignores the developer’s explicit domain selection.

## See Also

- [var includesSchemaInInstructions: Bool](spotlightsearchtool/includesschemaininstructions.md)
  On-device uses includesSchemaInInstructions: true; .dynamic uses false (schema in compact notation prose instead).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/parameters)*