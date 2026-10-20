# AccessibilityComponent.SupportedActions

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A custom action that can be invoked on an entity in response to specific user cues.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct SupportedActions
```

## Topics

### Type Properties
- [static let activate: AccessibilityComponent.SupportedActions](./supportedactions/activate.md)
  Tells the entity to activate itself.
- [static let decrement: AccessibilityComponent.SupportedActions](./supportedactions/decrement.md)
  Tells the entity to decrement the value of its content.
- [static let increment: AccessibilityComponent.SupportedActions](./supportedactions/increment.md)
  Tells the entity to increment the value of its content.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Accessibility
- [Improving the Accessibility of RealityKit Apps](../improving-the-accessibility-of-realitykit-apps.md)
  Incorporate assistive technologies in your augmented reality app.
- [struct AccessibilityComponent](../accessibilitycomponent.md)
  A component that stores accessibility information for an entity.
- [AccessibilityComponent.CustomContent](./customcontent-swift.struct.md)
  A CustomContent struct contains the accessibility strings for the labels you apply to your accessibility content.
- [AccessibilityComponent.RotorType](./rotortype.md)
  A context-sensitive event that helps VoiceOver users find the next instance of a related element.
- [enum AccessibilityEvents](../accessibilityevents.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/accessibilitycomponent/supportedactions)*