# captureDevice

**Framework**: App Intents  
**Kind**: property

The device or camera for capturing a photo or video.

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
var captureDevice: some AssistantSchemas.Enum { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app enum implementation. The following example shows an app enum that conforms to the `.camera.captureDevice` schema:

```swift
@AppEnum(schema: .camera.captureDevice)
enum CaptureDevice: AppEnum {
    case front
    case back

    static var caseDisplayRepresentations: [CaptureDevice: AppIntents.DisplayRepresentation] = [
        .front: "Front",
        .back: "Back",
    ]
}
```

For more information about the `.camera` app intent domain, see [`Making camera actions available to Siri and Apple Intelligence`](making-camera-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

## See Also

- [var captureDuration: some AssistantSchemas.Enum](assistantschemas/cameraenum/captureduration.md)
  The capture duration for a photo or video.
- [var captureMode: some AssistantSchemas.Enum](assistantschemas/cameraenum/capturemode.md)
  The capture mode for taking a photo or video.
- [AssistantSchemas.CameraEnum](assistantschemas/cameraenum.md)
  Assistant schema conformance for types you use for camera functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/cameraenum/capturedevice)*