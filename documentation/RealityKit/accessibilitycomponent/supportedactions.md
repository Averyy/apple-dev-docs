# AccessibilityComponent.SupportedActions

**Framework**: RealityKit  
**Kind**: struct

A custom action that can be invoked on an entity in response to specific user cues.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
struct SupportedActions
```

## Topics

### Initializers
- [init(rawValue: Int)](accessibilitycomponent/supportedactions/init(rawvalue:).md)
  Creates a new option set from the given raw value.
### Instance Properties
- [let rawValue: Int](accessibilitycomponent/supportedactions/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [AccessibilityComponent.SupportedActions.ArrayLiteralElement](accessibilitycomponent/supportedactions/arrayliteralelement.md)
  The type of the elements of an array literal.
- [AccessibilityComponent.SupportedActions.Element](accessibilitycomponent/supportedactions/element.md)
  The element type of the option set.
- [AccessibilityComponent.SupportedActions.RawValue](accessibilitycomponent/supportedactions/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static let activate: AccessibilityComponent.SupportedActions](accessibilitycomponent/supportedactions/activate.md)
  Tells the entity to activate itself.
- [static let decrement: AccessibilityComponent.SupportedActions](accessibilitycomponent/supportedactions/decrement.md)
  Tells the entity to decrement the value of its content.
- [static let increment: AccessibilityComponent.SupportedActions](accessibilitycomponent/supportedactions/increment.md)
  Tells the entity to increment the value of its content.
### Default Implementations
- [Equatable Implementations](accessibilitycomponent/supportedactions/equatable-implementations.md)
- [OptionSet Implementations](accessibilitycomponent/supportedactions/optionset-implementations.md)
- [SetAlgebra Implementations](accessibilitycomponent/supportedactions/setalgebra-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Improving the Accessibility of RealityKit Apps](improving-the-accessibility-of-realitykit-apps.md)
  Incorporate assistive technologies in your augmented reality app.
- [struct AccessibilityComponent](accessibilitycomponent.md)
  A component that stores accessibility information for an entity.
- [AccessibilityComponent.CustomContent](accessibilitycomponent/customcontent-swift.struct.md)
  A CustomContent struct contains the accessibility strings for the labels you apply to your accessibility content.
- [AccessibilityComponent.RotorType](accessibilitycomponent/rotortype.md)
  A context-sensitive event that helps VoiceOver users find the next instance of a related element.
- [enum AccessibilityEvents](accessibilityevents.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/accessibilitycomponent/supportedactions)*