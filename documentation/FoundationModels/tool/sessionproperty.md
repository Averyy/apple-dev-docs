# Tool.SessionProperty

**Framework**: Foundation Models  
**Kind**: typealias

A property wrapper that provides access to a session property from within a tool.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
typealias SessionProperty = LanguageModelSession.SessionProperty
```

## See Also

- [var name: String](tool/name.md)
  A unique name for the tool.
- [var description: String](tool/description.md)
  A natural language description of when and how to use the tool.
- [var parameters: GenerationSchema](tool/parameters.md)
  A schema for the parameters this tool accepts.
- [var includesSchemaInInstructions: Bool](tool/includesschemaininstructions.md)
  A Boolean value that indicates whether the framework includes this tool’s definition in the session’s instructions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/tool/sessionproperty)*