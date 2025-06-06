# Making camera actions available to Siri and Apple Intelligence

**Framework**: Appintents

Create app intents and enumerations to integrate your app’s camera functionality with Siri and Apple Intelligence.

#### Overview

To integrate your app’s camera capabilities with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app intent and app enumeration implementation that Apple Intelligence needs.

> **Note**: Siri’s personal context understanding, onscreen awareness, and in-app actions are in development and will be available with a future software update.

For example, if your app allows a person to take a photo or video, use the [`AssistantIntent(schema:)`](assistantintent(schema:).md) macro and provide the assistant schema that consists of the `.camera` domain and the [`startCapture`](assistantschemas/cameraintent/startcapture.md) schema:

```swift
@AssistantIntent(schema: .camera.startCapture)
struct StartCaptureIntent {
    var captureMode: CaptureMode
    var timerDuration: CaptureDuration?
    var device: CaptureDevice?

    func perform() async throws -> some IntentResult {
        .result()
    }
}
```

To learn more about assistant schemas, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md). For a list of available app intents in the `.camera` domain, see [`AssistantSchemas.CameraIntent`](assistantschemas/cameraintent.md).

##### Make Sure Your Enumeration Meets Requirements

To make sure Siri and Apple Intelligence understand custom static types for your intent parameters, annotate app enumerations with the [`AssistantEnum(schema:)`](assistantenum(schema:).md) macro. Then, pass the `.camera` domain and a schema to it. The following example uses the [`captureMode`](assistantschemas/cameraenum/capturemode.md) schema:

```swift
@AssistantEnum(schema: .camera.captureMode)
struct CameraCaptureMode: String, AppEnum {
    // Your app's camera capture modes.
    case portrait
    case landscape
    case catFace
    case awesomeFilter

    static var caseDisplayRepresentations: [ClearHistoryTimeFrame: DisplayRepresentation] = [:]

}
```

For a list of available app enumeration schemas in the `.camera` domain, see [`AssistantSchemas.CameraEnum`](assistantschemas/cameraenum.md).

## See Also

- [AssistantSchemas.CameraIntent](assistantschemas/cameraintent.md)
  Assistant schema conformance for app intents that offer camera functionality.
- [AssistantSchemas.CameraEnum](assistantschemas/cameraenum.md)
  Assistant schema conformance for types you use for camera functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppIntents/making-camera-actions-available-to-siri-and-apple-intelligence)*