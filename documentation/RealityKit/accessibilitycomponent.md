# AccessibilityComponent

**Framework**: RealityKit  
**Kind**: struct

A component that stores accessibility information for an entity.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
struct AccessibilityComponent
```

#### Overview

Add an `AccessibilityComponent` to entities to provide accessibility information to the system, such as the entity’s name which VoiceOver says aloud when it describes the entity.

See [`Improving the Accessibility of RealityKit Apps`](improving-the-accessibility-of-realitykit-apps.md) for more information.

## Topics

### Creating an accessibility component
- [init()](accessibilitycomponent/init.md)
  Creates a new accessibility component with default values.
### Providing accessibility information
- [var isAccessibilityElement: Bool](accessibilitycomponent/isaccessibilityelement.md)
  A Boolean value indicating whether the receiver is an accessibility entity that an assistive application can access.
- [var label: LocalizedStringResource?](accessibilitycomponent/label.md)
  A succinct label that identifies the entity, in a localized string key.
- [var value: LocalizedStringResource?](accessibilitycomponent/value.md)
  A localized string key that represents the current value of the entity.
### Defining traits
- [var traits: UIAccessibilityTraits](accessibilitycomponent/traits.md)
  The combination of accessibility traits that best characterize the entity.
### Defining actions
- [var systemActions: AccessibilityComponent.SupportedActions](accessibilitycomponent/systemactions.md)
  The set of supported accessibility actions.
### Specifying custom data
- [var customActions: [LocalizedStringResource]](accessibilitycomponent/customactions.md)
  An array of custom actions supported by the entity, identified by their localized string key.
- [var customContent: [AccessibilityComponent.CustomContent]](accessibilitycomponent/customcontent-swift.property.md)
  An array of custom content objects that deliver accessibility information.
### Identifying the next element
- [var customRotors: [AccessibilityComponent.RotorType]](accessibilitycomponent/customrotors.md)
  An array of supported rotors.
### Structures
- [AccessibilityComponent.CustomContent](accessibilitycomponent/customcontent-swift.struct.md)
  A CustomContent struct contains the accessibility strings for the labels you apply to your accessibility content.
- [AccessibilityComponent.SupportedActions](accessibilitycomponent/supportedactions.md)
  A custom action that can be invoked on an entity in response to specific user cues.
### Enumerations
- [AccessibilityComponent.RotorType](accessibilitycomponent/rotortype.md)
  A context-sensitive event that helps VoiceOver users find the next instance of a related element.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [Improving the Accessibility of RealityKit Apps](improving-the-accessibility-of-realitykit-apps.md)
  Incorporate assistive technologies in your augmented reality app.
- [AccessibilityComponent.SupportedActions](accessibilitycomponent/supportedactions.md)
  A custom action that can be invoked on an entity in response to specific user cues.
- [AccessibilityComponent.CustomContent](accessibilitycomponent/customcontent-swift.struct.md)
  A CustomContent struct contains the accessibility strings for the labels you apply to your accessibility content.
- [AccessibilityComponent.RotorType](accessibilitycomponent/rotortype.md)
  A context-sensitive event that helps VoiceOver users find the next instance of a related element.
- [enum AccessibilityEvents](accessibilityevents.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/accessibilitycomponent)*