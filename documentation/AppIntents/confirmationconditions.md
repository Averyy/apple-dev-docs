# ConfirmationConditions

**Framework**: App Intents  
**Kind**: struct

Conditions for a confirmation request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct ConfirmationConditions
```

#### Overview

If any of the conditions are met, confirmation will be requested.

## Topics

### Initializers
- [init(rawValue: Int)](confirmationconditions/init(rawvalue:).md)
  Creates a new option set from the given raw value.
### Instance Properties
- [let rawValue: Int](confirmationconditions/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [ConfirmationConditions.ArrayLiteralElement](confirmationconditions/arrayliteralelement.md)
  The type of the elements of an array literal.
- [ConfirmationConditions.Element](confirmationconditions/element.md)
  The element type of the option set.
- [ConfirmationConditions.RawValue](confirmationconditions/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static let lowConfidenceSource: ConfirmationConditions](confirmationconditions/lowconfidencesource.md)
  Only confirm if initiated from a low-confidence action source.
### Default Implementations
- [Equatable Implementations](confirmationconditions/equatable-implementations.md)
- [OptionSet Implementations](confirmationconditions/optionset-implementations.md)
- [SetAlgebra Implementations](confirmationconditions/setalgebra-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/confirmationconditions)*