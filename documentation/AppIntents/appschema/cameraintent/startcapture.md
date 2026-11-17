# startCapture

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that starts a capture or opens the camera in a specified mode with a timer setting.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var startCapture: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `camera` domain and one of your app’s actions matches the `startCapture` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .camera.startCapture)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `startCapture` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `camera_startCapture` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .camera.startCapture)
struct StartCameraCaptureIntent {
    /// Mode to capture in.
    var captureMode: <#CaptureMode#>

    /// Device position to capture with.
    var device: <#CaptureDevice#>?

    /// Duration to wait before starting the capture.
    var timerDuration: <#CaptureDuration#>?

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the start-capture intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `captureMode` | `@AppEnum(schema: .camera.captureMode)` | Your app | Mode to capture in. `CaptureMode` is a placeholder name for a type that conforms to the [`captureMode`](../cameraenum/capturemode.md) enum schema, which your app defines and implements. |
| `device` | `@AppEnum(schema: .camera.captureDevice)?` | Your app | Device position to capture with. `CaptureDevice` is a placeholder name for a type that conforms to the [`captureDevice`](../cameraenum/capturedevice.md) enum schema, which your app defines and implements. |
| `timerDuration` | `@AppEnum(schema: .camera.captureDuration)?` | Your app | Duration to wait before starting the capture. `CaptureDuration` is a placeholder name for a type that conforms to the [`captureDuration`](../cameraenum/captureduration.md) enum schema, which your app defines and implements. |

## See Also

### Actions
- [var openInCaptureMode: some AppSchemaIntent](./openincapturemode.md)
  An intent schema that opens the camera in the specified mode.
- [var setDevice: some AppSchemaIntent](./setdevice.md)
  An intent schema that changes the camera to the specified position.
- [var stopCapture: some AppSchemaIntent](./stopcapture.md)
  An intent schema that stops a recording in progress.
- [var switchDevice: some AppSchemaIntent](./switchdevice.md)
  An intent schema that toggles between front and back camera.
- [AppSchema.CameraIntent](../cameraintent.md)
  Identifies intent schemas in the camera domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/cameraintent/startcapture)*