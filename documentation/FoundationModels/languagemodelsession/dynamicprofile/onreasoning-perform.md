# onReasoning(perform:)

**Framework**: Foundation Models  
**Kind**: method

Runs an action whenever this dynamic profile produces reasoning.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@export(implementation)
func onReasoning(perform action: nonisolated(nonsending) sending @escaping () async throws -> Void) -> some LanguageModelSession.DynamicProfile
```

#### Discussion

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

- [func onActivate(perform: sending () async -> Void) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/onactivate(perform:).md)
  Runs an action when this dynamic profile becomes active.
- [func onDeactivate(perform: sending () async -> Void) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/ondeactivate(perform:).md)
  Runs an action when this dynamic profile becomes inactive.
- [func onPrompt(perform:)](languagemodelsession/dynamicprofile/onprompt(perform:).md)
  Runs an action before the model is invoked for this dynamic profile.
- [func onResponse(perform:)](languagemodelsession/dynamicprofile/onresponse(perform:).md)
  Runs an action after this dynamic profile produces a response.
- [func onToolCall(perform:)](languagemodelsession/dynamicprofile/ontoolcall(perform:).md)
  Runs an action whenever a tool is called within this dynamic profile.
- [func onToolOutput(perform:)](languagemodelsession/dynamicprofile/ontooloutput(perform:).md)
  Runs an action whenever a tool call output is received within this dynamic profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofile/onreasoning(perform:))*