# SensoryFeedback.Flexibility

**Framework**: SwiftUI  
**Kind**: struct

The flexibility to be represented by a type of feedback.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 26.0+
- watchOS 10.0+

## Declaration

```swift
struct Flexibility
```

#### Overview

`Flexibility` values can be passed to `SensoryFeedback.impact(flexibility:intensity:)`.

## Topics

### Getting flexibility values
- [static let rigid: SensoryFeedback.Flexibility](sensoryfeedback/flexibility/rigid.md)
  Indicates a collision between hard or inflexible UI objects.
- [static let soft: SensoryFeedback.Flexibility](sensoryfeedback/flexibility/soft.md)
  Indicates a collision between soft or flexible UI objects.
- [static let solid: SensoryFeedback.Flexibility](sensoryfeedback/flexibility/solid.md)
  Indicates a collision between solid UI objects of medium flexibility.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static let impact: SensoryFeedback](sensoryfeedback/impact.md)
  Provides a physical metaphor you can use to complement a visual experience.
- [static func impact(weight: SensoryFeedback.Weight, intensity: Double) -> SensoryFeedback](sensoryfeedback/impact(weight:intensity:).md)
  Provides a physical metaphor you can use to complement a visual experience.
- [static func impact(flexibility: SensoryFeedback.Flexibility, intensity: Double) -> SensoryFeedback](sensoryfeedback/impact(flexibility:intensity:).md)
  Provides a physical metaphor you can use to complement a visual experience.
- [SensoryFeedback.Weight](sensoryfeedback/weight.md)
  The weight to be represented by a type of feedback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sensoryfeedback/flexibility)*