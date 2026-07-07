# LiveActivityStartingIntent

**Framework**: App Intents  
**Kind**: protocol

An intent that starts, pauses, or otherwise modifies a Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- visionOS ?+

## Declaration

```swift
protocol LiveActivityStartingIntent : SystemIntent
```

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SystemIntent](systemintent.md)

## See Also

- [protocol AudioStartingIntent](audiostartingintent.md)
  An App Intent that plays, pauses, or otherwise modifies audio playback state when it executes.
- [protocol ForegroundContinuableIntent](foregroundcontinuableintent.md)
  A protocol you use for app intents which begin their work with the app in the background but may request to continue in the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/liveactivitystartingintent)*