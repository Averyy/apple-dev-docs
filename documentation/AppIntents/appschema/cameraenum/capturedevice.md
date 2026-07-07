# captureDevice

**Framework**: App Intents  
**Kind**: property

An enum schema for a capture device parameter.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var captureDevice: some AppSchemaEnum { get }
```

#### Discussion

To make your app’s parameter types available to Apple Intelligence, conform your [`AppEnum`](appenum.md) to a schema that describes a parameter’s possible values to the system. If your app’s functionality aligns with the `camera` domain and a parameter type matches the `captureDevice` schema, you can generate the protocol conformance the schema requires for your app enum implementation with the `@AppEnum( .camera.captureDevice)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app enum that conforms to the `captureDevice` schema:

```swift
@AppEnum(schema: .camera.captureDevice)
enum CaptureDevice: String {
    case <#CaptureDevice Case#>

    static let caseDisplayRepresentations: [Self: DisplayRepresentation] = [
        <#DisplayRepresentations#>
    ]
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var captureDuration: some AppSchemaEnum](appschema/cameraenum/captureduration.md)
  An enum schema for a capture duration parameter.
- [var captureMode: some AppSchemaEnum](appschema/cameraenum/capturemode.md)
  An enum schema for a capture mode parameter.
- [AppSchema.CameraEnum](appschema/cameraenum.md)
  Identifies enum schemas in the camera domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/cameraenum/capturedevice)*