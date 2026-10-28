# parameters

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

The schema for the parameters this tool accepts.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var parameters: GenerationSchema { get }
```

## Discussion

The Spotlight search tool implements this property as part of its conformance to the [`Tool`](../../FoundationModels/tool.md) protocol.

## See Also

### Getting tool-specific properties
- [var includesSchemaInInstructions: Bool](./includesschemaininstructions.md)
  A Boolean value that indicates whether to inject the model’s name, description, and parameters schema into the instructions of sessions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/parameters)*