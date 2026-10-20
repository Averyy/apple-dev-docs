# AppSchema.CameraIntent

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Identifies intent schemas in the camera domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
protocol CameraIntent : AppSchema.Kind
```

## Topics

### Instance Properties
- [var openInCaptureMode: some AppSchemaIntent](./cameraintent/openincapturemode.md)
  An intent schema that opens the camera in the specified mode.
- [var setDevice: some AppSchemaIntent](./cameraintent/setdevice.md)
  An intent schema that changes the camera to the specified position.
- [var startCapture: some AppSchemaIntent](./cameraintent/startcapture.md)
  An intent schema that starts a capture or opens the camera in a specified mode with a timer setting.
- [var stopCapture: some AppSchemaIntent](./cameraintent/stopcapture.md)
  An intent schema that stops a recording in progress.
- [var switchDevice: some AppSchemaIntent](./cameraintent/switchdevice.md)
  An intent schema that toggles between front and back camera.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Intent](./intent.md)

## See Also

### Actions
- [var openInCaptureMode: some AppSchemaIntent](./cameraintent/openincapturemode.md)
  An intent schema that opens the camera in the specified mode.
- [var setDevice: some AppSchemaIntent](./cameraintent/setdevice.md)
  An intent schema that changes the camera to the specified position.
- [var startCapture: some AppSchemaIntent](./cameraintent/startcapture.md)
  An intent schema that starts a capture or opens the camera in a specified mode with a timer setting.
- [var stopCapture: some AppSchemaIntent](./cameraintent/stopcapture.md)
  An intent schema that stops a recording in progress.
- [var switchDevice: some AppSchemaIntent](./cameraintent/switchdevice.md)
  An intent schema that toggles between front and back camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/cameraintent)*