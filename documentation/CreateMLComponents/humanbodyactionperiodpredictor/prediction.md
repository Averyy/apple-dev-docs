# HumanBodyActionPeriodPredictor.Prediction

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

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
- [init(period: Float, periodicity: Float)](./prediction/init%28period,periodicity%29.md)
  Creates a human body action period prediction.
### Getting the properties
- [var period: Float](./prediction/period.md)
  The duration of a human body action measured in frames.
- [var periodicity: Float](./prediction/periodicity.md)
  A score that indicates whether this frame contributes to a periodic human body action.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Performing the transformation
- [func applied(to: [Pose], eventHandler: EventHandler?) async throws -> [HumanBodyActionPeriodPredictor.Prediction]](./applied%28to,eventhandler%29.md)
  Predicts human body action periods from an array of poses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/humanbodyactionperiodpredictor/prediction)*