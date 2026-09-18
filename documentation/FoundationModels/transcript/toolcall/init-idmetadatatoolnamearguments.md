# init(id:metadata:toolName:arguments:)

**Framework**: Foundation Models  
**Kind**: init

Creates a tool call that invokes a tool with the metadata and arguments you provide.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(id: String, metadata: [String : any ConvertibleToGeneratedContent], toolName: String, arguments: GeneratedContent)
```

## Parameters

- `id`: A unique identifier for the tool call.
- `metadata`: Additional information to associate with the tool call, keyed by name.
- `toolName`: The name of the tool to invoke.
- `arguments`: The arguments to pass to the invoked tool.

## See Also

- [init(id: String, toolName: String, arguments: GeneratedContent)](transcript/toolcall/init(id:toolname:arguments:).md)
  Creates a tool call that invokes a tool with the arguments you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/toolcall/init(id:metadata:toolname:arguments:))*