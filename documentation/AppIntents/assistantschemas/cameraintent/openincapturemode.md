# openInCaptureMode

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for opening the app’s camera functionality, ready to capture a photo or video.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var openInCaptureMode: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.camera.openInCaptureMode` schema:

```swift
@AppIntent(schema: .camera.openInCaptureMode)
struct NavigateToCaptureModeIntent: OpenIntent {
    @Parameter
    var target: CaptureMode

    func perform() async throws -> some IntentResult {
        .result()
    }
}
```

For more information about the `.camera` app intent domain, see doc:Making-camera-actions-available-to-siri-and-apple-intelligence. For general information about app intent domains, see doc:Integrating-actions-with-siri-and-apple-intelligence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/cameraintent/openincapturemode)*