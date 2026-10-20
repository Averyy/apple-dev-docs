# AccessibilityTechnologies

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

Accessibility technologies available to the system.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct AccessibilityTechnologies
```

## Topics

### Getting technology types
- [static let switchControl: AccessibilityTechnologies](./accessibilitytechnologies/switchcontrol.md)
  The value that represents a Switch Control, allowing the use of the entire system using controller buttons, a breath-controlled switch or similar hardware.
- [static let voiceOver: AccessibilityTechnologies](./accessibilitytechnologies/voiceover.md)
  The value that represents the VoiceOver screen reader, allowing use of the system without seeing the screen visually.
### Creating a technology type
- [init()](./accessibilitytechnologies/init%28%29.md)
  Creates a new accessibility technologies structure with an empy accessibility technology set.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Supporting types
- [struct AccessibilityAttachmentModifier](./accessibilityattachmentmodifier.md)
  A view modifier that adds accessibility properties to the view


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilitytechnologies)*