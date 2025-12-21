# includesSchemaInInstructions

**Framework**: Foundation Models  
**Kind**: property  
**Required**: Yes

If true, the model’s name, description, and parameters schema will be injected into the instructions of sessions that leverage this tool.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var includesSchemaInInstructions: Bool { get }
```

#### Discussion

The default implementation is `true`

> **Note**: This should only be `false` if the model has been trained to have innate knowledge of this tool. For zero-shot prompting, it should always be `true`.

## See Also

- [var description: String](tool/description.md)
  A natural language description of when and how to use the tool.
- [var name: String](tool/name.md)
  A unique name for the tool, such as “get_weather”, “toggleDarkMode”, or “search contacts”.
- [var parameters: GenerationSchema](tool/parameters.md)
  A schema for the parameters this tool accepts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/tool/includesschemaininstructions)*