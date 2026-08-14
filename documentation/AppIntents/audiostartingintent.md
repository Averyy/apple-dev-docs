# AudioStartingIntent

**Framework**: App Intents  
**Kind**: protocol

An App Intent that plays, pauses, or otherwise modifies audio playback state when it executes.

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
protocol AudioStartingIntent : SystemIntent
```

#### Overview

Adopt this protocol to indicate to the system that your App Intent plays audio. The system can then avoid dialogue or other experiences that might interrupt that audio.

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SystemIntent](systemintent.md)

## See Also

- [protocol ForegroundContinuableIntent](foregroundcontinuableintent.md)
  A protocol you use for app intents which begin their work with the app in the background but may request to continue in the foreground.
- [protocol LiveActivityStartingIntent](liveactivitystartingintent.md)
  An intent that starts, pauses, or otherwise modifies a Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/audiostartingintent)*