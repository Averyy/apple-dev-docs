# AssistantSchemas.CameraIntent

**Framework**: App Intents  
**Kind**: protocol

Assistant schema conformance for app intents that offer camera functionality.

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
protocol CameraIntent : AssistantSchemas.Model
```

## Mentions

- [Making camera actions available to Siri and Apple Intelligence](making-camera-actions-available-to-siri-and-apple-intelligence.md)

## Topics

### Instance Properties
- [var openInCaptureMode: some AssistantSchemas.Intent](assistantschemas/cameraintent/openincapturemode.md)
  The app intent conforms to the schema for opening the app’s camera functionality, ready to capture a photo or video.
- [var setDevice: some AssistantSchemas.Intent](assistantschemas/cameraintent/setdevice.md)
  The app intent conforms to the schema for choosing a device to capture a photo.
- [var startCapture: some AssistantSchemas.Intent](assistantschemas/cameraintent/startcapture.md)
  The app intent conforms to the schema for starting the capture of a photo or video.
- [var stopCapture: some AssistantSchemas.Intent](assistantschemas/cameraintent/stopcapture.md)
  The app intent conforms to the schema for stopping the capture of a photo or video.
- [var switchDevice: some AssistantSchemas.Intent](assistantschemas/cameraintent/switchdevice.md)
  The app intent conforms to the schema for switching between cameras or devices.

## Relationships

### Inherits From
- [AssistantSchemas.Model](assistantschemas/model.md)
### Conforming Types
- [AssistantSchema.IntentSchema](assistantschema/intentschema.md)
- [AssistantSchemas.IntentSchema](assistantschemas/intentschema.md)

## See Also

- [Making camera actions available to Siri and Apple Intelligence](making-camera-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and enumerations to integrate your app’s camera functionality with Siri and Apple Intelligence.
- [AssistantSchemas.CameraEnum](assistantschemas/cameraenum.md)
  Assistant schema conformance for types you use for camera functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/cameraintent)*