# enabledToolDefinitions

**Framework**: Foundation Models  
**Kind**: property  
**Role**: Instance Property

The subset of tool definitions that the model is allowed to call.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var enabledToolDefinitions: [Transcript.ToolDefinition]
```

## See Also

### Configuring a generation request
- [var id: UUID](./id.md)
  A request id for logging and tracing purposes.
- [var metadata: [String : GeneratedContent]](./metadata.md)
  Metadata to attach to the request.
- [var contextOptions: ContextOptions](./contextoptions.md)
  Settings that configure how the model is prompted.
- [var generationOptions: GenerationOptions](./generationoptions.md)
  Generation options that control sampling behavior.
- [var schema: GenerationSchema?](./schema.md)
  An optional schema dictating the required output format.
- [var transcript: Transcript](./transcript.md)
  A transcript to generate the next entry for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationrequest/enabledtooldefinitions)*