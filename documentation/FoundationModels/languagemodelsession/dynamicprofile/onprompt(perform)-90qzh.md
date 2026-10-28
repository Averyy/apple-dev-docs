# onPrompt(perform:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Instance Method

Runs an action before the model is invoked for this dynamic profile.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func onPrompt(perform action: nonisolated(nonsending) sending @escaping (Transcript.Prompt) async throws -> Void) -> some LanguageModelSession.DynamicProfile
```

**Other overloads**:

```swift
@export(implementation)
func onPrompt(perform action: nonisolated(nonsending) sending @escaping () async throws -> Void) -> some LanguageModelSession.DynamicProfile
```

## Discussion

When the `onPrompt` closure throws an error, the caller’s `respond` or `response` propagates that error.

Use this to observe or log prompts before generation begins:

```swift
struct MyDynamicProfile: LanguageModelSession.DynamicProfile {
  var body: some LanguageModelSession.DynamicProfile {
    Profile {
      Instructions("You are a helpful assistant.")
    }
    .onPrompt { prompt in
      print("prompt: \(prompt)")
      promptCount += 1
    }
  }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofile/onprompt(perform:)-90qzh)*