# SensoryFeedback.Flexibility

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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

## Overview

`Flexibility` values can be passed to `SensoryFeedback.impact(flexibility:intensity:)`.

## Topics

### Getting flexibility values
- [static let rigid: SensoryFeedback.Flexibility](./flexibility/rigid.md)
  Indicates a collision between hard or inflexible UI objects.
- [static let soft: SensoryFeedback.Flexibility](./flexibility/soft.md)
  Indicates a collision between soft or flexible UI objects.
- [static let solid: SensoryFeedback.Flexibility](./flexibility/solid.md)
  Indicates a collision between solid UI objects of medium flexibility.

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
- [SensoryFeedback.Weight](./weight.md)
  The weight to be represented by a type of feedback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sensoryfeedback/flexibility)*