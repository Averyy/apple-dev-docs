# AssistantSchemas.CameraEnum

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

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

## Topics

### Instance Properties
- [var captureDevice: some AssistantSchemas.Enum](./cameraenum/capturedevice.md)
  The device or camera for capturing a photo or video.
- [var captureDuration: some AssistantSchemas.Enum](./cameraenum/captureduration.md)
  The capture duration for a photo or video.
- [var captureMode: some AssistantSchemas.Enum](./cameraenum/capturemode.md)
  The capture mode for taking a photo or video.

## Relationships

### Inherits From
- [AssistantSchemas.Model](./model.md)
### Conforming Types
- [AssistantSchema.EnumSchema](../assistantschema/enumschema.md)
- [AssistantSchemas.EnumSchema](./enumschema.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/cameraenum)*