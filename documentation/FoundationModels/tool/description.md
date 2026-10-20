# description

**Framework**: Foundation Models  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A natural language description of when and how to use the tool.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
var description: String { get }
```

## See Also

### Inspecting a tool
- [var name: String](./name.md)
  A unique name for the tool.
- [var parameters: GenerationSchema](./parameters.md)
  A schema for the parameters this tool accepts.
- [var includesSchemaInInstructions: Bool](./includesschemaininstructions.md)
  A Boolean value that indicates whether the framework includes this tool’s definition in the session’s instructions.
- [typealias SessionProperty](./sessionproperty.md)
  A property wrapper that provides access to a session property from within a tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/tool/description)*