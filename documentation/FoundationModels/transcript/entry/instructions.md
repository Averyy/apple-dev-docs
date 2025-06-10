# Transcript.Entry.instructions(_:)

**Framework**: Foundation Models  
**Kind**: case

Instructions, typically provided by you, the developer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
case instructions(Transcript.Instructions)
```

## See Also

- [init(from: any Decoder) throws](transcript/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [case prompt(Transcript.Prompt)](transcript/entry/prompt(_:).md)
  A prompt, typically sourced from an end user.
- [case response(Transcript.Response)](transcript/entry/response(_:).md)
  A response from the model.
- [case toolCalls(Transcript.ToolCalls)](transcript/entry/toolcalls(_:).md)
  A tool call containing a tool name and the arguments to invoke it with.
- [case toolOutput(Transcript.ToolOutput)](transcript/entry/tooloutput(_:).md)
  An tool output provided back to the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/entry/instructions(_:))*