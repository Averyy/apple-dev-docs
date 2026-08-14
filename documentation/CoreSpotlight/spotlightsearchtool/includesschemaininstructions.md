# includesSchemaInInstructions

**Framework**: Core Spotlight  
**Kind**: property

A Boolean value that indicates whether to inject the model’s name, description, and parameters schema into the instructions of sessions.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var includesSchemaInInstructions: Bool { get }
```

#### Discussion

The Spotlight search tool implements this property as part of its conformance to the [`Tool`](https://developer.apple.com/documentation/foundationmodels/tool) protocol.

## See Also

- [var parameters: GenerationSchema](spotlightsearchtool/parameters.md)
  The schema for the parameters this tool accepts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/includesschemaininstructions)*