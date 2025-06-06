# impact

**Framework**: SwiftUI  
**Kind**: property

Provides a physical metaphor you can use to complement a visual experience.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
static let impact: SensoryFeedback
```

#### Discussion

Use this to provide feedback for UI elements colliding. It should supplement the user experience, since only some platforms will play feedback in response to it.

Only plays feedback on iOS and watchOS.

## See Also

- [static func impact(weight: SensoryFeedback.Weight, intensity: Double) -> SensoryFeedback](sensoryfeedback/impact(weight:intensity:).md)
  Provides a physical metaphor you can use to complement a visual experience.
- [static func impact(flexibility: SensoryFeedback.Flexibility, intensity: Double) -> SensoryFeedback](sensoryfeedback/impact(flexibility:intensity:).md)
  Provides a physical metaphor you can use to complement a visual experience.
- [SensoryFeedback.Flexibility](sensoryfeedback/flexibility.md)
  The flexibility to be represented by a type of feedback.
- [SensoryFeedback.Weight](sensoryfeedback/weight.md)
  The weight to be represented by a type of feedback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sensoryfeedback/impact)*