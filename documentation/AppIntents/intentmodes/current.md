# IntentModes.Current

**Framework**: App Intents  
**Kind**: struct

The current behavior for performing an app intent.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct Current
```

#### Overview

This type provides additional detail about the current behavior for running the intent’s action, such as whether the app intent can require to continue the action in the foreground.

## Topics

### Operators
- [static func == (IntentModes.Current, IntentModes.Current) -> Bool](intentmodes/current/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var canContinueInForeground: Bool](intentmodes/current/cancontinueinforeground.md)
  A flag that indicates whether the app intent can continue its action while the app is in the foreground.
- [var debugDescription: String](intentmodes/current/debugdescription.md)
  A textual representation of this instance, suitable for debugging.
- [var hashValue: Int](intentmodes/current/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](intentmodes/current/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static var background: IntentModes.Current](intentmodes/current/background.md)
  The background execution mode.
- [static var foreground: IntentModes.Current](intentmodes/current/foreground.md)
  The foreground execution mode.
### Default Implementations
- [Equatable Implementations](intentmodes/current/equatable-implementations.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentmodes/current)*