# openInCaptureMode

**Framework**: App Intents  
**Kind**: property

An intent schema that opens the camera in the specified mode.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var openInCaptureMode: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `camera` domain and one of your app’s actions matches the `openInCaptureMode` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .camera.openInCaptureMode)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `openInCaptureMode` schema:

```swift
@AppIntent(schema: .camera.openInCaptureMode)
struct NavigateToCaptureModeIntent: OpenIntent {
    var target: <#CaptureMode#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var setDevice: some AppSchemaIntent](appschema/cameraintent/setdevice.md)
  An intent schema that changes the camera to the specified position.
- [var startCapture: some AppSchemaIntent](appschema/cameraintent/startcapture.md)
  An intent schema that starts a capture or opens the camera in a specified mode with a timer setting.
- [var stopCapture: some AppSchemaIntent](appschema/cameraintent/stopcapture.md)
  An intent schema that stops a recording in progress.
- [var switchDevice: some AppSchemaIntent](appschema/cameraintent/switchdevice.md)
  An intent schema that toggles between front and back camera.
- [AppSchema.CameraIntent](appschema/cameraintent.md)
  Identifies intent schemas in the camera domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/cameraintent/openincapturemode)*