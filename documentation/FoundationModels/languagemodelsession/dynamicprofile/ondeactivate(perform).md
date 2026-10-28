# onDeactivate(perform:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Instance Method

Runs an action when this dynamic profile becomes inactive.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func onDeactivate(perform action: sending @escaping @isolated(any) () async -> Void) -> some LanguageModelSession.DynamicProfile
```

## Mentions

- [Composing dynamic sessions with instructions and profiles](../../composing-dynamic-sessions-with-instructions-and-profiles.md)

## Discussion

A profile becomes inactive when it is no longer included in the session’s resolved configuration after previously being active. Use this to tear down state tied to the profile’s lifecycle:

```swift
struct MyDynamicProfile: LanguageModelSession.DynamicProfile {
  var body: some LanguageModelSession.DynamicProfile {
    Profile {
      Instructions("You are a helpful assistant.")
    }
    .onDeactivate {
      activeProfile = nil
    }
  }
}
```

## See Also

### Observing life cycle modifiers
- [func onActivate(perform: sending () async -> Void) -> some LanguageModelSession.DynamicProfile](./onactivate%28perform%29.md)
  Runs an action when this dynamic profile becomes active.
- [func onPrompt(perform:)](./onprompt%28perform%29.md)
  Runs an action before the model is invoked for this dynamic profile.
- [func onReasoning(perform:)](./onreasoning%28perform%29.md)
  Runs an action whenever this dynamic profile produces reasoning.
- [func onResponse(perform:)](./onresponse%28perform%29.md)
  Runs an action after this dynamic profile produces a response.
- [func onToolCall(perform:)](./ontoolcall%28perform%29.md)
  Runs an action whenever a tool is called within this dynamic profile.
- [func onToolOutput(perform:)](./ontooloutput%28perform%29.md)
  Runs an action whenever a tool call output is received within this dynamic profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofile/ondeactivate(perform:))*