# onReasoning(perform:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Instance Method

Runs an action whenever this dynamic profile produces reasoning.

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
func onReasoning(perform action: nonisolated(nonsending) sending @escaping () async throws -> Void) -> some LanguageModelSession.DynamicProfile
```

**Other overloads**:

```swift
func onReasoning(perform action: nonisolated(nonsending) sending @escaping (Transcript.Reasoning) async throws -> Void) -> some LanguageModelSession.DynamicProfile
```

## Discussion

Reasoning is only produced by models that declare the `.reasoning` capability.

When the `onReasoning` closure throws an error, the caller’s `respond` or `response` propagates that error.

Use this to observe or log the model’s reasoning as it works toward a response:

```swift
struct MyDynamicProfile: LanguageModelSession.DynamicProfile {
  var body: some LanguageModelSession.DynamicProfile {
    Profile {
      Instructions("You are a helpful assistant.")
    }
    .onReasoning {
      reasoningCount += 1
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
- [func onResponse(perform:)](./onresponse%28perform%29.md)
  Runs an action after this dynamic profile produces a response.
- [func onToolCall(perform:)](./ontoolcall%28perform%29.md)
  Runs an action whenever a tool is called within this dynamic profile.
- [func onToolOutput(perform:)](./ontooloutput%28perform%29.md)
  Runs an action whenever a tool call output is received within this dynamic profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofile/onreasoning(perform:))*