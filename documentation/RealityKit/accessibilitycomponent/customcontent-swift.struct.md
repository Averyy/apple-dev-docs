# AccessibilityComponent.CustomContent

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A CustomContent struct contains the accessibility strings for the labels you apply to your accessibility content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct CustomContent
```

## Topics

### Initializers
- [init(label: LocalizedStringResource, value: LocalizedStringResource, importance: AXCustomContent.Importance)](./customcontent-swift.struct/init%28label,value,importance%29.md)
  Creates a new CustomContent with the given label, value, and importance.
### Instance Properties
- [var importance: AXCustomContent.Importance](./customcontent-swift.struct/importance.md)
  Determines when to output custom accessibility content.
- [var label: LocalizedStringResource](./customcontent-swift.struct/label.md)
  A localized string key that identifies the label for this content.
- [var value: LocalizedStringResource](./customcontent-swift.struct/value.md)
  A localized string key that provides a value for the label.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)

## See Also

### Accessibility
- [Improving the Accessibility of RealityKit Apps](../improving-the-accessibility-of-realitykit-apps.md)
  Incorporate assistive technologies in your augmented reality app.
- [struct AccessibilityComponent](../accessibilitycomponent.md)
  A component that stores accessibility information for an entity.
- [AccessibilityComponent.SupportedActions](./supportedactions.md)
  A custom action that can be invoked on an entity in response to specific user cues.
- [AccessibilityComponent.RotorType](./rotortype.md)
  A context-sensitive event that helps VoiceOver users find the next instance of a related element.
- [enum AccessibilityEvents](../accessibilityevents.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/accessibilitycomponent/customcontent-swift.struct)*