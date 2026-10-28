# ForegroundContinuableIntent

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

A protocol you use for app intents which begin their work with the app in the background but may request to continue in the foreground.

**Availability**:
- iOS 16.4+ - Deprecated in 26.0
- iPadOS 16.4+ - Deprecated in 26.0
- Mac Catalyst 16.4+ - Deprecated in 26.0
- macOS 13.3+ - Deprecated in 26.0
- tvOS 16.4+ - Deprecated in 26.0
- visionOS
- watchOS 9.4+ - Deprecated in 26.0

> **Deprecated**: Please include '.foreground(.dynamic)' in the 'supportedModes' of your app intent instead

## Declaration

```swift
protocol ForegroundContinuableIntent : AppIntent
```

## Overview

This protocol is deprecated, please include `.foreground(.dynamic)` in the [`supportedModes`](./appintent/supportedmodes.md) of your app intent instead. For backward compatibility, you can provide conformance to this protocol in an extension, for example:

```swift
@available(*, deprecated)
extension OrderSoupIntent: ForegroundContinuableIntent {}
```

## Topics

### Instance Methods
- [func needsToContinueInForegroundError(IntentDialog?, continuation: (() async throws -> Void)?) -> AppIntentError](./foregroundcontinuableintent/needstocontinueinforegrounderror%28_,continuation%29.md)
  A method you call to ask a person to continue an intent’s action in the foreground after it encounters an error.
- [func requestToContinueInForeground<ResultValue>(IntentDialog?, continuation: () async throws -> ResultValue) async throws -> ResultValue](./foregroundcontinuableintent/requesttocontinueinforeground%28_,continuation%29.md)
  A method you call to ask a person to continue an action in the foreground.

## Relationships

### Inherits From
- [AppIntent](./appintent.md)
- [PersistentlyIdentifiable](./persistentlyidentifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Deprecated types
- [protocol AudioStartingIntent](./audiostartingintent.md)
  An App Intent that plays, pauses, or otherwise modifies audio playback state when it executes.
- [protocol LiveActivityStartingIntent](./liveactivitystartingintent.md)
  An intent that starts, pauses, or otherwise modifies a Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/foregroundcontinuableintent)*