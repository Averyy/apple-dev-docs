# onToolOutput(perform:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Instance Method

Runs an action whenever a tool call output is received within this dynamic profile.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func onToolOutput(perform action: nonisolated(nonsending) sending @escaping (Transcript.ToolCall, Transcript.ToolOutput) async throws -> Void) -> some LanguageModelSession.DynamicProfile
```

**Other overloads**:

```swift
@export(implementation)
func onToolOutput(perform action: nonisolated(nonsending) sending @escaping () async throws -> Void) -> some LanguageModelSession.DynamicProfile
```

## Discussion

When the `onToolOutput` closure throws an error, the caller’s `respond` or `response` propagates that error.

Use this to track or log tool output within a dynamic profile:

```swift
struct MyDynamicProfile: LanguageModelSession.DynamicProfile {
  var body: some LanguageModelSession.DynamicProfile {
    Profile {
      Instructions("You are a helpful assistant.")
      SomeTool()
    }
    .onToolOutput { call, output in
      print("Tool \(call) produced: \(output)")
    }
  }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofile/ontooloutput(perform:)-3vs5a)*