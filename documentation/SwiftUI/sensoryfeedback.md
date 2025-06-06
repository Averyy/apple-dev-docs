# SensoryFeedback

**Framework**: SwiftUI  
**Kind**: struct

Represents a type of haptic and/or audio feedback that can be played.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
struct SensoryFeedback
```

#### Overview

This feedback can be passed to `View.sensoryFeedback` to play it.

## Topics

### Indicating start and stop
- [static let start: SensoryFeedback](sensoryfeedback/start.md)
  Indicates that an activity started.
- [static let stop: SensoryFeedback](sensoryfeedback/stop.md)
  Indicates that an activity stopped.
### Indicating changes and selections
- [static let alignment: SensoryFeedback](sensoryfeedback/alignment.md)
  Indicates the alignment of a dragged item.
- [static let decrease: SensoryFeedback](sensoryfeedback/decrease.md)
  Indicates that an important value decreased below a significant threshold.
- [static let increase: SensoryFeedback](sensoryfeedback/increase.md)
  Indicates that an important value increased above a significant threshold.
- [static let levelChange: SensoryFeedback](sensoryfeedback/levelchange.md)
  Indicates movement between discrete levels of pressure.
- [static let selection: SensoryFeedback](sensoryfeedback/selection.md)
  Indicates that a UI element’s values are changing.
- [static let pathComplete: SensoryFeedback](sensoryfeedback/pathcomplete.md)
  Indicates a drawn path has completed and/or recognized.
### Indicating the outcome of an operation
- [static let success: SensoryFeedback](sensoryfeedback/success.md)
  Indicates that a task or action has completed.
- [static let warning: SensoryFeedback](sensoryfeedback/warning.md)
  Indicates that a task or action has produced a warning of some kind.
- [static let error: SensoryFeedback](sensoryfeedback/error.md)
  Indicates that an error has occurred.
### Producing a physical impact
- [static let impact: SensoryFeedback](sensoryfeedback/impact.md)
  Provides a physical metaphor you can use to complement a visual experience.
- [static func impact(weight: SensoryFeedback.Weight, intensity: Double) -> SensoryFeedback](sensoryfeedback/impact(weight:intensity:).md)
  Provides a physical metaphor you can use to complement a visual experience.
- [static func impact(flexibility: SensoryFeedback.Flexibility, intensity: Double) -> SensoryFeedback](sensoryfeedback/impact(flexibility:intensity:).md)
  Provides a physical metaphor you can use to complement a visual experience.
- [SensoryFeedback.Flexibility](sensoryfeedback/flexibility.md)
  The flexibility to be represented by a type of feedback.
- [SensoryFeedback.Weight](sensoryfeedback/weight.md)
  The weight to be represented by a type of feedback.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> some View](view/sensoryfeedback(_:trigger:).md)
  Plays the specified `feedback` when the provided `trigger` value changes.
- [func sensoryFeedback<T>(trigger: T, (T, T) -> SensoryFeedback?) -> some View](view/sensoryfeedback(trigger:_:).md)
  Plays feedback when returned from the `feedback` closure after the provided `trigger` value changes.
- [func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) -> Bool) -> some View](view/sensoryfeedback(_:trigger:condition:).md)
  Plays the specified `feedback` when the provided `trigger` value changes and the `condition` closure returns `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sensoryfeedback)*