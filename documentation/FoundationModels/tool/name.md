# name

**Framework**: Foundation Models  
**Kind**: property  
**Required**: Yes

A unique name for the tool.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
var name: String { get }
```

#### Discussion

Use whichever style reads best in your codebase, such as `get_weather`, `toggleDarkMode`, or `search contacts`.

## See Also

- [var description: String](tool/description.md)
  A natural language description of when and how to use the tool.
- [var parameters: GenerationSchema](tool/parameters.md)
  A schema for the parameters this tool accepts.
- [var includesSchemaInInstructions: Bool](tool/includesschemaininstructions.md)
  A Boolean value that indicates whether the framework includes this tool’s definition in the session’s instructions.
- [typealias SessionProperty](tool/sessionproperty.md)
  A property wrapper that provides access to a session property from within a tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/tool/name)*