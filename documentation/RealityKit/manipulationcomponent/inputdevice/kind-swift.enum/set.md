# ManipulationComponent.InputDevice.Kind.Set

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An efficient set of input device kinds.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct Set
```

## Topics

### Initializers
- [init(ManipulationComponent.InputDevice.Kind)](./set/init%28_%29.md)
  Creates a set of input device kinds containing only the specified input device kind.
### Type Properties
- [static var all: ManipulationComponent.InputDevice.Kind.Set](./set/all.md)
  A set of all available input device kinds.
- [static var directPinch: ManipulationComponent.InputDevice.Kind.Set](./set/directpinch.md)
  A pinching hand in close proximity to content.
- [static var indirectPinch: ManipulationComponent.InputDevice.Kind.Set](./set/indirectpinch.md)
  An indirectly targeted pinching hand.
- [static var pointer: ManipulationComponent.InputDevice.Kind.Set](./set/pointer.md)
  A click-based, indirect input device.

## Relationships

### Conforms To
- [Equatable](../../../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../../../Swift/expressiblebyarrayliteral.md)
- [Hashable](../../../../Swift/hashable.md)
- [OptionSet](../../../../Swift/optionset.md)
- [RawRepresentable](../../../../Swift/rawrepresentable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)
- [SetAlgebra](../../../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/manipulationcomponent/inputdevice/kind-swift.enum/set)*