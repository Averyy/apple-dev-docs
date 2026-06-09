# currentMode

**Framework**: App Intents  
**Kind**: property

A value that indicates the foreground and background behavior for app intent’s action.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var currentMode: IntentModes.Current { get }
```

#### Discussion

This value indicates whether the intent is running in the background or foreground, and the current [`IntentModes.ForegroundMode`](intentmodes/foregroundmode.md) option if it requires the app to be in the foreground. When handling an app intent that supports both foreground and background modes, use this property to check the current run mode before making any adjustments, as shown in the following example from an app intent type:

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