# IntentModes

**Framework**: App Intents  
**Kind**: struct

A set of options that describe an app intent’s behavior.

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
struct IntentModes
```

#### Overview

The`IntentModes` structure provides values that describe an app intent’s behavior. For example, intent modes describe whether an app intent can run in the background, foreground, or both.  If an app intent supports a [`IntentModes.ForegroundMode`](intentmodes/foregroundmode.md), it can specify additional behaviors.

## Topics

### Structures
- [IntentModes.Current](intentmodes/current.md)
  The current behavior for performing an app intent.
- [IntentModes.ForegroundMode](intentmodes/foregroundmode.md)
  A type defining specific foreground behaviors for an app intent.
### Type Properties
- [static var background: IntentModes](intentmodes/background.md)
  The app intent can perform its action in the background.
- [static var foreground: IntentModes](intentmodes/foreground.md)
  The app intent requires the app to be in the foreground to perform its action.
### Type Methods
- [static func foreground(IntentModes.ForegroundMode) -> IntentModes](intentmodes/foreground(_:).md)
  Creates and returns a foreground mode with a specified behavior.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentmodes)*