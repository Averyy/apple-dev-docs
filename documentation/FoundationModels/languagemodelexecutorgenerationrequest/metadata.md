# metadata

**Framework**: Foundation Models  
**Kind**: property

Metadata to attach to the request

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var metadata: [String : any Sendable & Codable & Equatable]
```

## See Also

- [var id: UUID](languagemodelexecutorgenerationrequest/id.md)
  A request id for logging and tracing purposes
- [var contextOptions: ContextOptions](languagemodelexecutorgenerationrequest/contextoptions.md)
  Settings that configure how the model is prompted
- [var enabledToolDefinitions: [Transcript.ToolDefinition]](languagemodelexecutorgenerationrequest/enabledtooldefinitions.md)
  The subset tool definitions that the model is allowed to call
- [var generationOptions: GenerationOptions](languagemodelexecutorgenerationrequest/generationoptions.md)
  Generation options that control sampling behavior
- [var schema: GenerationSchema?](languagemodelexecutorgenerationrequest/schema.md)
  An optional schema dictating the required output format
- [var transcript: Transcript](languagemodelexecutorgenerationrequest/transcript.md)
  A transcript to generate the next entry for


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationrequest/metadata)*