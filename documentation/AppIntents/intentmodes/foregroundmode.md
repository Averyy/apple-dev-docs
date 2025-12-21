# IntentModes.ForegroundMode

**Framework**: App Intents  
**Kind**: struct

A type defining specific foreground behaviors for an app intent.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct ForegroundMode
```

#### Overview

The set of options you use to specify when and how the system should bring your app to the foreground when it performs its action.

## Topics

### Type Properties
- [static var deferred: IntentModes.ForegroundMode](intentmodes/foregroundmode/deferred.md)
  The system brings the app to the foreground while it performs the intent’s action or just before returning from its perform function.
- [static var dynamic: IntentModes.ForegroundMode](intentmodes/foregroundmode/dynamic.md)
  The system can bring the app to the foreground dynamically while it performs the intent’s action, depending on runtime conditions.
- [static var immediate: IntentModes.ForegroundMode](intentmodes/foregroundmode/immediate.md)
  The system brings the app into the foreground immediately after it resolves the intent’s parameters.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentmodes/foregroundmode)*