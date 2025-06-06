# InputTargetComponent.InputType

**Framework**: RealityKit  
**Kind**: struct

A type of input that the `InputTargetComponent`’s entity can receive.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct InputType
```

## Topics

### Initializers
- [init(rawValue: UInt32)](inputtargetcomponent/inputtype/init(rawvalue:).md)
  Creates a new option set from the given raw value.
### Instance Properties
- [let rawValue: UInt32](inputtargetcomponent/inputtype/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [InputTargetComponent.InputType.ArrayLiteralElement](inputtargetcomponent/inputtype/arrayliteralelement.md)
  The type of the elements of an array literal.
- [InputTargetComponent.InputType.Element](inputtargetcomponent/inputtype/element.md)
  The element type of the option set.
- [InputTargetComponent.InputType.RawValue](inputtargetcomponent/inputtype/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static let all: InputTargetComponent.InputType](inputtargetcomponent/inputtype/all.md)
  All forms of input.
- [static let direct: InputTargetComponent.InputType](inputtargetcomponent/inputtype/direct.md)
  All forms of input that target content by querying proximity from the input device to the content.
- [static let indirect: InputTargetComponent.InputType](inputtargetcomponent/inputtype/indirect.md)
  All forms of input that target content using an indirect targeting mechanism.
### Default Implementations
- [Equatable Implementations](inputtargetcomponent/inputtype/equatable-implementations.md)
- [OptionSet Implementations](inputtargetcomponent/inputtype/optionset-implementations.md)
- [SetAlgebra Implementations](inputtargetcomponent/inputtype/setalgebra-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/inputtargetcomponent/inputtype)*