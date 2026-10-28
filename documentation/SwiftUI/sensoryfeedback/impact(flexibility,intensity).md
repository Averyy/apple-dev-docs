# impact(flexibility:intensity:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Provides a physical metaphor you can use to complement a visual experience.

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
static func impact(flexibility: SensoryFeedback.Flexibility, intensity: Double = 1.0) -> SensoryFeedback
```

## Discussion

Use this to provide feedback for UI elements colliding. It should supplement the user experience, since only some platforms will play feedback in response to it.

Not all platforms will play different feedback for different flexibilities and intensities of impact.

Only plays feedback on iOS and watchOS.

## See Also

### Producing a physical impact
- [static let impact: SensoryFeedback](./impact.md)
  Provides a physical metaphor you can use to complement a visual experience.
- [static func impact(weight: SensoryFeedback.Weight, intensity: Double) -> SensoryFeedback](./impact%28weight,intensity%29.md)
  Provides a physical metaphor you can use to complement a visual experience.
- [SensoryFeedback.Flexibility](./flexibility.md)
  The flexibility to be represented by a type of feedback.
- [SensoryFeedback.Weight](./weight.md)
  The weight to be represented by a type of feedback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sensoryfeedback/impact(flexibility:intensity:))*