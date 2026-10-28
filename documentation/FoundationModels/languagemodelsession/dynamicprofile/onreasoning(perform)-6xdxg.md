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
func onReasoning(perform action: nonisolated(nonsending) sending @escaping (Transcript.Reasoning) async throws -> Void) -> some LanguageModelSession.DynamicProfile
```

**Other overloads**:

```swift
@export(implementation)
func onReasoning(perform action: nonisolated(nonsending) sending @escaping () async throws -> Void) -> some LanguageModelSession.DynamicProfile
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
    .onReasoning { reasoning in
      print("reasoning: \(reasoning)")
      reasoningCount += 1
    }
  }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofile/onreasoning(perform:)-6xdxg)*