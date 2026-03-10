# AudioStartingIntent

**Framework**: App Intents  
**Kind**: protocol

An App Intent that plays, pauses, or otherwise modifies audio playback state when it executes.

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
protocol AudioStartingIntent : SystemIntent
```

#### Overview

Adopt this protocol to indicate to the system that your App Intent plays audio. The system can then avoid dialogue or other experiences that might interrupt that audio.

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SystemIntent](systemintent.md)

## See Also

- [protocol AudioPlaybackIntent](audioplaybackintent.md)
  An App Intent that plays, pauses, or otherwise modifies audio playback state when it executes.
- [protocol AudioRecordingIntent](audiorecordingintent.md)
  An app intent that starts, stops or otherwise modifies audio recording state.
- [protocol CameraCaptureIntent](cameracaptureintent.md)
  Designates intent that will launch an activity that uses device’s camera to capture photos or videos. Marking your intent with this protocol makes it available as a possible action for Camera quick action.
- [protocol PlayVideoIntent](playvideointent.md)
  An intent that looks for videos based on a search term, then plays the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/audiostartingintent)*