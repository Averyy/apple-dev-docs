# contextOptions

**Framework**: Foundation Models  
**Kind**: property

Settings that configure how the model is prompted

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var contextOptions: ContextOptions
```

## See Also

- [var id: UUID](languagemodelexecutorgenerationrequest/id.md)
  A request id for logging and tracing purposes
- [var metadata: [String : GeneratedContent]](languagemodelexecutorgenerationrequest/metadata.md)
  Metadata to attach to the request
- [var enabledToolDefinitions: [Transcript.ToolDefinition]](languagemodelexecutorgenerationrequest/enabledtooldefinitions.md)
  The subset tool definitions that the model is allowed to call
- [var generationOptions: GenerationOptions](languagemodelexecutorgenerationrequest/generationoptions.md)
  Generation options that control sampling behavior
- [var schema: GenerationSchema?](languagemodelexecutorgenerationrequest/schema.md)
  An optional schema dictating the required output format
- [var transcript: Transcript](languagemodelexecutorgenerationrequest/transcript.md)
  A transcript to generate the next entry for


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationrequest/contextoptions)*