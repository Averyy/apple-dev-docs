# currentMode

**Framework**: App Intents  
**Kind**: property

A value that indicates the foreground and background behavior for app intent’s action.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var currentMode: IntentModes.Current { get }
```

#### Discussion

This value indicates whether the intent is running in the background or foreground, and, if it requires the app to be in the foreground, the specific `ForegroundModes`. Use this property when handling app intents that support multiple modes — for example, `IntentModes.background` and `IntentModes.foreground` — to enable conditional behavior based on the current run mode. The following example shows how you can check the intent mode before performing its action:

```swift
func perform() async throws -> some IntentResult {
    if systemContext.currentMode.canContinueInForeground {
        // Perform actions if it's OK for the app intent to request
        // to appear in the foreground if necessary.
        try await continueInForeground()
    }
    return .result()
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentsystemcontext/currentmode)*