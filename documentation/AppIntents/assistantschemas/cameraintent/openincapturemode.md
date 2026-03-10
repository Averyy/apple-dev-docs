# openInCaptureMode

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for opening the app’s camera functionality, ready to capture a photo or video.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
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

For more information about the `.camera` app intent domain, see [`Making camera actions available to Siri and Apple Intelligence`](making-camera-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

## See Also

- [var setDevice: some AssistantSchemas.Intent](assistantschemas/cameraintent/setdevice.md)
  The app intent conforms to the schema for choosing a device to capture a photo.
- [var startCapture: some AssistantSchemas.Intent](assistantschemas/cameraintent/startcapture.md)
  The app intent conforms to the schema for starting the capture of a photo or video.
- [var stopCapture: some AssistantSchemas.Intent](assistantschemas/cameraintent/stopcapture.md)
  The app intent conforms to the schema for stopping the capture of a photo or video.
- [var switchDevice: some AssistantSchemas.Intent](assistantschemas/cameraintent/switchdevice.md)
  The app intent conforms to the schema for switching between cameras or devices.
- [AssistantSchemas.CameraIntent](assistantschemas/cameraintent.md)
  Assistant schema conformance for app intents that offer camera functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/cameraintent/openincapturemode)*