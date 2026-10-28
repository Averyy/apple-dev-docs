# includesSchemaInInstructions

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to inject the model’s name, description, and parameters schema into the instructions of sessions.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var includesSchemaInInstructions: Bool { get }
```

## Discussion

The Spotlight search tool implements this property as part of its conformance to the [`Tool`](../../FoundationModels/tool.md) protocol.

## See Also

### Getting tool-specific properties
- [var parameters: GenerationSchema](./parameters.md)
  The schema for the parameters this tool accepts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/includesschemaininstructions)*