# IntentModes.ForegroundMode

**Framework**: App Intents  
**Kind**: struct

A type that defines the available foreground behaviors for an app intent.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct ForegroundMode
```

#### Overview

Use this type to specify the foreground behaviors you want to apply to your app intent. Each option specifies when and how the system brings your app to the foreground to perform the app intent’s action.

## Topics

### Type Properties
- [static var deferred: IntentModes.ForegroundMode](intentmodes/foregroundmode/deferred.md)
  An option to bring the app to the foreground while running the intent’s action or shortly before the action completes.
- [static var dynamic: IntentModes.ForegroundMode](intentmodes/foregroundmode/dynamic.md)
  An option to bring the app to the foreground if conditions permit it.
- [static var immediate: IntentModes.ForegroundMode](intentmodes/foregroundmode/immediate.md)
  An option to bring the app to the foreground immediately after the system resolves the intent’s parameters.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentmodes/foregroundmode)*