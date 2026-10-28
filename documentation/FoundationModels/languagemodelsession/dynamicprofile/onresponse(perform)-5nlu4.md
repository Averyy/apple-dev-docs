# onResponse(perform:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Instance Method

Runs an action after this dynamic profile produces a response.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func onResponse(perform action: nonisolated(nonsending) sending @escaping (Transcript.Response) async throws -> Void) -> some LanguageModelSession.DynamicProfile
```

**Other overloads**:

```swift
@export(implementation)
func onResponse(perform action: nonisolated(nonsending) sending @escaping () async throws -> Void) -> some LanguageModelSession.DynamicProfile
```

## Discussion

When the `onResponse` closure throws an error, the caller’s `respond` or `response` propagates that error.

Use this to perform cleanup or state updates when a dynamic profile completes:

```swift
struct MyDynamicProfile: LanguageModelSession.DynamicProfile {
  var body: some LanguageModelSession.DynamicProfile {
    Profile {
      Instructions("You are a helpful assistant.")
    }
    .onResponse { response in
      print("response: \(response)")
      completedTasks += 1
    }
  }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofile/onresponse(perform:)-5nlu4)*