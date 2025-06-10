# parameters

**Framework**: Foundation Models  
**Kind**: property  
**Required**: Yes

A schema for the parameters this tool accepts.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var parameters: GenerationSchema { get }
```

## See Also

- [var description: String](tool/description.md)
  A natural language description of when and how to use the tool.
- [var includesSchemaInInstructions: Bool](tool/includesschemaininstructions.md)
  If true, the model’s name, description, and parameters schema will be injected into the instructions of sessions that leverage this tool.
- [var name: String](tool/name.md)
  A unique name for the tool, such as “get_weather”, “toggleDarkMode”, or “search contacts”.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/tool/parameters)*