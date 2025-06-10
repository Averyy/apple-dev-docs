# IntentModes

**Framework**: App Intents  
**Kind**: struct

A set of options that describe an app intent’s behavior.

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
### Initializers
- [init(rawValue: Int)](intentmodes/init(rawvalue:).md)
  Creates a new option set from the given raw value.
### Instance Properties
- [let rawValue: Int](intentmodes/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [IntentModes.ArrayLiteralElement](intentmodes/arrayliteralelement.md)
  The type of the elements of an array literal.
- [IntentModes.Element](intentmodes/element.md)
  The element type of the option set.
- [IntentModes.RawValue](intentmodes/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static var background: IntentModes](intentmodes/background.md)
  The app intent can perform its action in the background.
- [static var foreground: IntentModes](intentmodes/foreground.md)
  The app intent requires the app to be in the foreground to perform its action.
### Type Methods
- [static func foreground(IntentModes.ForegroundMode) -> IntentModes](intentmodes/foreground(_:).md)
  Creates and returns a foreground mode with a specified behavior.
### Default Implementations
- [Equatable Implementations](intentmodes/equatable-implementations.md)
- [OptionSet Implementations](intentmodes/optionset-implementations.md)
- [RawRepresentable Implementations](intentmodes/rawrepresentable-implementations.md)
- [SetAlgebra Implementations](intentmodes/setalgebra-implementations.md)

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