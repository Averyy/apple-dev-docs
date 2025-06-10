# onAppIntentExecution(_:perform:)

**Framework**: App Intents  
**Kind**: method

Registers a handler to invoke in response to the specified app intent that your app receives.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 16.0+
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func onAppIntentExecution<I>(_ intent: I.Type = I.self, perform action: @escaping @MainActor (I) -> Void) -> some View where I : TargetContentProvidingIntent
```

#### Return Value

A view that handles the specified app intent’s perform

#### Discussion

Use this view modifier to receive instances in a particular scene within your app. The scene that SwiftUI routes the incoming user activity to depends on the structure of your app, what scenes are active, and other configuration. For more information, see `Scene/handlesExternalEvents(matching:)`.

If the app intent implements a perform() method, it will be called after the action closure.  This can be useful if your app intent supports running in the background via the AppIntent.IntentModes API

> **Note**: Usage of the app intent instance provided to the action closure is limited to inspecting parameter values, interactive requests like [`requestValue(_:)`](IntentParameter/requestValue(_:)-592nd.md) or <doc://com.apple.documentation/documentation/appintents/intentparameter/needsvalueerror(_:) will not work.

## Parameters

- `intent`: The type of App Intent that the   closure handles.
- `action`: A closure that SwiftUI calls when the specified app intent is being performed.   The closure takes the app intent instance as an input parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/onappintentexecution(_:perform:))*