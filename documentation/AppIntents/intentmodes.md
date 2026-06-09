# IntentModes

**Framework**: App Intents  
**Kind**: struct

A set of options you use to configure the runtime behavior of an app intent.

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

This structure defines the mode values you can assign to the [`supportedModes`](appintent/supportedmodes.md) property of your app intent. Intent modes indicate whether your app needs to run in the foreground or background when performing the app intent’s action. For example, the [`foreground`](intentmodes/foreground.md) mode requires your app intent code to run in a foreground process.

At runtime, an app intent’s [`systemContext`](appintent/systemcontext.md) property also contains information about whether the process is currently running in the foreground or background. Use that information to make additional decisions about how to perform the action. For more information, see the [`IntentModes.Current`](intentmodes/current.md) type.

## Topics

### Structures
- [IntentModes.Current](intentmodes/current.md)
  The current runtime behavior of an app intent.
- [IntentModes.ForegroundMode](intentmodes/foregroundmode.md)
  A type that defines the available foreground behaviors for an app intent.
### Type Properties
- [static var background: IntentModes](intentmodes/background.md)
  A value that indicates the action can run in the background.
- [static var foreground: IntentModes](intentmodes/foreground.md)
  A value that indicates the action needs to run in the foreground.
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

## See Also

- [struct IntentSystemContext](intentsystemcontext.md)
  Contextual information that the system provides while it performs an app intent.
- [struct IntentDescription](intentdescription.md)
  The human-readable description and metadata for an app intent.
- [struct IntentDialog](intentdialog.md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [struct IntentDeprecation](intentdeprecation.md)
- [class IntentProjection](intentprojection.md)
  Projections for an app intent that returns non-optional values for parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentmodes)*