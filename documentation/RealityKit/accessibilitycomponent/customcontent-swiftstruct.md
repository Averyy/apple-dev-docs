# AccessibilityComponent.CustomContent

**Framework**: RealityKit  
**Kind**: struct

A CustomContent struct contains the accessibility strings for the labels you apply to your accessibility content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
struct CustomContent
```

## Topics

### Operators
- [static func == (AccessibilityComponent.CustomContent, AccessibilityComponent.CustomContent) -> Bool](accessibilitycomponent/customcontent-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(label: LocalizedStringResource, value: LocalizedStringResource, importance: AXCustomContent.Importance)](accessibilitycomponent/customcontent-swift.struct/init(label:value:importance:).md)
  Creates a new CustomContent with the given label, value, and importance.
### Instance Properties
- [var importance: AXCustomContent.Importance](accessibilitycomponent/customcontent-swift.struct/importance.md)
  Determines when to output custom accessibility content.
- [var label: LocalizedStringResource](accessibilitycomponent/customcontent-swift.struct/label.md)
  A localized string key that identifies the label for this content.
- [var value: LocalizedStringResource](accessibilitycomponent/customcontent-swift.struct/value.md)
  A localized string key that provides a value for the label.
### Default Implementations
- [Equatable Implementations](accessibilitycomponent/customcontent-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [Improving the Accessibility of RealityKit Apps](improving-the-accessibility-of-realitykit-apps.md)
  Incorporate assistive technologies in your augmented reality app.
- [struct AccessibilityComponent](accessibilitycomponent.md)
  A component that stores accessibility information for an entity.
- [AccessibilityComponent.SupportedActions](accessibilitycomponent/supportedactions.md)
  A custom action that can be invoked on an entity in response to specific user cues.
- [AccessibilityComponent.RotorType](accessibilitycomponent/rotortype.md)
  A context-sensitive event that helps VoiceOver users find the next instance of a related element.
- [enum AccessibilityEvents](accessibilityevents.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/accessibilitycomponent/customcontent-swift.struct)*