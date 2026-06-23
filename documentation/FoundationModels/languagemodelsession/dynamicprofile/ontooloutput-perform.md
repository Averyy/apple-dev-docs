# onToolOutput(perform:)

**Framework**: Foundation Models  
**Kind**: method

Runs an action whenever a tool call output is received within this dynamic profile.

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
func onToolOutput(perform action: nonisolated(nonsending) sending @escaping () async throws -> Void) -> some LanguageModelSession.DynamicProfile
```

## Mentions

- [Composing dynamic sessions with instructions and profiles](composing-dynamic-sessions-with-instructions-and-profiles.md)

#### Discussion

When the `onToolOutput` closure throws an error, the caller’s `respond` or `response` will propagate that error.

Use this to track or log tool output within a dynamic profile:

```swift
struct MyDynamicProfile: LanguageModelSession.DynamicProfile {
  var body: some LanguageModelSession.DynamicProfile {
    Profile {
      Instructions("You are a helpful assistant.")
      SomeTool()
    }
    .onToolOutput {
      toolOutputCount += 1
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofile/ontooloutput(perform:))*