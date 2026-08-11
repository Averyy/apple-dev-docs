# onActivate(perform:)

**Framework**: Foundation Models  
**Kind**: method

Runs an action when this dynamic profile becomes active.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func onActivate(perform action: sending @escaping @isolated(any) () async -> Void) -> some LanguageModelSession.DynamicProfile
```

## Mentions

- [Composing dynamic sessions with instructions and profiles](composing-dynamic-sessions-with-instructions-and-profiles.md)

#### Discussion

A profile becomes active when it is first included in the session’s resolved configuration, or when it is re-included after being absent. Use this to set up state tied to the profile’s lifecycle:

```swift
struct MyDynamicProfile: LanguageModelSession.DynamicProfile {
  var body: some LanguageModelSession.DynamicProfile {
    Profile {
      Instructions("You are a helpful assistant.")
    }
    .onActivate {
      activeProfile = "assistant"
    }
  }
}
```

## See Also

- [func onDeactivate(perform: sending () async -> Void) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/ondeactivate(perform:).md)
  Runs an action when this dynamic profile becomes inactive.
- [func onPrompt(perform:)](languagemodelsession/dynamicprofile/onprompt(perform:).md)
  Runs an action before the model is invoked for this dynamic profile.
- [func onReasoning(perform:)](languagemodelsession/dynamicprofile/onreasoning(perform:).md)
  Runs an action whenever this dynamic profile produces reasoning.
- [func onResponse(perform:)](languagemodelsession/dynamicprofile/onresponse(perform:).md)
  Runs an action after this dynamic profile produces a response.
- [func onToolCall(perform:)](languagemodelsession/dynamicprofile/ontoolcall(perform:).md)
  Runs an action whenever a tool is called within this dynamic profile.
- [func onToolOutput(perform:)](languagemodelsession/dynamicprofile/ontooloutput(perform:).md)
  Runs an action whenever a tool call output is received within this dynamic profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofile/onactivate(perform:))*