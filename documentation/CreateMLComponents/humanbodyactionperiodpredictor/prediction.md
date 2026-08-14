# HumanBodyActionPeriodPredictor.Prediction

**Framework**: Create ML Components  
**Kind**: struct

A human body action period prediction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct Prediction
```

## Topics

### Creating a prediction
- [init(period: Float, periodicity: Float)](humanbodyactionperiodpredictor/prediction/init(period:periodicity:).md)
  Creates a human body action period prediction.
### Getting the properties
- [var period: Float](humanbodyactionperiodpredictor/prediction/period.md)
  The duration of a human body action measured in frames.
- [var periodicity: Float](humanbodyactionperiodpredictor/prediction/periodicity.md)
  A score that indicates whether this frame contributes to a periodic human body action.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func applied(to: [Pose], eventHandler: EventHandler?) async throws -> [HumanBodyActionPeriodPredictor.Prediction]](humanbodyactionperiodpredictor/applied(to:eventhandler:).md)
  Predicts human body action periods from an array of poses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/humanbodyactionperiodpredictor/prediction)*