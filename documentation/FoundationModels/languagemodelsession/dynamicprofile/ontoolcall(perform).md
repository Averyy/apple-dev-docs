# onToolCall(perform:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Instance Method

Runs an action whenever a tool is called within this dynamic profile.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@export(implementation)
func onToolCall(perform action: nonisolated(nonsending) sending @escaping () async throws -> Void) -> some LanguageModelSession.DynamicProfile
```

**Other overloads**:

```swift
func onToolCall(perform action: nonisolated(nonsending) sending @escaping (Transcript.ToolCall) async throws -> Void) -> some LanguageModelSession.DynamicProfile
```

## Mentions

- [Composing dynamic sessions with instructions and profiles](../../composing-dynamic-sessions-with-instructions-and-profiles.md)

#### Discussion

When the `onToolCall` closure throws an error, the caller’s `respond` or `response` propagates that error.

Use this to track or log tool usage within a dynamic profile:

```swift
struct MyDynamicProfile: LanguageModelSession.DynamicProfile {
  var body: some LanguageModelSession.DynamicProfile {
    Profile {
      Instructions("You are a helpful assistant.")
      SomeTool()
    }
    .onToolCall {
      toolCallCount += 1
    }
  }
}
```

## See Also

### Observing life cycle modifiers
- [func onActivate(perform: sending () async -> Void) -> some LanguageModelSession.DynamicProfile](./onactivate%28perform%29.md)
  Runs an action when this dynamic profile becomes active.
- [func onDeactivate(perform: sending () async -> Void) -> some LanguageModelSession.DynamicProfile](./ondeactivate%28perform%29.md)
  Runs an action when this dynamic profile becomes inactive.
- [func onPrompt(perform:)](./onprompt%28perform%29.md)
  Runs an action before the model is invoked for this dynamic profile.
- [func onReasoning(perform:)](./onreasoning%28perform%29.md)
  Runs an action whenever this dynamic profile produces reasoning.
- [func onResponse(perform:)](./onresponse%28perform%29.md)
  Runs an action after this dynamic profile produces a response.
- [func onToolOutput(perform:)](./ontooloutput%28perform%29.md)
  Runs an action whenever a tool call output is received within this dynamic profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofile/ontoolcall(perform:))*