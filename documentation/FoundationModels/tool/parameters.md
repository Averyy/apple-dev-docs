# parameters

**Framework**: Foundation Models  
**Kind**: property  
**Required**: Yes

A schema for the parameters this tool accepts.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
var parameters: GenerationSchema { get }
```

## See Also

- [var name: String](tool/name.md)
  A unique name for the tool, such as “get_weather”, “toggleDarkMode”, or “search contacts”.
- [var description: String](tool/description.md)
  A natural language description of when and how to use the tool.
- [var includesSchemaInInstructions: Bool](tool/includesschemaininstructions.md)
  A Boolean value that indicates whether the tool’s name, description, and parameters schema are injected into the instructions of sessions that leverage this tool.
- [typealias SessionProperty](tool/sessionproperty.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/tool/parameters)*