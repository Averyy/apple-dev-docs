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
func onToolCall(perform action: nonisolated(nonsending) sending @escaping (Transcript.ToolCall) async throws -> Void) -> some LanguageModelSession.DynamicProfile
```

**Other overloads**:

```swift
@export(implementation)
func onToolCall(perform action: nonisolated(nonsending) sending @escaping () async throws -> Void) -> some LanguageModelSession.DynamicProfile
```

## Discussion

When the `onToolCall` closure throws an error, the caller’s `respond` or `response` propagates that error.

Use this to track or log tool usage within a dynamic profile:

```swift
struct MyDynamicProfile: LanguageModelSession.DynamicProfile {
  var body: some LanguageModelSession.DynamicProfile {
    Profile {
      Instructions("You are a helpful assistant.")
      SomeTool()
    }
    .onToolCall { call in
      print("called tool: \(call)")
      toolCallCount += 1
    }
  }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofile/ontoolcall(perform:)-70tox)*