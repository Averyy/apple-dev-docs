# IntentModes.Current

**Framework**: App Intents  
**Kind**: struct

The current behavior for performing an app intent.

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
struct Current
```

#### Overview

This type provides additional detail about the current behavior for running the intent’s action, such as whether the app intent can require to continue the action in the foreground.

## Topics

### Instance Properties
- [var canContinueInForeground: Bool](intentmodes/current/cancontinueinforeground.md)
  A flag that indicates whether the app intent can continue its action while the app is in the foreground.
### Type Properties
- [static var background: IntentModes.Current](intentmodes/current/background.md)
  The background execution mode.
- [static var foreground: IntentModes.Current](intentmodes/current/foreground.md)
  The foreground execution mode.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentmodes/current)*