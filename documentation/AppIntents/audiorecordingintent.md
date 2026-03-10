# AudioRecordingIntent

**Framework**: App Intents  
**Kind**: protocol

An app intent that starts, stops or otherwise modifies audio recording state.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
protocol AudioRecordingIntent : SystemIntent
```

#### Overview

Adopt this protocol to create an app intent for audio recording functionality and tell the system that your app records audio. As a result of this intent, the system displays an audio recording indicator.

> ❗ **Important**: In iOS, iPadOS, and watchOS, When you adopt the `AudioRecordingIntent` protocol, you must start a Live Activity when you begin the audio recording and keep it active as long as you record audio. If you don’t start a Live Activity, the audio recording stops.

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
- [protocol AudioStartingIntent](audiostartingintent.md)
  An App Intent that plays, pauses, or otherwise modifies audio playback state when it executes.
- [protocol CameraCaptureIntent](cameracaptureintent.md)
  Designates intent that will launch an activity that uses device’s camera to capture photos or videos. Marking your intent with this protocol makes it available as a possible action for Camera quick action.
- [protocol PlayVideoIntent](playvideointent.md)
  An intent that looks for videos based on a search term, then plays the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/audiorecordingintent)*