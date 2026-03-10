# PlayVideoIntent

**Framework**: App Intents  
**Kind**: protocol

An intent that looks for videos based on a search term, then plays the content.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst ?+
- macOS 14.2+
- tvOS 17.2+
- visionOS ?+

## Declaration

```swift
protocol PlayVideoIntent : SystemIntent
```

## Topics

### Instance Properties
- [var term: String](playvideointent/term.md)
  The search term requested by the user.
### Type Properties
- [static var supportedCategories: [VideoCategory]](playvideointent/supportedcategories.md)
  The list of video categories that the app supports through this intent.

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
- [protocol AudioStartingIntent](audiostartingintent.md)
  An App Intent that plays, pauses, or otherwise modifies audio playback state when it executes.
- [protocol CameraCaptureIntent](cameracaptureintent.md)
  Designates intent that will launch an activity that uses device’s camera to capture photos or videos. Marking your intent with this protocol makes it available as a possible action for Camera quick action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/playvideointent)*