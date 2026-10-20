# SensoryFeedback.Weight

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The weight to be represented by a type of feedback.

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
struct Weight
```

#### Overview

`Weight` values can be passed to `SensoryFeedback.impact(weight:intensity:)`.

## Topics

### Getting flexibility values
- [static let light: SensoryFeedback.Weight](./weight/light.md)
  Indicates a collision between small or lightweight UI objects.
- [static let medium: SensoryFeedback.Weight](./weight/medium.md)
  Indicates a collision between medium-sized or medium-weight UI objects.
- [static let heavy: SensoryFeedback.Weight](./weight/heavy.md)
  Indicates a collision between large or heavyweight UI objects.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Producing a physical impact
- [static let impact: SensoryFeedback](./impact.md)
  Provides a physical metaphor you can use to complement a visual experience.
- [static func impact(weight: SensoryFeedback.Weight, intensity: Double) -> SensoryFeedback](./impact%28weight,intensity%29.md)
  Provides a physical metaphor you can use to complement a visual experience.
- [static func impact(flexibility: SensoryFeedback.Flexibility, intensity: Double) -> SensoryFeedback](./impact%28flexibility,intensity%29.md)
  Provides a physical metaphor you can use to complement a visual experience.
- [SensoryFeedback.Flexibility](./flexibility.md)
  The flexibility to be represented by a type of feedback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sensoryfeedback/weight)*