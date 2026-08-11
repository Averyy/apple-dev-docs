# Tool.SessionProperty

**Framework**: Foundation Models  
**Kind**: typealias

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
typealias SessionProperty = LanguageModelSession.SessionProperty
```

## See Also

- [var name: String](tool/name.md)
  A unique name for the tool, such as “get_weather”, “toggleDarkMode”, or “search contacts”.
- [var description: String](tool/description.md)
  A natural language description of when and how to use the tool.
- [var parameters: GenerationSchema](tool/parameters.md)
  A schema for the parameters this tool accepts.
- [var includesSchemaInInstructions: Bool](tool/includesschemaininstructions.md)
  A Boolean value that indicates whether the tool’s name, description, and parameters schema are injected into the instructions of sessions that leverage this tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/tool/sessionproperty)*