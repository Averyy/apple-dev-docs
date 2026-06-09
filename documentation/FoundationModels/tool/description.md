# description

**Framework**: Foundation Models  
**Kind**: property  
**Required**: Yes

A natural language description of when and how to use the tool.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
var description: String { get }
```

## See Also

- [var name: String](tool/name.md)
  A unique name for the tool, such as “get_weather”, “toggleDarkMode”, or “search contacts”.
- [var parameters: GenerationSchema](tool/parameters.md)
  A schema for the parameters this tool accepts.
- [var includesSchemaInInstructions: Bool](tool/includesschemaininstructions.md)
  If true, the model’s name, description, and parameters schema will be injected into the instructions of sessions that leverage this tool.
- [typealias SessionProperty](tool/sessionproperty.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/tool/description)*