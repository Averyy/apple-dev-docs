# ForegroundContinuableIntent

**Framework**: App Intents  
**Kind**: protocol

A protocol you use for app intents which begin their work with the app in the background but may request to continue in the foreground.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS ?+
- watchOS 9.4+

## Declaration

```swift
protocol ForegroundContinuableIntent : AppIntent
```

#### Overview

This protocol is deprecated, please include `.foreground(.dynamic)` in the `supportedModes` of your app intent instead. For backward compatibility, you can provide conformance to this protocol in an extension, for example:

```swift
@available(*, deprecated)
extension OrderSoupIntent: ForegroundContinuableIntent {}
```

## Topics

### Instance Methods
- [func needsToContinueInForegroundError(IntentDialog?, continuation: (() async throws -> Void)?) -> AppIntentError](foregroundcontinuableintent/needstocontinueinforegrounderror(_:continuation:).md)
  A method you call to ask a person to continue an intent’s action in the foreground after it encounters an error.
- [func requestToContinueInForeground<ResultValue>(IntentDialog?, continuation: () async throws -> ResultValue) async throws -> ResultValue](foregroundcontinuableintent/requesttocontinueinforeground(_:continuation:).md)
  A method you call to ask a person to continue an action in the foreground.

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol AudioStartingIntent](audiostartingintent.md)
  An App Intent that plays, pauses, or otherwise modifies audio playback state when it executes.
- [protocol LiveActivityStartingIntent](liveactivitystartingintent.md)
  An intent that starts, pauses, or otherwise modifies a Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/foregroundcontinuableintent)*