# AssistantSchemas.CameraEnum

**Framework**: App Intents  
**Kind**: protocol

Assistant schema conformance for types you use for camera functionality.

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
protocol CameraEnum : AssistantSchemas.Model
```

## Mentions

- [Making camera actions available to Siri and Apple Intelligence](making-camera-actions-available-to-siri-and-apple-intelligence.md)

## Topics

### Instance Properties
- [var captureDevice: some AssistantSchemas.Enum](assistantschemas/cameraenum/capturedevice.md)
  The device or camera for capturing a photo or video.
- [var captureDuration: some AssistantSchemas.Enum](assistantschemas/cameraenum/captureduration.md)
  The capture duration for a photo or video.
- [var captureMode: some AssistantSchemas.Enum](assistantschemas/cameraenum/capturemode.md)
  The capture mode for taking a photo or video.

## Relationships

### Inherits From
- [AssistantSchemas.Model](assistantschemas/model.md)
### Conforming Types
- [AssistantSchema.EnumSchema](assistantschema/enumschema.md)
- [AssistantSchemas.EnumSchema](assistantschemas/enumschema.md)

## See Also

- [Making camera actions available to Siri and Apple Intelligence](making-camera-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and enumerations to integrate your app’s camera functionality with Siri and Apple Intelligence.
- [AssistantSchemas.CameraIntent](assistantschemas/cameraintent.md)
  Assistant schema conformance for app intents that offer camera functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/cameraenum)*